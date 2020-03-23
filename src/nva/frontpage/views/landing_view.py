# -*- coding: utf-8 -*-

from nva.frontpage import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LandingView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('landing_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.pagecontents = self.get_pagecontents()
        return self.index()

    def get_pagecontents(self):
        return self.context.listFolderContents()

    def getRemote(self, item):
        remote = item.remoteUrl
        if 'resolveuid' in remote:
            uid = remote.split('/')[-1]
            obj = ploneapi.content.get(UID=uid)
            if obj:
                return obj.absolute_url()
        return remote
