# -*- coding: utf-8 -*-
from nva.frontpage.behaviors.landing_page_shape import ILandingPageShapeMarker
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class LandingPageShapeIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_landing_page_shape(self):
        behavior = getUtility(IBehavior, 'nva.frontpage.landing_page_shape')
        self.assertEqual(
            behavior.marker,
            ILandingPageShapeMarker,
        )
