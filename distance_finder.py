#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:51:08 2021

@author: christianschoeberl
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#Author: Christian Schoeberl 
#example URL to match 

#https://www.mapquest.com/directions/from/us/pennsylvania/pittsburgh/
#15213-1454/4101-bigelow-blvd-40.450207,-79.954566/to/us/pa/pittsburgh/
#15213-4450/3328-ward-st-40.434066,-79.954726

#example coordinates 
#need zip code, don't need lat/long for it to work 
start = "15213-1454/4101-bigelow-blvd"
end = "15213-4450/3328-ward-st"
page = requests.get("https://www.mapquest.com/directions/from/us/pennsylvania" +
                    "/pittsburgh/" + start + "/to/us/pa/pittsburgh/" + end)
page.raise_for_status()
soup = BeautifulSoup(page.content, 'html.parser')
narrative = soup.find(id="primaryPanel")
distance_full = narrative.find_all('div', {'class': 'distance primary-only'})
distance_strip= distance_full[0]
distance_store= []
for i in distance_strip:
    distance_store.append(i)
distance = float(distance_store[0])
print(distance)

    
