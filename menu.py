import yaml
import pygame
from vizualize import Object
	
def menu(screen, clock):
		
	
	def wybierz_element(self):
		# Zwracanie konkretnego elementu
		print(self.data['element'])
		return self.data['element']
	
	texts = []
	objects = []
	
	with open('prawa.yaml', 'r') as plik:
		keys = list(yaml.safe_load(plik).keys())
	
	key = ''
	
	
	font = pygame.font.SysFont('Arial', 40)
	for i, key in enumerate(keys):
		# Tworzenie obiektu tekstowego
		objects.append(Object(x=400, y=i * 100 + 50, texture=key, scale=[10, 10], font=font, text_color=(100, 100, 100)))
	
		# Tworzenie prostokąta z kolorem na powierzchni
		surface = pygame.Surface((40, 40))  # Utwórz powierzchnię o wymiarach 40x40
		surface.fill((255, 0, 0))  # Wypełnij powierzchnię kolorem czerwonym
		
		data = {'element': key}
		# Dodanie obiektu z powierzchnią
		objects.append(Object(x=150, y=i * 100 + 50, texture=surface, scale=[80, 80], code=wybierz_element, data=data))
	
	
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					for obj in objects:
						s = obj.interact((event.pos[0], event.pos[1]))
						if isinstance(s, str):  # Poprawne sprawdzenie, czy wynik jest stringiem
							key = s
							running = False
							return key
		
		screen.fill((255, 245, 255))
		for obj in objects:
			obj.draw(screen)
		
		clock.tick(60)
		pygame.display.flip()


if __name__ == '__main__':
	pygame.init()

	display_info = pygame.display.Info()
	screen_width, screen_height = display_info.current_w, display_info.current_h
	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	menu(screen, clock)