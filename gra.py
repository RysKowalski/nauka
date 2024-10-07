from random import randint
import yaml
import numpy as np
import time
from math import log2
import pygame
from vizualize import Object, create_box

def gra(screen, clock, key):
	
	# Get screen dimensions
	screen_width, screen_height = screen.get_size()

	def wyswietl(pytanie, odpowiedz):
		
		start = time.time()

		def button(self):
			print(self.data)
			return self.data
		
		# Adjust the coordinates based on screen size
		question_scale_width = int(screen_width * 0.35)
		question_scale_height = int(screen_height * 0.05)
		
		pytanie_vizualize = Object(
			texture=pytanie,
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.1),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', 40),
			text=pytanie,
			text_color=(0, 0, 0)
		)
		
		chances_vizualize = Object(
			texture = ',\\n'.join([f'{k}: {round(v, 2)}' for k, v in zip(dane[key]['names'], chances)]),
			x=int(screen_width * 0.1),
			y=int(screen_height * 0.5),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', 40),
			text = ',\\n'.join([f'{k}: {round(v, 2)}' for k, v in zip(dane[key]['names'], chances)]),
			text_color=(0, 0, 0)
		)

		punkty_vizualize = Object(
			texture=f'punkty: {punkty}',
			x=int(screen_width * 0.85),
			y=int(screen_height * 0.1),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', 40),
			text=str(punkty),
			text_color=(0, 0, 0)
		)

		max_punkty_vizualize = Object(
			texture=f'najwięcej punktów: {max_punkty}',
			x=int(screen_width * 0.85),
			y=int(screen_height * 0.2),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', 40),
			text=str(punkty),
			text_color=(0, 0, 0)
		)

		odpowiedz_vizualize = Object(
			texture=odpowiedz,
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.2),
			scale=[int(screen_width * 0.1), int(screen_height * 0.05)],
			angle=0,
			font=pygame.font.SysFont('Arial', 40),
			text=pytanie,
			text_color=(10, 200, 10)
		)
		
		done_button = [
			Object(
				texture=create_box(500, 50, (10, 200, 10)),
				x=int(screen_width * 0.5),
				y=int(screen_height * 0.85),
				scale=[int(screen_width * 0.5), int(screen_height * 0.05)],
				angle=0,
				code=button,
				data=True
			),
			Object(
				texture='Gotowe',
				x=int(screen_width * 0.5),
				y=int(screen_height * 0.85),
				scale=[int(screen_width * 0.5), int(screen_height * 0.05)],
				angle=0,
				font=pygame.font.SysFont('Arial', 40),
				text='Gotowe',
				text_color=(255, 0, 0)
			)
		]
		
		wyniki_buttons = [
			Object(    # przycisk 1
				texture=create_box(1, 1, (255, 0, 0)),
				x=int(screen_width * 0.25),
				y=int(screen_height * 0.85),
				scale=[int(screen_width * 0.2), int(screen_height * 0.05)],
				code=button,
				data=bool(False)
			),
			Object(    # przycisk 2
				texture=create_box(1, 1, (0, 255, 0)),
				x=int(screen_width * 0.75),
				y=int(screen_height * 0.85),
				scale=[int(screen_width * 0.2), int(screen_height * 0.05)],
				code=button,
				data=True
			),
			Object(    # tekst 1
				texture='źle',
				x=int(screen_width * 0.25),
				y=int(screen_height * 0.85),
				scale=[int(screen_width * 0.2), int(screen_height * 0.05)],
				font=pygame.font.SysFont('Arial', 40),
				text='źle',
				text_color=(255, 255, 255)
			),
			Object(    # tekst 2
				texture='dobrze',
				x=int(screen_width * 0.75),
				y=int(screen_height * 0.85),
				scale=[int(screen_width * 0.2), int(screen_height * 0.05)],
				font=pygame.font.SysFont('Arial', 40),
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
			y=int(screen_height * 0.05),
			scale=[question_scale_width, question_scale_height],
			angle=0,
			font=pygame.font.SysFont('Arial', 40),
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

			screen.fill((255, 245, 255))

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
			dane = yaml.safe_load(plik)
			max_punkty = int(dane[key]['punkty'])
			chances = dane[key]['chances']
			prawa = dane[key]['data']
			names = dane[key]['names']
		
		punkty = 0
		while True:
			weights = np.array(chances) / np.sum(chances)
			liczba = np.random.choice(range(0, len(weights)), p=weights)
			endtime, odpowiedz = wyswietl(names[liczba], prawa[liczba])
			
			if endtime / 10 > 1:
				chances[liczba] *= log2(endtime) - 2.7
			
			if not odpowiedz:
				chances[liczba] *= 1.7
				with open('prawa.yaml', 'w') as plik:
					chances = list(chances)
					if punkty > max_punkty:
						dane[key]['punkty'] = punkty
					yaml.safe_dump(dane, plik)
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
	
	gra(screen, clock, 'prawa')
