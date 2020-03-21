# -*- coding: utf-8 -*-
from nva.frontpage.content.card import ICard  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CardIntegrationTest(unittest.TestCase):

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

    def test_ct_card_schema(self):
        fti = queryUtility(IDexterityFTI, name='Card')
        schema = fti.lookupSchema()
        self.assertEqual(ICard, schema)

    def test_ct_card_fti(self):
        fti = queryUtility(IDexterityFTI, name='Card')
        self.assertTrue(fti)

    def test_ct_card_factory(self):
        fti = queryUtility(IDexterityFTI, name='Card')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICard.providedBy(obj),
            u'ICard not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_card_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Card',
            id='card',
        )

        self.assertTrue(
            ICard.providedBy(obj),
            u'ICard not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('card', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('card', parent.objectIds())

    def test_ct_card_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Card')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
