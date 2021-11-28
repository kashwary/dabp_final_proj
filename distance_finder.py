#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:51:08 2021

@author: christianschoeberl
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv 
import time 

#Author: Christian Schoeberl 
#example URL to match 

#https://www.mapquest.com/directions/from/us/pennsylvania/pittsburgh/
#15213-1454/4101-bigelow-blvd-40.450207,-79.954566/to/us/pa/pittsburgh/
#15213-4450/3328-ward-st-40.434066,-79.954726

#load in addys
full_schools = pd.read_excel("school_full_addresses.xlsx")
full_hospitals = pd.read_excel("hospital_full_addresses.xlsx")

#separate addies& cities 
school_addresses = pd.DataFrame(full_schools, columns=["New address"])
school_cities = pd.DataFrame(full_schools, columns=['[city_name]'])
num_schools = len(school_addresses)

hospital_addresses = pd.DataFrame(full_hospitals, columns=['Address'])
hospital_cities = pd.DataFrame(full_hospitals, columns=['City'])
num_hospitals = len(hospital_addresses)

#storing matrix 
#row = school; col = hospitals
full_distances = [[0 for r in range(num_hospitals)] for u in range(num_schools)]
for i in range(num_schools):
    start = school_addresses['New address'][i]
    start_city = school_cities['[city_name]'][i]
    print(i)
    for j in range(num_hospitals):
        end = hospital_addresses['Address'][j]
        end_city = hospital_cities['City'][j]
        page = requests.get("https://www.mapquest.com/directions/from/us/pennsylvania" 
                    + "/" + start_city + "/" + start + "/to/us/pa/" + 
                    end_city + "/" + end)
        try:
            page.raise_for_status()
        except:
            time.sleep(10)
            continue
        else:
            soup = BeautifulSoup(page.content, 'html.parser')
            narrative = soup.find(id="primaryPanel")
            distance_full = narrative.find_all('div', {'class': 'distance primary-only'})
            distance_strip= distance_full[0]
            distance_store= []
            for t in distance_strip:
                distance_store.append(t)
            distance = float(distance_store[0])
            full_distances[i][j] = distance

file = open('distances_store.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerows(full_distances)

#example coordinates 
#need zip code, don't need lat/long for it to work 


    
