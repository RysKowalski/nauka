import requests
import json

debug = False

if debug:
	url = 'http://localhost:3000/api'
else:
	url = 'https://stronadlabogatych.website/api'

def save(dane: dict) -> None:

	# Wysyłanie danych jako JSON
	response = requests.post(url, json=dane)  # Użyj argumentu `json`, aby automatycznie ustawić nagłówek

	# Sprawdzenie odpowiedzi
	if response.status_code == 200:
		print("Dane zostały zapisane:", response.text)
	else:
		print("Błąd zapisu danych YAML:", response.text)

def load() -> dict:
	response = requests.get(url)

	if response.status_code == 200:
		return json.loads(response.text)

	else:
		raise RuntimeError('błąd pobierania pliku:', response.text)

if __name__ == '__main__':
	url = 'http://localhost:3000/api'

	import yaml
	with open('prawa.yaml', 'r') as plik:
		save(yaml.safe_load(plik))
	print(load())
