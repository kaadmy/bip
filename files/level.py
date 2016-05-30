
import pygame

import sprite

# transforms
R90  = 1<<0 # counter-clockwise!
R180 = 1<<1 # counter-clockwise!
R270 = 1<<2 # counter-clockwise!
FX   = 1<<3
FY   = 1<<4
FXY  = 1<<5

floormask = [
    [(0,11),(0,11),(0,11),(0,11),(0,11),(0,11),(0,11),(0,13)],
    [(0,2),(0,10),(0,4),(0,4),(0,4),(0,4),(0,4),(0,10)],
    [(0,2),(0,10),(0,4),(4,1),(0,4),(0,4),(0,4),(0,10)],
    [(0,6),(0,10),(0,4),(0,4),(0,4),(0,4),(0,4),(0,5)],
    [(0,6),(0,10),(0,4),(0,4),(0,4),(0,4),(0,4),(0,10)],
    [(0,2),(0,10),(0,4),(0,4),(0,4),(4,1),(0,4),(0,10)],
    [(0,6),(0,10),(0,4),(0,4),(0,4),(0,4),(0,4),(0,10)],
    [(0,11),(0,11),(0,11),(0,11),(0,11),(0,11),(0,11),(0,12)],
    ]

wallmask = [
    [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,3)],
    [None,(1,0),None,(10,0),(11,0),None,None,(1,0)],
    [None,(1,0),None,None,None,None,None,(4,5,R270|FX)],
    [None,(1,0),None,None,None,None,None,(15,0)],
    [None,(1,0),None,None,None,None,None,(4,4)],
    [None,(1,0),None,None,None,None,None,(1,0)],
    [None,(1,0),None,None,None,None,None,(1,0)],
    [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,2)],
    ]

decomask = [
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,(6,0),(7,0),(4,0),None,None],
    [None,None,None,(6,1),(7,1),None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,(4,0),(6,0),(7,0),None,None],
    [None,None,None,None,(6,1),(7,1),None,None],
    [None,None,None,None,None,None,None,None],
    ]

def render():
    for y in range(len(floormask)): # assume all 3 masks are the same size
        for x in range(len(floormask[y])):
            tilepos = (x * 16, y * 16)

            f_tile = floormask[y][x]
            w_tile = wallmask[y][x]
            d_tile = decomask[y][x]

            sprite.get_screen("game").blit(sprite.get_sprite(
                    "tiles", (16, 16), f_tile), tilepos)

            if w_tile != None:
                w_sprite = sprite.get_sprite("tiles", (16, 16), w_tile)

                if len(w_tile) > 2:
                    if w_tile[2] & R90: w_sprite = pygame.transform.rotate(w_sprite, 90)
                    if w_tile[2] & R180: w_sprite = pygame.transform.rotate(w_sprite, 180)
                    if w_tile[2] & R270: w_sprite = pygame.transform.rotate(w_sprite, 270)
                    if w_tile[2] & FXY: w_sprite = pygame.transform.flip(w_sprite, True, True)
                    if w_tile[2] & FX: w_sprite = pygame.transform.flip(w_sprite, True, False)
                    if w_tile[2] & FY: w_sprite = pygame.transform.flip(w_sprite, False, True)

                sprite.get_screen("game").blit(w_sprite, tilepos)

            if d_tile != None:
                d_sprite = sprite.get_sprite("tiles", (16, 16), d_tile)

                if len(d_tile) > 2:
                    if d_tile[2] & R90: d_sprite = pygame.transform.rotate(d_sprite, 90)
                    if d_tile[2] & R180: d_sprite = pygame.transform.rotate(d_sprite, 180)
                    if d_tile[2] & R270: d_sprite = pygame.transform.rotate(d_sprite, 270)
                    if d_tile[2] & FXY: d_sprite = pygame.transform.flip(d_sprite, True, True)
                    if d_tile[2] & FX: d_sprite = pygame.transform.flip(d_sprite, True, False)
                    if d_tile[2] & FY: d_sprite = pygame.transform.flip(d_sprite, False, True)

                sprite.get_screen("game").blit(d_sprite, tilepos)
