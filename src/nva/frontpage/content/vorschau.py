# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.dexterity.content import Item
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


directions = SimpleVocabulary((
                 SimpleTerm(value=u'left', token=u'left', title=u'links'),
                 SimpleTerm(value=u'center', token=u'center', title=u'mittig'),
                 SimpleTerm(value=u'right', token=u'right', title=u'rechts'),
                 ))


class IVorschau(model.Schema):
    """ Marker interface and Dexterity Python Schema for Vorschau
    """

    dachzeile = schema.TextLine(title=u"Dachzeile", required=False)

    link = schema.URI(title=u"Link auf eine externe Information", required=False)

    verweis = schema.RelationChoice(title=u"Interner Verweis", required=False,
                                    description=u"Wenn vorhanden überschreibt der Verweis den externen Link.",
                                    source=CatalogSource())

    linktitle = schema.TextLine(title=u"Titel des Links auf der Landingpage", required=False)

    image = NamedBlobImage(title=u"Vorschaubild", required=False)

    ausrichtung = schema.Choice(title=u"Ausrichtung der Ansicht", required=True,
                                    vocabulary=directions,
                                    default='left')

    @invariant
    def link_invariant(data):
        if data.link or data.verweis:
            if not data.linktitle:
                raise Invalid(_(u'Bei Auswahl eines Links muss ein Linktitel angegeben werden.'))


@implementer(IVorschau)
class Vorschau(Item):
    """
    """
