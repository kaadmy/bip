#!/usr/bin/python2.7

import atexit

import game

def cleanup():
    game.cleanup()

def init():
    atexit.register(cleanup)
    game.init()

if __name__ == "__main__":
    init()
