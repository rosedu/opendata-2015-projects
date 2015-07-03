import csv
import json

def exist(word,dicti):
  for w in dicti:
    if w==word:
      return True
  return False

def number(txt):
   return float(txt.replace(',', '.'))
dictiM = {}  #RURAL
dictiF = {}  #URBAN
dictiNumF= {}
dictiNumM= {}

with open('rawdata/Bac_sesiune1_1.csv') as stream:
  reader = csv.DictReader(stream , delimiter='\t')
  for row in reader:
    if row['Mediu candidat']=='URBAN':
      if row['STATUS_EA']!='Absent':    
        if exist(row['Subiect ea'],dictiF)==True:
          dictiF[row['Subiect ea']]+=number(row['NOTA_EA'])	  
          dictiNumF[row['Subiect ea']]+=1
        else:
          dictiF[row['Subiect ea']]=number(row['NOTA_EA'])
          dictiNumF[row['Subiect ea']]=1
      if row['STATUS_EC']!='Absent':
        if exist(row['Subiect ec'],dictiF)==True:
          dictiF[row['Subiect ec']]+=number(row['NOTA_EC'])
          dictiNumF[row['Subiect ec']]+=1
        else:
          dictiF[row['Subiect ec']]=number(row['NOTA_EC'])
          dictiNumF[row['Subiect ec']]=1
      if row['STATUS_ED']!='Absent':
        if exist(row['Subiect ed'],dictiF)==True:
          dictiF[row['Subiect ed']]+=number(row['NOTA_ED'])
          dictiNumF[row['Subiect ed']]+=1
        else:
          dictiF[row['Subiect ed']]=number(row['NOTA_ED'])
          dictiNumF[row['Subiect ed']]=1
    if row['Mediu candidat']=='RURAL':
      if row['STATUS_EA']!='Absent':
        if exist(row['Subiect ea'],dictiM)==True:
          dictiM[row['Subiect ea']]+=number(row['NOTA_EA'])
          dictiNumM[row['Subiect ea']]+=1
        else:
          dictiM[row['Subiect ea']]=number(row['NOTA_EA'])
          dictiNumM[row['Subiect ea']]=1
      if row['STATUS_EA']!='Absent':
        if exist(row['Subiect ec'],dictiM)==True:
          dictiM[row['Subiect ec']]+=number(row['NOTA_EC'])
          dictiNumM[row['Subiect ec']]+=1
        else:
          dictiM[row['Subiect ec']]=number(row['NOTA_EC'])
          dictiNumM[row['Subiect ec']]=1
      if row['STATUS_EA']!='Absent':
        if exist(row['Subiect ed'],dictiM)==True:
          dictiM[row['Subiect ed']]+=number(row['NOTA_ED'])
          dictiNumM[row['Subiect ed']]+=1
        else:
          dictiM[row['Subiect ed']]=number(row['NOTA_ED'])
          dictiNumM[row['Subiect ed']]=1


for key in dictiF:
  dictiF[key]/=dictiNumF[key]
for key in dictiM:
  dictiM[key]/=dictiNumM[key]

import collections

def sortare(f,dicti):
  return [f*dicti[key] for key in sorted(dicti)]

for key in dictiF:
  if exist(key,dictiM)==False:
    dictiM[key]=0

for key in dictiM:
  if exist(key,dictiF)==False:
    dictiF[key]=0


#import pdb; pdb.set_trace()

out = {
  'series': [
       { 
         'name':'Urban',
         'data': sortare(-1,dictiF)
       },
       { 
         'name':'Rural', 
         'data': sortare(1,dictiM)
       }
       
      ],
   }

with open('data/urban_rural.json', 'w') as f:
   json.dump(out, f, indent=2)
      
      
