# -*- coding: utf-8 -*-

from nva.frontpage import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LandingView(BrowserView):

    def __call__(self):
        self.pagecontents = self.get_pagecontents()
        return self.index()

    def getMacro(self, pageitem):
        vorschauname = ViewPageTemplateFile('templates/vorschau/vorschau_'+pageitem.blockshape+'_view.pt').id.split("_")[1]
        return ViewPageTemplateFile('templates/vorschau/vorschau_' + vorschauname + '_view.pt').macros[vorschauname]

    def createSnippet(self, obj):
        if obj.portal_type == 'Link':
            return createLinkSnippet(obj)

    def get_pagecontents(self):
        objekte = self.context.listFolderContents()
        for item in objekte:
            item.url = item.absolute_url()
        return objekte

    def getRemote(self, item):
        remote = item.remoteUrl
        if 'resolveuid' in remote:
            uid = remote.split('/')[-1]
            obj = ploneapi.content.get(UID=uid)
            if obj:
                return obj.absolute_url()
        return remote

    def formatEvent(self, item):
        event = u''
        if item.start and item.end:
            event = "%s-%s" % (item.start.strftime('%d.%m.%Y'), item.end.strftime('%d.%m.%Y'))
        elif item.start and not item.end:
            event = "%s" % item.start.strftime('%d.%m.%Y')
        if item.location:
            event += ", %s" % item.location
        return event

    def getCollectionEntries(self, item):
        data = {'cards': [], 'morelink': None}
        artikel = ploneapi.content.get_view('enhanced_foldersummary', item, self.request).contentlist()
        if item.deckshape == '1-4-0':
            if len(artikel) > 4:
                artikel = artikel[:4]
                data['morelink'] = item.decklink  # Der Link mit weiteren Objekten muss angezeigt werden
            data['cards'] = artikel
        elif item.deckshape == '2-3-4':
            if len(artikel) > 7:
                artikel = artikel[:7]
                data['morelink'] = item.decklink  # Der Link mit weiteren Objekten muss angezeigt werden
            data['cards'] = [artikel[:3], artikel[3:]]
        return data
