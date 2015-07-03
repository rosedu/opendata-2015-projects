import csv
import json


def number(txt):
    return float(txt.replace(',', ''))


def normalize_name(txt):
    return txt.lower().replace('-', ' ').replace('_', ' ')


data = {}
with open('data/siruta-judete.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        data[normalize_name(row['DENJ'])] = {
            'siruta': int(row['JUD']),
            'namee' : normalize_name(row['DENJ']).title(),
            'brev': row['MNEMONIC'],
            'values': [],
        }
with open('data/numar_decedati.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:

        val = number(row['2013'])+number(row['2012'])+number(row['2011'])+number(row['2010'])+number(row['2009'])+number(row['2008'])+number(row['2007'])+ number(row['2006'])+number(row['2005'])
        data[normalize_name(row['Jud'])]['values'].append(val)

series = []

for jud in data.values():
    series.append({
        'siruta': jud['siruta'],
        'namee' : jud['namee'],
        'brev' : jud['brev'],
        'value': int(sum(jud['values'])),
    })


out = {
    'series': series,
}


with open('parsed/maps.json', 'w') as f:
    json.dump(out, f, indent=2)
