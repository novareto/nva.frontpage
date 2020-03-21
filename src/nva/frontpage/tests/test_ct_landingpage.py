# -*- coding: utf-8 -*-
from nva.frontpage.content.landingpage import ILandingpage  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class LandingpageIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_landingpage_schema(self):
        fti = queryUtility(IDexterityFTI, name='Landingpage')
        schema = fti.lookupSchema()
        self.assertEqual(ILandingpage, schema)

    def test_ct_landingpage_fti(self):
        fti = queryUtility(IDexterityFTI, name='Landingpage')
        self.assertTrue(fti)

    def test_ct_landingpage_factory(self):
        fti = queryUtility(IDexterityFTI, name='Landingpage')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ILandingpage.providedBy(obj),
            u'ILandingpage not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_landingpage_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Landingpage',
            id='landingpage',
        )

        self.assertTrue(
            ILandingpage.providedBy(obj),
            u'ILandingpage not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('landingpage', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('landingpage', parent.objectIds())

    def test_ct_landingpage_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Landingpage')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_landingpage_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Landingpage')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'landingpage_id',
            title='Landingpage container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
