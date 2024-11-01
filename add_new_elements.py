from komunikacja_api import save, load


dane: dict = load()

nazwa: str = input('podaj nazwe zbioru: ')

nazwy: list[str] = []
elementy: list[str] = []

while True:
    nowa_nazwa: str = input('podaj nazwę nowego elementu: ')
    nowe_dane: str = input(f'podaj dane do elementu {nowa_nazwa}: ')
    
    nazwy.append(nowa_nazwa)
    elementy.append(nowe_dane)
    
    if input('zakończyć dodawanie? y/N ') == 'y':
        break

chances: list[float] = [100 for _ in range(len(nazwy))]

dane[nazwa] = {'chances':chances, 'data':elementy, 'names':nazwy}


save(dane)