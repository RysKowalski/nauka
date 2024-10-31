import yaml

with open('prawa.yaml', 'r') as plik:
	dane: dict = yaml.safe_load(plik)

klucze: list = list(dane.keys())
klucze.remove('points')


for klucz in klucze:
	for i in range(len(dane[klucz]['chances'])):
		dane[klucz]['chances'][i] = 100.0

with open('prawa.yaml', 'w') as plik:
	yaml.safe_dump(dane, plik)