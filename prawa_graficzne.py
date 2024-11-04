import pygame

from menu import menu
from gra import gra

pygame.init()

display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

key = menu(screen, clock)

gra(screen, clock, key)