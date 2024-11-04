import yaml
from komunikacja_api import save, load


dane: dict = load()

klucze: list = list(dane.keys())
klucze.remove('points')


for klucz in klucze:
	for i in range(len(dane[klucz]['chances'])):
		dane[klucz]['chances'][i] = 100.0

save(dane)