import csv
import json

def number(txt):
    return float(txt.replace(',', ''))


def normalize_name(txt):
    return txt.lower().replace('-', ' ').replace('_', ' ')

data = {}
nr = 0
with open('data/numar_decedati.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nr += 1
        data[normalize_name(row['Jud']).title()] = [ float(row['2005']) , float(row['2006']) , float(row['2007']) , float(row['2008']) , float(row['2009']) , float(row['2010']) ,float(row['2011']) , float(row['2012']) , float(row['2013']) ]

out = {'series' : []}
with open('data/siruta-judete.csv') as f:
    reader = csv.DictReader(f , delimiter = ';')
    for row in reader:

        j = {'name' : '' , 'data': [] , 'siruta': ''}
        j['data'] = data[normalize_name(row['DENJ']).title()]
        j['name'] = normalize_name(row['DENJ']).title()
        j['siruta'] = row ['JUD'] 

        out['series'].append(j)

with open('parsed/nr_decedati.json', 'w') as f:
    json.dump(out , f, indent=2)
       
data = {}
nr = 0
with open('data/numar_decedati_1000.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nr += 1
        data[normalize_name(row['Jud']).title()] = [ float(row['2005']) , float(row['2006']) , float(row['2007']) , float(row['2008']) , float(row['2009']) , float(row['2010']) ,float(row['2011']) , float(row['2012']) , float(row['2013']) ]


out = {'series' : []}
with open('data/siruta-judete.csv') as f:
    reader = csv.DictReader(f , delimiter = ';')
    for row in reader:

        j = {'name' : '' , 'data': [] , 'siruta': ''}
        j['data'] = data[normalize_name(row['DENJ']).title()]
        j['name'] = normalize_name(row['DENJ']).title()
        j['siruta'] = row ['JUD'] 

        out['series'].append(j)

with open('parsed/nr_decedati_1000.json', 'w') as f:
    json.dump(out , f, indent=2)
        
