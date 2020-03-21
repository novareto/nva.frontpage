# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class ILandingpage(model.Schema):
    """ Marker interface and Dexterity Python Schema for Landingpage
    """

    text = RichText(title=u"Haupttext der Seite", required=False)

    show_title = schema.Bool(title=u"Titel der Seite anzeigen", default=False)

    show_description = schema.Bool(title=u"Kurzbeschreibung der Seite anzeigen", default=False)


@implementer(ILandingpage)
class Landingpage(Container):
    """
    """
