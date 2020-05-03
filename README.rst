=============
nva.frontpage
=============

Mit nva.frontpage kann auf einer Plone-Site mit plonetheme.tokyo und plonetheme.siguv an jeder Stelle des Portals eine Landingpage eingestellt 
werden. Das Package nva.frontpage stellt kein generisches Produkt für das CMS Plone dar, sondern ist speziell für die Bedürfnisse der 
SIGUV-Gemeinschaft konzipiert.

Eine Landingpage besteht aus Blöcken, die über die Sortierung im Ordner beliebig nach oben und unten verschoben werden können.

- Für statische Informationen in den Blöcken kann der Artikeltyp "Vorschau" verwendet werden.
- Für alle Blöcke mit mehr als einem Artikel oder für Blöcke mit dynamischen Inhalten können Ordner oder Kollektionen verwendet werden.

Für die Vorschau können auf der Landingpage folgende Darstellungsformen ausgewählt werden:

- Bild links oben (Text rechts unten)
- Bild links unten (Text rechts oben)
- Bild rechts oben (Text links unten)
- Bild rechts unten (Text links oben)
- Textblock (Text aus Haupttext mittig zentriert)
- Bühnenbild

Für Ordner und Kollektionen können Kartendecks mit folgender Aufteilung gewählt werden:

- Zwei Zeilen, 3 Karten oben, dann 4 Karten
- Eine Zeile, 4 Karten

Die Konfigurationseinstellung für die Vorschau erfolgt beim Anlegen des Artikels. Für Ordner und Kollektionen muss das Behavior "Landingpage"
aktiviert werden. Hier können die Einstellungen vorgenommen werden.

Features
--------

Das Package umfasst 2 Inhaltstypen:

- Landingpage (Container)
- Vorschau (Container)

Einer Landingpage können folgende Inhaltstypen hinzugefügt werden:

- Vorschau (einer Vorschau können nur Bilder zur Anzeige in deren Haupttext hinzugefügt werden)
- Ordner (Standard-Plone-Ordner)
- Kollektion (Standard-Plone-Kollektion)

Das Package enthält das Behavior Landingpage, dass den Artikeltypen Ordner und Kollektion zugeordnet werden muss.

Das Package enthält den Browserview landing_view als Standardansicht der Landingpage. Hier sind alle möglichen Blöcke enthalten und
auch dokumentiert.

Examples
--------

https://newbgetem.bg-kooperation.de/startseite-der-bg-etem

Documentation
-------------

Im Package und auf dieser Seite

Translations
------------

Das Package existiert nur in Deutscher Sprache

Installation
------------

Installiere nva.frontpage durch Hinzufügen des Packages zur buildout::

    [buildout]

    ...

    eggs =
        nva.frontpage


danach muss buildout ausgeführt werden: ``bin/buildout``

Danach muss das Behavior "Landingpage" den Inhaltstypen Ordner und Kollektion zugeordnet werden.


Contribute
----------

- Issue Tracker: https://github.com/collective/nva.frontpage/issues
- Source Code: https://github.com/collective/nva.frontpage


Support
-------

lwalther@novareto.de

License
-------

The project is licensed under the GPLv2.
