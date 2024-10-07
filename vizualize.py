import pygame
from typing import Union, Callable

def create_box(width, height, color):
	surface = pygame.Surface((width, height))
	surface.fill((color))
	return surface


def nothing(*t):
	pass

class Object:
	def __init__(self,
				 texture: Union[pygame.Surface, str],
				 x: float = 0,
				 y: float = 0,
				 scale: list[float] = [1, 1],
				 angle: float = 0,
				 code: Callable[..., any] = nothing,
				 font: pygame.font.Font = None,
				 text: str = None,
				 text_color: tuple[int] = (255, 255, 255),
				 data: dict = None):
		"""
		inputs x=float, y=float, texture=pygame_texture or str, scale=[int, int], angle=int, code=function, font=pygame_font, text=str, text_color=tuple
		"""

		def nothing(*t):
			pass

		self.x = x
		self.y = y
		self.texture = texture
		self.scale = scale
		self.angle = angle
		self.code = code  # Dynamicznie przypisywana funkcja
		self.font = font  # Font Pygame (opcjonalny)
		self.text = text  # Tekst do wyświetlenia (opcjonalny)
		self.text_color = text_color  # Kolor tekstu
		self.data = data

		if isinstance(texture, str) and self.font is not None:  # Jeśli tekstura to tekst
			self.image = self._render_text(texture)
		else:
			self.image = pygame.transform.scale(texture, scale)

		self.rect = self.image.get_rect(center=(x, y))
	def _render_text(self, text: str) -> pygame.Surface:
		""" Renderuje tekst z obsługą wielowierszowego tekstu. """
		if not self.font:
			return None

		lines = text.split('\\n')  # Podział tekstu na linie na podstawie \n
		line_surfaces = [self.font.render(line, True, self.text_color) for line in lines]

		# Obliczenie łącznej wysokości bloku tekstu oraz maksymalnej szerokości
		total_height = sum(line.get_height() for line in line_surfaces)
		max_width = max(line.get_width() for line in line_surfaces)

		# Tworzymy nową powierzchnię do wyświetlenia całego tekstu
		surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)

		# Wyśrodkowanie pionowe - obliczamy przesunięcie, aby tekst był wyśrodkowany względem środka obiektu
		y_offset = 0
		for line_surface in line_surfaces:
			# Wyśrodkowanie poziome każdej linii na powierzchni
			surface.blit(line_surface, ((max_width - line_surface.get_width()) // 2, y_offset))
			y_offset += line_surface.get_height()

		return surface

	def draw(self, surface):
		# Rotacja obrazu
		rotated_image = pygame.transform.rotate(self.image, self.angle)
		rotated_rect = rotated_image.get_rect(center=self.rect.center)
		surface.blit(rotated_image, rotated_rect.topleft)

	def update(self, x=None, y=None, texture=None, scale=None, angle=None, code=None, font=None, text=None, text_color=None, data=None):
		if x is not None:
			self.x = x
		if y is not None:
			self.y = y

		if texture is not None:
			self.texture = texture
			if isinstance(texture, str) and self.font is not None:
				self.image = self._render_text(texture)
			else:
				self.image = pygame.transform.scale(self.texture, self.scale)
		if scale is not None:
			self.scale = scale
			self.image = pygame.transform.scale(self.texture, self.scale)
		if angle is not None:
			self.angle = angle
		if font is not None:
			self.font = font
		if text is not None:
			self.text = text
		if text_color is not None:
			self.text_color = text_color
		if data is not None:
			self.data = data

		# Aktualizacja pozycji prostokąta
		self.rect.center = (self.x, self.y)

	def get_settings(self):
		return {
			"x": self.x,
			"y": self.y,
			"texture": self.texture,
			"scale": self.scale,
			"angle": self.angle,
			"code": self.code,
			"data": self.data
		}

	def interact(self, coords, *args, **kwargs):
		click_x, click_y = coords

		# Obliczenie obróconego obrazu
		rotated_image = pygame.transform.rotate(self.image, self.angle)
		rotated_rect = rotated_image.get_rect(center=self.rect.center)

		# Sprawdzenie, czy kliknięto wewnątrz obróconego prostokąta
		if rotated_rect.collidepoint((click_x, click_y)):
			if args:
				ret = self.code(self, *args, **kwargs)  # Przekazanie samego obiektu do funkcji

				if ret is not None:
					return ret
			else:
				ret = self.code(self)
				if ret is not None:
					return ret