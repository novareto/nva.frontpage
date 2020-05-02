# -*- coding: utf-8 -*-
from nva.frontpage.content.textblock import ITextblock  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class TextblockIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Landingpage',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_textblock_schema(self):
        fti = queryUtility(IDexterityFTI, name='Textblock')
        schema = fti.lookupSchema()
        self.assertEqual(ITextblock, schema)

    def test_ct_textblock_fti(self):
        fti = queryUtility(IDexterityFTI, name='Textblock')
        self.assertTrue(fti)

    def test_ct_textblock_factory(self):
        fti = queryUtility(IDexterityFTI, name='Textblock')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITextblock.providedBy(obj),
            u'ITextblock not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_textblock_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Textblock',
            id='textblock',
        )

        self.assertTrue(
            ITextblock.providedBy(obj),
            u'ITextblock not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('textblock', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('textblock', parent.objectIds())

    def test_ct_textblock_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Textblock')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_textblock_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Textblock')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'textblock_id',
            title='Textblock container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
