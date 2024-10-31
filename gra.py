import yaml
import numpy as np
import time
from math import log2
import pygame
from vizualize import Object, create_box
from dict_format import add_new_keys, divide_list

def gra(screen: pygame.display, clock: pygame.time.Clock, keys: list[str]):



	# Get screen dimensions
	screen_width, screen_height = screen.get_size()

	# Adjust scale and positions based on screen orientation
	def adjust_for_orientation(screen_width, screen_height):
		# If the screen is taller than it is wide (portrait mode)
		if screen_height > screen_width:
			scale_factor = screen_width / screen_height  # Scale relative to width
		else:
			scale_factor = screen_height / screen_width  # Scale relative to height
		return scale_factor * 2  # Increase all elements' size by 2 times


	# Get the scaling factor for the screen
	scale_factor = adjust_for_orientation(screen_width, screen_height)

	# Adjusted scaling for question and answer display (multiplied by 2)
	question_scale_width = int(screen_width * 0.35 * scale_factor)
	question_scale_height = int(screen_height * 0.05 * scale_factor)

	# Ensure nothing goes beyond the screen in portrait mode
	if screen_height > screen_width:
		question_scale_height = min(question_scale_height, screen_height * 0.1)  # Limit height in portrait mode
		question_scale_width = min(question_scale_width, screen_width * 0.9)	 # Limit width in portrait mode

	def wyswietl(pytanie, odpowiedz):

		start = time.time()

		def button(self: Object):
			print(self.data)
			return self.data

		# Adjust the coordinates and scale based on screen size and orientation
		question_scale_width = int(screen_width * 0.35 * scale_factor)
		question_scale_height = int(screen_height * 0.05 * scale_factor)

		pytanie_vizualize = Object(
			texture=pytanie,
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.2),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
			text=pytanie,
			text_color=(0, 0, 0)
		)

		chances_text = ',\\n'.join(
			[f'{k}: {round(v, 2)}' for key in keys for k, v in zip(dane[key]['names'], chances)]
		)

		chances_vizualize = Object(
			texture=chances_text,
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.6),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
			text=chances_text,
			text_color=(0, 0, 0)
		)


		punkty_vizualize = Object(
			texture=f'punkty: {punkty}',
			x=int(screen_width * 0.25 - question_scale_width / 2),
			x=int(screen_width * 0.25 - question_scale_width / 2),
			y=int(screen_height * 0.16),
			scale=[question_scale_width / question_scale_width, question_scale_height],
			scale=[question_scale_width / question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
			text=str(punkty),
			text_color=(0, 0, 0)
		)

		max_punkty_vizualize = Object(
			texture=f'najwięcej punktów: {max_punkty}',
			x=int(screen_width * 0.29 - question_scale_width / 2),
			x=int(screen_width * 0.29 - question_scale_width / 2),
			y=int(screen_height * 0.35),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
			text=str(max_punkty),
			text_color=(0, 0, 0)
		)

		odpowiedz_vizualize = Object(
			texture=odpowiedz,
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.3),
			scale=[int(screen_width * 0.1 * scale_factor), int(screen_height * 0.05 * scale_factor)],
			angle=0,
			font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
			text=odpowiedz,
			text_color=(10, 200, 10)
		)

		done_button = [
			Object(
				texture=create_box(500, 50, (10, 200, 10)),
				x=int(screen_width * 0.5),
				y=int(screen_height * 0.95),
				scale=[int(screen_width * 0.5 * scale_factor), int(screen_height * 0.05 * scale_factor)],
				angle=0,
				code=button,
				data=True
			),
			Object(
				texture='Gotowe',
				x=int(screen_width * 0.5),
				y=int(screen_height * 0.95),
				scale=[int(screen_width * 0.5 * scale_factor), int(screen_height * 0.05 * scale_factor)],
				angle=0,
				font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
				text='Gotowe',
				text_color=(255, 0, 0)
			)
		]

		wyniki_buttons = [
			Object(	# przycisk 1
				texture=create_box(1, 1, (255, 0, 0)),
				x=int(screen_width * 0.25),
				y=int(screen_height * 0.95),
				scale=[int(screen_width * 0.2 * scale_factor), int(screen_height * 0.05 * scale_factor)],
				code=button,
				data=bool(False)
			),
			Object(	# przycisk 2
				texture=create_box(1, 1, (0, 255, 0)),
				x=int(screen_width * 0.75),
				y=int(screen_height * 0.95),
				scale=[int(screen_width * 0.2 * scale_factor), int(screen_height * 0.05 * scale_factor)],
				code=button,
				data=True
			),
			Object(	# tekst 1
				texture='źle',
				x=int(screen_width * 0.25),
				y=int(screen_height * 0.95),
				scale=[int(screen_width * 0.2 * scale_factor), int(screen_height * 0.05 * scale_factor)],
				font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
				text='źle',
				text_color=(255, 255, 255)
			),
			Object(	# tekst 2
				texture='dobrze',
				x=int(screen_width * 0.75),
				y=int(screen_height * 0.95),
				scale=[int(screen_width * 0.2 * scale_factor), int(screen_height * 0.05 * scale_factor)],
				font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
				text='dobrze',
				text_color=(255, 255, 255)
			)
		]

		# Zmienna start z czasem rozpoczęcia pytania
		start = time.time()

		# Tworzenie obiektu licznika (raz, przed pętlą)
		licznik = Object(
			texture=f'czas: {round(0, 1)}s',  # Początkowy czas to 0 sekund
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.015),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', int(40 * scale_factor)),
			text=f'czas: {round(0, 1)}s',  # Początkowy tekst licznika
			text_color=(0, 0, 0)  # Początkowy kolor: czarny
		)

		done = False
		odpowiedz = False

		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						pos = event.pos[0], event.pos[1]
						if not done:
							wynik = done_button[0].interact(pos)
							if isinstance(wynik, bool):
								done = wynik
						else:
							for przycisk in wyniki_buttons:
								wynik = przycisk.interact(pos)
								if isinstance(wynik, bool):
									odpowiedz = wynik
									endtime = time.time() - start
									running = False

			# Obliczanie upływu czasu
			current_time = time.time() - start
			licznik_text_color = (0, 0, 0)  # Domyślny kolor (czarny)

			# Jeśli czas przekroczy 10 sekund, zmień kolor na czerwony
			if current_time > 10:
				licznik_text_color = (255, 0, 0)

			# Aktualizuj licznik co klatkę za pomocą funkcji update
			licznik.update(
				texture=f'czas: {round(current_time, 1)}s',  # Aktualizowanie tekstu
				text=f'czas: {round(current_time, 1)}s',
				text_color=licznik_text_color  # Zmieniony kolor, jeśli ponad 10 sekund
			)

			screen.fill((225, 225, 255))

			# Rysowanie elementów na ekranie
			pytanie_vizualize.draw(screen)
			punkty_vizualize.draw(screen)
			max_punkty_vizualize.draw(screen)
			chances_vizualize.draw(screen)
			licznik.draw(screen)  # Rysowanie zaktualizowanego licznika

			if done:
				odpowiedz_vizualize.draw(screen)
				for object in wyniki_buttons:
					object.draw(screen)

			if not done:
				for object in done_button:
					object.draw(screen)

			clock.tick(60)
			pygame.display.flip()

		return current_time, odpowiedz


	while True:
		with open('prawa.yaml', 'r') as plik:
			dane: dict = yaml.safe_load(plik)

			dane = add_new_keys(keys, dane)

			dane = add_new_keys(keys, dane)

			current_dict = dane['points']

			for key in keys:
				current_dict = current_dict[key]  

			max_punkty: int = int(current_dict['max_points'])
			punkty: int = int(current_dict['points'])

			print(f"Max punkty: {max_punkty}, Punkty: {punkty}")

			chances: list[float] = []
			prawa: list[str] = []
			names: list[str] = []

			for key in keys:
				chances += dane[key]['chances']
				prawa += dane[key]['data']
				names += dane[key]['names']


		punkty = 0
		while True:
			weights = np.array(chances) / np.sum(chances)
			liczba = np.random.choice(range(0, len(weights)), p=weights)
			endtime, odpowiedz = wyswietl(names[liczba], prawa[liczba])

			if endtime / 10 > 1:
				chances[liczba] *= log2(endtime) - 2.7

			if not odpowiedz:
				chances[liczba] *= 1.7

				# Nowe wartości punktów
				nowe_punkty = punkty

				# Przechodzimy przez klucze, aby dotrzeć do odpowiedniego miejsca w danych
				current_dict = dane['points']  # Zakładamy, że zaczynamy od klucza 'points'
				
				for key in keys[:-1]:  # Przechodzimy przez wszystkie klucze oprócz ostatniego
					if key in current_dict:
						current_dict = current_dict[key]
					else:
						raise KeyError(f"Key {key} not found in the data")

				# Ostatni klucz - tam, gdzie chcemy zmienić wartość punktów
				ostatni_klucz = keys[-1]

				if isinstance(current_dict.get(ostatni_klucz), dict):
					# Zmieniamy wartość punktów, jeśli są większe niż max_points
					if nowe_punkty > current_dict[ostatni_klucz]['max_points']:
						current_dict[ostatni_klucz]['max_points'] = nowe_punkty
				else:
					raise TypeError(f"Expected dict at {ostatni_klucz}, but got {type(current_dict[ostatni_klucz])}")
				
				# Zapisujemy zmodyfikowane dane z powrotem do pliku YAML
				with open('prawa.yaml', 'w') as plik:

					lenghts: list[int] = []
					for key in keys:
						lenghts.append(len(dane[key]['chances']))
					


					new_chances: list[list] = divide_list(lenghts, chances)

					for i, key in enumerate(keys):
						dane[key]['chances'] = new_chances[i]

					yaml.safe_dump(dane, plik, sort_keys=True)

				break


			else:
				punkty += 1
				if punkty > max_punkty:
					max_punkty = punkty
				chances[liczba] /= 1.2
			print(punkty)


if __name__ == '__main__':
	pygame.init()
	
	# Automatically set the screen resolution to the user's display size
	display_info = pygame.display.Info()
	screen_width, screen_height = display_info.current_w, display_info.current_h
	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	gra(screen, clock, ['prawa', 'sznury_choragwia'])