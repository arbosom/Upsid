#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:49:49 2019

@author: tanguy
"""
import folium
import json
geo=json.load(open("geolocalisation.json"))
c= folium.Map(location=[0, 0],
    zoom_start=2,
    attr='Geolocalisation',
    tiles='Stamen Toner')

for nom,valeurs in geo.items():
    for variete,loc in valeurs.items():
        if loc:
            for i,point in enumerate(loc):
                folium.Marker(
                    location=[eval(point[1]), eval(point[0])],
                    popup='%s: %s %g'%(nom,variete,i),
                    icon=folium.Icon(color='red', icon='info-sign')
                ).add_to(c)

c.save('maCarte.html')