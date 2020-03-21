# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import nva.frontpage


class NvaFrontpageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=nva.frontpage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nva.frontpage:default')


NVA_FRONTPAGE_FIXTURE = NvaFrontpageLayer()


NVA_FRONTPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NVA_FRONTPAGE_FIXTURE,),
    name='NvaFrontpageLayer:IntegrationTesting',
)


NVA_FRONTPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NVA_FRONTPAGE_FIXTURE,),
    name='NvaFrontpageLayer:FunctionalTesting',
)


NVA_FRONTPAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NVA_FRONTPAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NvaFrontpageLayer:AcceptanceTesting',
)
