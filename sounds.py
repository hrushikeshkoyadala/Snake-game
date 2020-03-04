import pygame, random, sounds
from pygame.locals import *


pygame.init()
apple_sound = pygame.mixer.Sound("eats_apple.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
turn_sound = pygame.mixer.Sound("turn_sound.wav")

#Plays Sound when snake eats Apple
def play_sound_1():
    global apple_sound
    pygame.mixer.Sound.play(apple_sound)
    pygame.mixer.music.stop()


#Game-over sound
def play_sound_2():
    global game_over_sound
    pygame.mixer.Sound.play(game_over_sound)
    pygame.mixer.music.stop()

#Plays sound when snake turns
def play_sound_3():
    global turn_sound
    pygame.mixer.Sound.play(turn_sound)
    pygame.mixer.music.stop()
