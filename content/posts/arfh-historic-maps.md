Title: Using Historic Maps of the Armed Forces Retirement Home
Date: 2016-08-04
Category: arches
Author: Adam Cox
Tags: preservation, Arches, web maps, historic maps
Maphtml: maps/afrh-historicmaps.html
Mapcaption: 12 historic map overlays created for the Armed Forces Retirement Home Arches installation. Historic maps courtesy of AFRH, map citations courtesy of Carrie Barton, PRESERVE/scapes.

One aspect of developing an Arches app is the configuration of the database's map view, one component of which is figuring out what layers to use. Which basemaps? Where will the aerial imagery come from? Can historic maps be included as overlays? To test all these things out, I generally make a light-weight webmap that can serve as a testing ground. Below is the result of the development of the AFRH Arches app.

Generally, there are suitable basemap layers out there somewhere. In this case, we used open street map's default tile rendering for the street map, and a 2013 aerial photograph tileset published by DCGIS for the imagery. (In an earlier iteration, we used MapQuest tiles which was great because they had a separate "labels" layer that we grouped with the imagery to make a very nice-looking hybrid layer. Then MapQuest discontinued their tile service. Bummer.)

The more interesting part of the process is always the creation of the historic map layers. Legion GIS was provided with 12 high resolution scans of these maps, ranging in date from 1850 to 1975, and then the fun begins. Full details on our favorite image processing techniques are for another post, but through some GIMP processing, ArcGIS/QGIS georeferencing, and GDAL resampling we are able to create nice, as-light-weight-as-possible GeoTiffs. These are published as Web Map Services through GeoServer, and the result is shown below.

Enjoy!