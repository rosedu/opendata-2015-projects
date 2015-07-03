import csv
import json
import datetime 

def number(txt):
    return float(txt.replace(',', ''))

dictionar = {} # dictionar de dictionare

def normalize_name(txt):
    return txt.lower().replace('-', ' ').replace('_', ' ')

    
files = ['cheltuiele_medicamente_per_pat' ,     'cheltuieli_per_pat' ,
'cheltuieli_medicamente_per_bolnav' , 'cheltuieli_zi_spitalizare',
'cheltuieli_medicamente_per_zi' ,  'cheltuieli_per_bolnav' ]          
 

for filename in files : 

    with open("data/"+filename+".csv") as f:
            reader = csv.DictReader(f)
           
            for row in reader:
                d = []
                d.append(float(row['2005']))
                d.append(float(row['2006']))
                d.append(float(row['2007']))
                d.append(float(row['2008']))
                d.append(float(row['2009']))
                d.append(float(row['2010']))
                d.append(float(row['2011']))
                d.append(float(row['2012']))
                d.append(float(row['2013']))
                dictionar[normalize_name(row['Jud']).title()] = d

    lista = []
    with open('data/siruta-judete.csv') as f:
        reader = csv.DictReader(f , delimiter = ';')
        for row in reader:
            temp = {}
            temp['data'] = dictionar[normalize_name(row['DENJ']).title()]
            temp['name'] = normalize_name(row['DENJ']).title()
            temp['siruta'] = row ['JUD']
            lista.append(temp)
    out = {
        'series': lista
    }
    with open("parsed/"+filename+".json", 'w') as f:
        json.dump(out, f, indent=2)    
    

                

