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
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

S3URL = "https://s3-us-west-2.amazonaws.com/legiongis.com"

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
    
    ("{}/img/map_gallery/Gunthorp Farm.png".format(S3URL), 'Food Producer Cluster map for Crossroads Resource Center'),
    ("{}/img/map_gallery/CRC_ME_elevation.png".format(S3URL), 'Phyiographic map for Crossroads Resource Center'),
    ("{}/img/map_gallery/FullCounty_physiographic.png".format(S3URL), 'Hazard Mitigation map for OCR West'),
    ("{}/img/map_gallery/SanAugustineDetail.jpg".format(S3URL), 'Hazard Mitigation map for MPTX'),
    ("{}/img/map_gallery/viroqua_to_sidieFINAL (Morea) reduce.png".format(S3URL), 'Virqua/Sidie Hollow area map for Vernon Trails'),
    ("{}/img/map_gallery/CenturyRideMaps2015_draft3.png".format(S3URL), 'Century Ride brochure map for Bike Natchitoches'),
    ("{}/img/map_gallery/Walmsley Graves 11x17.jpg".format(S3URL), 'American Cemetery map just for fun'),
    )
    

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
