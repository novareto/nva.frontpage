# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from plone.namedfile.field import NamedBlobImage
from z3c.relationfield.schema import RelationChoice
from plone.app.vocabularies.catalog import CatalogSource


class ICard(model.Schema):
    """ Marker interface and Dexterity Python Schema for Card
    """

    cardclass = schema.TextLine(title=u"Style-Klasse der Karte", required=False)

    cardhaeder = schema.TextLine(title=u"Kopf der Karte", required=False)
    
    calltoaction = RelationChoice(title=u"Referenz auf der Seite", source=CatalogSource(), required=False)

    buttonclass = schema.TextLine(title=u"Buttonklasse", required=False)

    cardimage = NamedBlobImage(title=u"Titelbild der Karte", required=False)


@implementer(ICard)
class Card(Item):
    """
    """
