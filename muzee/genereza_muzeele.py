#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json
import sys
import io
import shutil
import codecs
from geopy import geocoders
import csv
import time
g_api_key = 'AIzaSyB_djldgwM0HGAg7opZpVx5StLQB1KDkQc'

g = geocoders.GoogleV3(g_api_key)


h = open("not_working.txt", "w")
data = {}
number = 0
with open('muzee.csv') as f:
    reader = csv.DictReader(f, delimiter='|')
    for row in reader:
    	if len(row['adresa']) > 8:
            adresa_noua = row['localitatea'] + " , " + row['adresa'] 
            print(int(row['identificatorul înregistrării']))
            try:
                andresa, (lat, lng) = g.geocode(adresa_noua, exactly_one=True)
            #    print(int(row['identificatorul înregistrării']))
                if andresa and lat and lng:
                    data [row['identificatorul înregistrării']] = {
            			'identificator': int(row['identificatorul înregistrării']),
            			'judetul': row['județul'],
            			'denumirea': row['denumirea (română)'], 
            			'localitatea': row['localitatea'],
            			'adresa': row['adresa'],
            			'codul postal': row['codul poștal'],
            			'telefon': row['telefon'], 
            			'descrierea': row['descrierea (română)'],
            			'latitudine': lat,
            			'longitudine': lng,
            			'coordonatele': (lat, lng),
            		}
                time.sleep(0.5)
            except:
                h.write(str(row['identificatorul înregistrării'])+ "\n")
        		#print(row['adresa'])
    		#number += 1

print(number)



with codecs.open('lista_muzeelor.json', mode = 'w', encoding = 'utf-8') as f:
    json.dump(data, f, indent=2)
