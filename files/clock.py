
import pygame

clock = None

target_fps = 60

run_time = 0
last_tick = 0
delta = 1.0 / target_fps
fps = target_fps # placeholder that isn't 0

def init():
    global clock

    clock = pygame.time.Clock()

def tick():
    global run_time, last_tick, delta, fps

    clock.tick(target_fps)
    fps = clock.get_fps()

    thistick = pygame.time.get_ticks()

    delta = (last_tick - thistick) / 1000.0
    last_tick = thistick

    run_time = thistick / 1000.0
