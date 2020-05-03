# -*- coding: utf-8 -*-

from nva.frontpage import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


deckshapes = SimpleVocabulary((
    SimpleTerm(value=u'2-3-4', token=u'2-3-4', title=u"Zwei Zeilen, 3 Karten oben, dann 4 Karten"),
    SimpleTerm(value=u'1-4-0', token=u'1-4-0', title=u"Eine Zeile, 4 Karten"),
    ))

cssclasses = SimpleVocabulary((
    SimpleTerm(value=u'bg-white', token=u'bg-white', title=u'weisser Hintergrund'),
    SimpleTerm(value=u'bg-light', token=u'bg-light', title=u'hellgrauer Hintergrund'),
    SimpleTerm(value=u'bg-secondary', token=u'bg-secondary', title=u'dunkelgrauer Hintergrund'),
    ))


class ILandingPageShapeMarker(Interface):
    pass

@provider(IFormFieldProvider)
class ILandingPageShape(model.Schema):
    """
    """

    model.fieldset(
        'landingpage',
        label=_(u"Landingpage"),
        fields=['deckshape', 'deckclass', 'decklink']
    )

    deckshape = schema.Choice(title=u"Aussehen des Kartendecks", required=True,
                              vocabulary=deckshapes,
                              default=u'1-4-0')

    deckclass = schema.Choice(title=u"CSS-Klasse des Kartendecks", required=True,
                              vocabulary=cssclasses,
                              default=u"bg-light")

    decklink = schema.TextLine(title=u"Beschriftung des Links für mehr Artikel", required=True,
                              default=u"Alle Artikel")


@implementer(ILandingPageShape)
@adapter(ILandingPageShapeMarker)
class LandingPageShape(object):
    def __init__(self, context):
        self.context = context

    @property
    def deckshape(self):
        if hasattr(self.context, 'deckshape'):
            return self.context.deckshape
        return None

    @deckshape.setter
    def deckshape(self, value):
        self.context.deckshape = value

    @property
    def deckclass(self):
        if hasattr(self.context, 'deckclass'):
            return self.context.deckclass
        return None

    @deckclass.setter
    def deckclass(self, value):
        self.context.deckclass = value

    @property
    def decklink(self):
        if hasattr(self.context, 'decklink'):
            return self.context.decklink
        return None

    @decklink.setter
    def decklink(self, value):
        self.context.decklink = value        
