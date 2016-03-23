#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'LegionGIS'
SITENAME = u'Legion GIS'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
PUBLISH_DATE = date.today().strftime("%b %d, %Y")

SUMMARY_MAX_LENGTH = 25

THEME = "theme"

SERVICES_PAGES = (
    ('Arches', "{}/pages/services/arches.html".format(SITEURL)),
    ('Cartography', "{}/pages/services/cartography.html".format(SITEURL)),
    ('Education', "{}/pages/services/education.html".format(SITEURL)),
    )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# links of interest
LINKS = (
    ('Quantum GIS', 'http://qgis.org/'),
    ('ArcGIS', 'http://esri.com/'),
    ('Arches', 'http://archesproject.org/'),
    ('GIMP', 'http://gimp.org'),
    ('GeoServer', 'http://geoserver.org'),
    ('Inkscape', 'http://inkscape.org'),
    ('Python', 'http://python.org/'),
    ('Amazon Web Services', 'https://aws.amazon.com/'),
    ('Pelican', 'http://getpelican.com/'),
    ('TileMill', 'https://www.mapbox.com/tilemill/'),
    )

MAP_GALLERY = (
    
    ("{}/theme/img/map_gallery/Gunthorp Farm.png".format(SITEURL), 'Food Producer Cluster map for Crossroads Resource Center'),
    ("{}/theme/img/map_gallery/CRC_ME_elevation.png".format(SITEURL), 'Phyiographic map for Crossroads Resource Center'),
    ("{}/theme/img/map_gallery/FullCounty_physiographic.png".format(SITEURL), 'Hazard Mitigation map for OCR West'),
    ("{}/theme/img/map_gallery/SanAugustineDetail.jpg".format(SITEURL), 'Hazard Mitigation map for MPTX'),
    ("{}/theme/img/map_gallery/viroqua_to_sidieFINAL (Morea) reduce.png".format(SITEURL), 'Virqua/Sidie Hollow area map for Vernon Trails'),
    ("{}/theme/img/map_gallery/CenturyRideMaps2015_draft3.png".format(SITEURL), 'Century Ride brochure map for Bike Natchitoches'),
    ("{}/theme/img/map_gallery/Walmsley Graves 11x17.jpg".format(SITEURL), 'American Cemetery map just for fun'),
    )
    

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
