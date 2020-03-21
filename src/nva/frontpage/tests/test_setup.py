# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that nva.frontpage is properly installed."""

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if nva.frontpage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'nva.frontpage'))

    def test_browserlayer(self):
        """Test that INvaFrontpageLayer is registered."""
        from nva.frontpage.interfaces import (
            INvaFrontpageLayer)
        from plone.browserlayer import utils
        self.assertIn(
            INvaFrontpageLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['nva.frontpage'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if nva.frontpage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'nva.frontpage'))

    def test_browserlayer_removed(self):
        """Test that INvaFrontpageLayer is removed."""
        from nva.frontpage.interfaces import \
            INvaFrontpageLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            INvaFrontpageLayer,
            utils.registered_layers())
