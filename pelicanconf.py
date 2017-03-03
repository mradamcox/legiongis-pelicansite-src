#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'LegionGIS'
SITENAME = u'Legion GIS, LLC'
SITESUBTITLE = 'geospatial consulting and research'

SITEURL = 'http://legiongis.com'

PATH = 'content'
THEME = 'theme'

# keep this false, because output directory has its own git init files
# which must stay intact!!!
DELETE_OUTPUT_DIRECTORY = False

# set format like this: March 23, 2016
DEFAULT_DATE_FORMAT = ('%B %d, %Y')

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
PUBLISH_DATE = date.today().strftime("%b %d, %Y")

SUMMARY_MAX_LENGTH = 25

SERVICES = ('arches','services','cartographic services','education','Introduction to QGIS Course',
    'Arches support and hosting',)
BACKGROUND = ('background')
BLOG_PAGES = ('blog')

STATIC_PATHS = [
    #'extra/robots.txt', 
    'extra/favicon.ico',
    'csp',
    #'maps',
    's',
]

READERS = {'html': None}

EXTRA_PATH_METADATA = {
    #'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

QUICK_LINKS = (
    ('Arches Services', "arches-services.html"),
    ('Cartographic Work Examples', "cartographic-services.html"),
    ('Crawford Stewardship Project', "csp-volunteer-efforts.html"),
    ('Introduction to GIS Course', "introduction-to-gis-course.html"),
    ('Blog Posts With Web Maps', "tag/web-maps.html"),
)

# the thought is that the map templates that are included in some blog posts
# can also be written directly to the output 
DIRECT_TEMPLATES = [
    r'maps/afrh-historicmaps',
]

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

# create client list (url,logo)
CLIENTS = (
    ('http://valleystewardshipnetwork.org/',S3URL+'/img/client-logos/gci.png'),
    ('http://home.preservescapes.com/', S3URL+'/img/client-logos/preservescapes.png'),
    ('http://www.crawfordstewardshipproject.org/',S3URL+'/img/client-logos/csp.png'),
    ('http://www.crcworks.org/',S3URL+'/img/client-logos/crc.png'),
    ('http://valleystewardshipnetwork.org/',S3URL+'/img/client-logos/vsn-black.png'),
    ('http://www.windingroadsart.com/',S3URL+'/img/client-logos/wrat.png'),
    ('http://www.vernoncountyhistory.org/',S3URL+'/img/client-logos/vchs.png'),
    ('http://www.melroseplantation.org/',S3URL+'/img/client-logos/melrose.png'),
    ('http://www.canerivernha.org/',S3URL+'/img/client-logos/crnha_logo.png'),
    
)

# create the list for map gallery: (fullsize,thumb,description)
MAP_GALLERY_URL = S3URL+"/img/map_gallery"
MAP_GALLERY = (
    (MAP_GALLERY_URL+"/Gunthorp+Farm.png",MAP_GALLERY_URL+"/thumbs/Gunthorp%2BFarm_thumb.png",
        'food producer cluster map, for Crossroads Resource Center'),
    (MAP_GALLERY_URL+"/CRC_ME_elevation.png",MAP_GALLERY_URL+"/thumbs/CRC_ME_elevation_thumb.png",
        'physiographic map showing counties in Maine, for Crossroads Resource Center'),
    (MAP_GALLERY_URL+"/FullCounty_physiographic.png",MAP_GALLERY_URL+"/thumbs/FullCounty_physiographic_thumb.png",
        'Lane County Oregon, for OCR West hazard mitigation planning document'),
    (MAP_GALLERY_URL+"/SanAugustineDetail.jpg",MAP_GALLERY_URL+"/thumbs/SanAugustineDetail_thumb.jpg",
        'City of San Augustine for MPTX hazard mitigation planning document'),
    (MAP_GALLERY_URL+"/viroqua_to_sidieFINAL (Morea) reduce.png",MAP_GALLERY_URL+"/thumbs/viroqua_to_sidieFINAL%2B(Morea)%2Breduce_thumb.png",
        'bike map of Sidie Hollow/Viroqua, WI area, for Vernon Trails'),
    (MAP_GALLERY_URL+"/CenturyRideMaps2015_draft3.png",MAP_GALLERY_URL+"/thumbs/CenturyRideMaps2015_draft3_thumb.png",
        '2nd Annual Century Ride brochure map, for Bike Natchitoches'),
    (MAP_GALLERY_URL+"/Walmsley+Graves+11x17.jpg",MAP_GALLERY_URL+"/thumbs/Walmsley%2BGraves%2B11x17_thumb.jpg",
        'American Cemetery, automated product of gravefinder ArcGIS toolbox'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
