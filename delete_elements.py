from komunikacja_api import save, load


while True:
	dane: dict = load()
	keys: list[str] = list(dane.keys())
	keys.remove('points')

	print(keys)

	nazwa: str = input('podaj nazwę do usunięcia: ')
	dane.pop(nazwa)

	save(dane)

	if input('zakończyć usuwanie? y/N ') == 'y':
		break