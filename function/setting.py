import pygame
from . import constants as ct

def init():
    pygame.init()
    pygame.display.set_mode(ct.SCREEN_SIZE)
    pygame.display.set_caption("PVZ")

