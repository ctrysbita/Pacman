'''
Author: xmug
Date: 2021-03-18 20:18:29
LastEditors: xmug
LastEditTime: 2021-03-18 23:41:32
FilePath: \PacMan\modules\Sprites.py
'''

import pygame
import random

from pygame.color import Color

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, **kwargs):
        super().__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color, **kwargs):
        super().__init__(self)
        self.image = pygame.Surface([width, height])

        # Make the background transparent
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color, pygame.RLEACCEL)

        # Draw food (The yellow picky one)
        # This is Inscribed circle in the image canvas(position donest matter, because of Inside out)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Put the image canvas at the correct position
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, char_name ,char_image_path):
        super.__init__(self)
        self.char_name = char_name
        # load original image and convert it to canvas
        self.base_image = pygame.image.load(char_image_path).convert()
        # Copy, not reference
        self.curr_image = self.base_image.copy()

        # setting postion
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        # setup some attributes
        self.base_speed = 30
        self.curr_speed = 0

    def Update(self):
        pass

    def AnimUpdate(self):
        pass



        
        