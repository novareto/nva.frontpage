# -*- coding: utf-8 -*-

from nva.frontpage import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class VorschauStageView(BrowserView):
    template = ViewPageTemplateFile('templates/vorschau/vorschau_stage_view.pt')

    def __call__(self):
        self.vorschau = self.context
        if self.context.verweis:
            self.vorschau.verweis = self.context.verweis.absolute_url()
        else:
            self.vorschau.verweis = self.context.link
        self.vorschau = self.context.__dict__
        return self.template()


class VorschauTextblockView(BrowserView):
    template = ViewPageTemplateFile('templates/vorschau/vorschau_textblock_view.pt')

    def __call__(self):
        self.vorschau = self.context
        if self.context.verweis:
            self.vorschau.verweis = self.context.verweis.absolute_url()
        else:
            self.vorschau.verweis = self.context.link
        self.vorschau = self.context.__dict__
        return self.template()


class VorschauLeftBottomView(BrowserView):
    template = ViewPageTemplateFile('templates/vorschau/vorschau_left-bottom_view.pt')

    def __call__(self):
        self.vorschau = self.context
        if self.context.verweis:
            self.vorschau.verweis = self.context.verweis.absolute_url()
        else:
            self.vorschau.verweis = self.context.link
        self.vorschau = self.context.__dict__
        return self.template()


class VorschauLeftTopView(BrowserView):
    template = ViewPageTemplateFile('templates/vorschau/vorschau_left-top_view.pt')

    def __call__(self):
        self.vorschau = self.context
        if self.context.verweis:
            self.vorschau.verweis = self.context.verweis.absolute_url()
        else:
            self.vorschau.verweis = self.context.link
        self.vorschau = self.context.__dict__
        return self.template()


class VorschauRightBottomView(BrowserView):
    template = ViewPageTemplateFile('templates/vorschau/vorschau_right-bottom_view.pt')

    def __call__(self):
        self.vorschau = self.context
        if self.context.verweis:
            self.vorschau.verweis = self.context.verweis.absolute_url()
        else:
            self.vorschau.verweis = self.context.link
        self.vorschau = self.context.__dict__
        return self.template()


class VorschauRightTopView(BrowserView):
    template = ViewPageTemplateFile('templates/vorschau/vorschau_right-top_view.pt')
    def __call__(self):
        self.vorschau = self.context
        if self.context.verweis:
            self.vorschau.verweis = self.context.verweis.absolute_url()
        else:
            self.vorschau.verweis = self.context.link
        self.vorschau = self.context.__dict__
        return self.template()
