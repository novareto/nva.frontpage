# -*- coding: utf-8 -*-
from nva.frontpage.content.vorschau import IVorschau  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class VorschauIntegrationTest(unittest.TestCase):

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

    def test_ct_vorschau_schema(self):
        fti = queryUtility(IDexterityFTI, name='Vorschau')
        schema = fti.lookupSchema()
        self.assertEqual(IVorschau, schema)

    def test_ct_vorschau_fti(self):
        fti = queryUtility(IDexterityFTI, name='Vorschau')
        self.assertTrue(fti)

    def test_ct_vorschau_factory(self):
        fti = queryUtility(IDexterityFTI, name='Vorschau')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IVorschau.providedBy(obj),
            u'IVorschau not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_vorschau_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Vorschau',
            id='vorschau',
        )

        self.assertTrue(
            IVorschau.providedBy(obj),
            u'IVorschau not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('vorschau', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('vorschau', parent.objectIds())

    def test_ct_vorschau_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Vorschau')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
