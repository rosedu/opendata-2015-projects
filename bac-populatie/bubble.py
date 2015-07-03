import csv
import json
import random

def exist(word,dicti):
  for w in dicti:
    if w==word:
      return True
  return False

populatie = {}
suprafata = {}


with open('rawdata/populatie_2.csv') as stream:
  reader = csv.DictReader(stream)
  #import pdb; pdb.set_trace()
  for row in reader:
    if exist(row['Denumire Judet'],populatie)==True:
      populatie[row['Denumire Judet']]+=int(row['Numar Locuitori'].replace(',',''))
      suprafata[row['Denumire Judet']]+=int(row['Suprafata'].replace(',',''))
    else:
      populatie[row['Denumire Judet']]=int(row['Numar Locuitori'].replace(',',''))
      suprafata[row['Denumire Judet']]=int(row['Suprafata'].replace(',',''))      

import pdb; pdb.set_trace()
serii=[]
for key in populatie:
  x=populatie[key]
  y=suprafata[key]
  serii.append({'name':key,'data':[[ x , y , x/y ]] })

out = {
     'series': serii
 }
    
with open('data/bubble.json', 'w') as f:
   json.dump(out, f, indent=2)

#================================================

