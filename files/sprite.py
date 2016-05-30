
import pygame

screens = {}
sheets = {}

def add_screen(name, size):
    screens[name] = pygame.Surface(size, flags = pygame.SRCALPHA)

def get_screen(name):
    return screens[name]

def load_sheet(name, path):
    sheets[name] = pygame.image.load(path)

def get_sprite(sheet, size, coord):

    sheetsurf = sheets[sheet]

    surf = pygame.Surface(size, flags = pygame.SRCALPHA)

    shift = (coord[0] * size[0], coord[1] * size[1], size[0], size[1])

    surf.blit(sheetsurf, (0, 0), shift)

    return surf
