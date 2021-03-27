'''
Author: xmug
Date: 2021-03-18 20:18:29
LastEditors: xmug
LastEditTime: 2021-03-18 23:41:32
FilePath: \PacMan\modules\Sprites.py
'''

import pygame
import enum
import random
from .Util import Vector2

from pygame.color import Color

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
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
    def __init__(self, x, y, char_image_path):
        pygame.sprite.Sprite.__init__(self)
        self.char_name = char_image_path.split('/')[-1].split('.')[0]
        # load original image and convert it to canvas
        self.base_image = pygame.image.load(char_image_path).convert()
        # Copy, not reference
        self.image = self.base_image.copy()

        # setting postion
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        # setup some attributes
        self.move_buffer = Vector2.Zero()
        self.move_dir = Vector2.Zero()
        self.move_area = 10
        self.move_dArea = 30
        self.AIProgram = None
        # self.wall_sprites = wall_sprites
        # self.gates_sprites = gates_sprites

    # TODO: Make it FixedUpdate
    def update(self, wall_sprites, gates_sprites, move_buffer):
        # if(self.AIProgram != None):
        #     move_buffer = self.AIProgram(1, 2, 3)
        self.moveUpdate(wall_sprites, gates_sprites, move_buffer)

    def moveUpdate(self, wall_sprites, gates_sprites, move_buffer):
        if (move_buffer != Vector2.Zero()):
            self.move_buffer = move_buffer
        if (self.move_buffer != Vector2.Zero()):
            self.rect.x = self.rect.x + self.move_dArea * move_buffer.x
            self.rect.y = self.rect.y + self.move_dArea * move_buffer.y
            is_collide = pygame.sprite.spritecollide(self, wall_sprites, dokill=False)
            if is_collide:
                self.rect.x = self.rect.x + self.move_dArea * move_buffer.x * -1
                self.rect.y = self.rect.y + self.move_dArea * move_buffer.y * -1
            else:
                self.rect.x = self.rect.x + self.move_dArea * move_buffer.x * -1
                self.rect.y = self.rect.y + self.move_dArea * move_buffer.y * -1
                self.move_dir = move_buffer
                self.move_buffer = Vector2.Zero()
        if (self.move_dir != Vector2.Zero()):
            self.AnimUpdate(self.move_dir)

        self.rect.x = self.rect.x + self.move_area * self.move_dir.x
        self.rect.y = self.rect.y + self.move_area * self.move_dir.y
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, dokill=False)
        if is_collide:
            self.rect.x = self.rect.x + self.move_area * self.move_dir.x * -1
            self.rect.y = self.rect.y + self.move_area * self.move_dir.y * -1

    def AnimUpdate(self, vec2):
        if (vec2 == Vector2.Right()):
            self.image = self.base_image.copy()
        elif (vec2 == -1 * Vector2.Right()):
            self.image = pygame.transform.flip(self.base_image, True, False)
        elif (vec2 == Vector2.Up()):
            self.image = pygame.transform.rotate(self.base_image, 90)
        else:
            self.image = pygame.transform.rotate(self.base_image, -90)
