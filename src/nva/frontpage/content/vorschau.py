# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from z3c.relationfield.schema import RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid
from zope.interface import invariant


from nva.frontpage import _


blockshapes = SimpleVocabulary((
    SimpleTerm(value=u'left-top', token=u'left-top', title=u'Bild links oben'),
    SimpleTerm(value=u'left-bottom', token=u'left-bottom', title=u'Bild links unten'),
    SimpleTerm(value=u'right-top', token=u'right-top', title=u'Bild rechts oben'),
    SimpleTerm(value=u'right-bottom', token=u'right-bottom', title=u'Bild rechts unten'),
    SimpleTerm(value=u'textblock', token=u'textblock', title=u'Textblock'),
    SimpleTerm(value=u'stage', token=u'stage', title=u'Bühnenbild'),
    ))

cssclasses = SimpleVocabulary((
    SimpleTerm(value=u'bg-white', token=u'bg-white', title=u'weisser Hintergrund'),
    SimpleTerm(value=u'bg-light', token=u'bg-light', title=u'hellgrauer Hintergrund'),
    SimpleTerm(value=u'bg-secondary', token=u'bg-secondary', title=u'dunkelgrauer Hintergrund'),
    ))


class IVorschau(model.Schema):
    """ Marker interface and Dexterity Python Schema for Vorschau
    """

    dachzeile = schema.TextLine(title=u"Dachzeile", required=False)

    text = RichText(title=u"Textblock", required=False)

    link = schema.URI(title=u"Link auf eine externe Information", required=False,
                                    description=u"Es muss ein Link oder ein interner Verweis eingegeben werden.")

    verweis = RelationChoice(title=u"Interner Verweis", required=False,
                                    description=u"Wenn vorhanden überschreibt der Verweis den externen Link.",
                                    source=CatalogSource())

    linktitle = schema.TextLine(title=u"Titel des Links auf der Landingpage", required=True,
                                    default="mehr erfahren")

    image = NamedBlobImage(title=u"Vorschaubild", required=False)

    blockshape = schema.Choice(title=u"Aussehen des Blocks", required=True,
                                    vocabulary=blockshapes,
                                    default='stage')

    blockclass = schema.Choice(title=u"CSS-Klasse des Blocks", required=True,
                                    vocabulary=cssclasses,
                                    default='bg-light')

    bannerclass = schema.Choice(title=u"CSS-Klasse des Bildbanners", required=True,
                                    vocabulary=cssclasses,
                                    default='bg-white')


    @invariant
    def image_invariant(data):
        if data.blockshape not in ['textblock',]:
            if not data.image:
                raise Invalid(_(u'Bei diesem Aussehen des Blocks ist ein Vorschaubild erforderlich.'))
            if not data.link and not data.verweis:
                raise Invalid(_(u'Es muss ein Link oder eine interner Verweis angegeben werden.'))

    @invariant
    def textblock_invariant(data):
        if data.blockshape in ['textblock',]:
            if not data.text:
                raise Invalid(_(u'Bei diesem Aussehen des Blocks ist ein Textblock erforderlich.'))


@implementer(IVorschau)
class Vorschau(Container):
    """
    """

    def format_link(self):
        if self.verweis:
            return self.verweis.to_object.absolute_url()
        return self.link
