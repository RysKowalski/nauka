import yaml
import pygame
from vizualize import Object, create_box
	
def menu(screen, clock):

	def wybierz_element(self: Object):
		self.data['clicked'] = not self.data['clicked']
		
		if self.data['clicked']:
			self.update(texture=self.data['textures']['clicked'])
		else:
			self.update(texture=self.data['textures']['not_clicked'])
	
	def button(self: Object, objects: list[Object]):
		chosen_keys = []

		for obj in objects:
			if obj.data['clicked']:
				chosen_keys.append(obj.data['element'])
		
		return chosen_keys


	def adjust_for_orientation(screen_width, screen_height):
		# If the screen is taller than it is wide (portrait mode)
		if screen_height > screen_width:
			scale_factor = screen_width / screen_height  # Scale relative to width
		else:
			scale_factor = screen_height / screen_width  # Scale relative to height
		return scale_factor * 2  # Increase all elements' size by 2 times

	# Get the scaling factor for the screen
	scale_factor = adjust_for_orientation(screen_width, screen_height)


	objects = []
	texts = []

	with open('prawa.yaml', 'r') as plik:
		keys = list(yaml.safe_load(plik).keys())
	
	key = ''
	
	
	font = pygame.font.SysFont('Arial', 40)
	for i, key in enumerate(keys):
		# Tworzenie obiektu tekstowego
		texts.append(Object(x=400, y=i * 100 + 50, texture=key, scale=[10, 10], font=font, text_color=(100, 100, 100)))
	
		# Tworzenie prostokąta z kolorem na powierzchni
		surface = pygame.Surface((40, 40))  # Utwórz powierzchnię o wymiarach 40x40
		surface.fill((255, 0, 0))  # Wypełnij powierzchnię kolorem czerwonym
		
		data = {'element': key, 'textures': {'not_clicked': surface, 'clicked': pygame.image.load('.\\assets\\wybrane.png')}, 'clicked': False}
		# Dodanie obiektu z powierzchnią
		objects.append(Object(x=150, y=i * 100 + 50, texture=surface, scale=[80, 80], code=wybierz_element, data=data))
	
	gotowe = [
		Object(
			texture=create_box(500, 50, (10, 200, 10)),
			x=int(screen_width * 0.5),
			y=int(screen_height * 0.95),
			scale=[int(screen_width * 0.5 * scale_factor), int(screen_height * 0.05 * scale_factor)],
			angle=0,
			code=button
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

	
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pos = (event.pos[0], event.pos[1])
					for obj in objects:
						s = obj.interact(pos)
						if isinstance(s, str):  # Poprawne sprawdzenie, czy wynik jest stringiem
							key = s
							running = False
							return key

					chosen_keys = gotowe[0].interact(pos, objects)
					if isinstance(chosen_keys, list):
						if len(chosen_keys) >= 1:
							print(chosen_keys)
							return chosen_keys

		screen.fill((225, 225, 255))
		for obj in objects:
			obj.draw(screen)

		for obj in texts:
			obj.draw(screen)

		for obj in gotowe:
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