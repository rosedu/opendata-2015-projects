import csv
import json


def number(txt):
    return float(txt.replace(',', ''))


def normalize_name(txt):
    return txt.lower().replace('-', ' ').replace('_', ' ')


def parse_demografic(filename):
    data_judete = {} # Dictionar de dictionare
    with open(filename, 'r') as fi:
        reader = csv.DictReader(fi)
        for row in reader:
            j = row['Judetul']
            data_ani = {}
            for i in range(1989, 2014):
                if str(i) in row:
                    data_ani[str(i)] = float(row[str(i)])
                else:
                    data_ani[str(i)] = 0
            data_judete[j] = data_ani
    return data_judete

def dump_json(data_judete, filename):
    with open(filename, 'w') as fo:
        json.dump(data_judete, fo, indent=4)
    return

def unify_by_year(df, dm, popj, somajf, somajm):
    data_ani = {}
    for i in range(1989, 2014):
        data_judet = {}
        for j in df:
            data_judet_an = {}
            ii = str(i)
            data_judet_an['df'] = df[j][ii]
            data_judet_an['dm'] = dm[j][ii]
            data_judet_an['popj'] = popj[j][ii]
            data_judet_an['somajf'] = somajf[j][ii]
            data_judet_an['somajm'] = somajm[j][ii]
            data_judet[j] = data_judet_an
        data_ani['an'+str(i)] = data_judet
        # data_ani['1989']['Teleorman']['df']
    return data_ani

def convert(d):
    # ['nume'], ['an....']['df'] etc.
    lista_headere = ['df', 'dm', 'popj', 'somajf', 'somajm']
    dd = {}
    lista_judete = []
    for an in d['an2000']:
        lista_judete.append(an)
    dd['nume'] = lista_judete
    for an in d:
        dd[an] = {}
        for header in lista_headere:
            dd[an][header] = []
    for an in d:
        for judet in d[an]:
            for header in lista_headere:
                dd[an][header].append(d[an][judet][header])
    return dd

if __name__ == '__main__':
    df = parse_demografic('durata-viata-f.csv')
    dm = parse_demografic('durata-viata-m.csv')
    popj = parse_demografic('populatia-pe-judete.csv')
    somajf = parse_demografic('rata-somaj-f.csv')
    somajm = parse_demografic('rata-somaj-m.csv')
    d = unify_by_year(df, dm, popj, somajf, somajm)
    d2 = convert(d)

    #dump_json(df, 'durata-viata-f.json')
    #dump_json(dm, 'durata-viata-m.json')
    #dump_json(popj, 'populatia-pe-judete.json')
    #dump_json(somajf, 'rata-somaj-f.json')
    #dump_json(somajm, 'rata-somaj-m.json')
    #dump_json(d, 'master.json')
    dump_json(d2, 'master2.json')