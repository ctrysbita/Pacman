"""
Author: xmug
Date: 2021-03-18 23:42:07
LastEditors: xmug
LastEditTime: 2021-03-19 00:03:41
FilePath: \PacMan\test.py
"""

import pygame

pygame.init()

CAMERA = pygame.display.set_mode([400, 400])
CAMERA.fill((255, 255, 255))

image = pygame.Surface([10, 10])
image.fill((0, 0, 0))
image.set_colorkey((0, 0, 0), pygame.RLEACCEL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.ellipse(CAMERA, (128, 128, 128), [0, 0, 400, 400])
    pygame.display.flip()