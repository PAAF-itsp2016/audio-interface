#!/usr/bin/env python
import pygame
pygame.init()
song = pygame.mixer.Sound('TumSaathHo.mp3')
clock = pygame.time.Clock()
song.play()
while True:
    clock.tick(10)
pygame.quit()

