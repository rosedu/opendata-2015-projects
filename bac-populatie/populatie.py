import csv
import json
import random
from collections import defaultdict

def exist(word,dicti):
  for w in dicti:
    if w==word:
      return True
  return False

def numar(nr):
  return int(nr.replace(',',''))

populatie = {}
judete={}

with open('rawdata/populatie_2.csv') as stream:
  reader = csv.DictReader(stream)

  for i, row in enumerate(reader):
    #if i >= 300: break
    if row['Tip localitate']!='COMUNA':
      if exist(row['Denumire Judet'],judete)==True:
         judete[row['Denumire Judet']].update({ row['Localitate']: {'Populatie': str(numar(row['Numar Locuitori']))}})
      else:
         judete[row['Denumire Judet']]={ row['Localitate']: {'Populatie': str(numar(row['Numar Locuitori']))}}



serii=[]

import pdb; pdb.set_trace()


out = {
     'series': judete
 }
    
with open('data/populatie.json', 'w') as f:
   json.dump(out, f, indent=2)
