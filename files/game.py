
import pygame

import clock
import sprite
import level

display = None

screen_size = (1024, 600)

def cleanup():
    pygame.quit()

def init():
    pygame.display.init()

    resize(screen_size)

    pygame.display.set_caption("biP")

    clock.init()

    sprite.load_sheet("tiles", "data/tilesheet.png")
    sprite.load_sheet("sprites", "data/spritesheet.png")

    while True:
        tick()

def resize(size):
    global display, screen_size

    screen_size = size

    display = pygame.display.set_mode(size, pygame.RESIZABLE)

    sprite.add_screen("game", (size[0] * 0.25, size[1] * 0.25))

def tick():
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.VIDEORESIZE:
            resize(event.size)
        elif event.type == pygame.KEYDOWN:
            if event.key == ord("q"): quit()

    sprite.get_screen("game").fill((100, 130, 160))

    level.render()

    screensprite = pygame.transform.scale(sprite.get_screen("game"), screen_size)
    display.blit(screensprite, (0, 0))

    pygame.display.flip()
