import pygame


pygame.init()
pygame.mixer.music.load('light.mp3')
pygame.mixer.music.play()
pygame.event.wait()
