# -*- coding: utf-8 -*-

from nva.frontpage import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi
from nva.frontpage.views.createMyLinkSnippet import createLinkSnippet


class LandingView(BrowserView):

    def __call__(self):
        self.pagecontents = self.get_pagecontents()
        return self.index()

    def createSnippet(self, obj):
        if obj.portal_type == 'Link':
            return createLinkSnippet(obj)

    def get_pagecontents(self):
        objekte = self.context.listFolderContents()
        return objekte

    def getRemote(self, item):
        remote = item.remoteUrl
        if 'resolveuid' in remote:
            uid = remote.split('/')[-1]
            obj = ploneapi.content.get(UID=uid)
            if obj:
                return obj.absolute_url()
        return remote

    def getCollectionEntries(self, item):
        artikel = ploneapi.content.get_view('enhanced_foldersummary', item, self.request).contentlist()
        size = 4
        cards = [artikel[i:i+size] for i in range(0, len(artikel), size)]
        return cards
