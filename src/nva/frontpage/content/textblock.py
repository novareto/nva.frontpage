# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


from nva.frontpage import _


class ITextblock(model.Schema):
    """ Marker interface and Dexterity Python Schema for Textblock
    """

    title = schema.TextLine(title=u"Titel", required=True,
                            description=u"Der Titel wird auf der Landingpage nicht eingeblendet.")

    dachzeile = schema.TextLine(title=u"Dachzeile", required=False)

    text = RichText(title=u"Haupttext", required=True)


@implementer(ITextblock)
class Textblock(Container):
    """
    """
