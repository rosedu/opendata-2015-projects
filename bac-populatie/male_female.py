import csv
import json

def exist(word,dicti):
  for w in dicti:
    if w==word:
      return True
  return False

def number(txt):
   return float(txt.replace(',', '.'))
dicti = {}
dictiM = {}
dictiF = {}
dictiNumF= {}
dictiNumM= {}
dictiNum= {}

with open('rawdata/Bac_sesiune1_1.csv') as stream:
  reader = csv.DictReader(stream , delimiter='\t')
  for row in reader:
    if row['Sex']=='F':
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
    if row['Sex']=='M':
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
  dicti[key]=dictiF[key]+dictiM[key]
  dictiNum[key]=dictiNumF[key]+dictiNumM[key]
  dicti[key]/=dictiNum[key]

for key in dictiF:
  dictiF[key]/=dictiNumF[key]
for key in dictiM:
  dictiM[key]/=dictiNumM[key]

def dict_to_list(dicti):
  lista=[]
  for key in dicti.values():
    lista.append(round(key,2))
  return lista

#import pdb; pdb.set_trace()

out = {
  'series': [
       { 
         'name':'Total', 
         'type':'column',
         'yAxis': 1, 
         'data': dict_to_list(dicti)
       },
       { 
         'name':'Male',
         'type':'spline',
         'yAxis': 1, 
         'data': dict_to_list(dictiM)
       },
       { 
         'name':'Female', 
         'type':'spline',
         'yAxis': 1, 
         'data': dict_to_list(dictiF)
       }
       
      ],
   }

with open('data/male_female.json', 'w') as f:
   json.dump(out, f, indent=2)
      
      
