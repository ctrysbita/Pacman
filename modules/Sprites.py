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

from pygame.color import Color


class Vector2():
    def __init__(self, x, y):
        return (x, y)

    @classmethod
    def Right(cls):
        return pygame.Vector2(1, 0)

    @classmethod
    def Up(cls):
        return pygame.Vector2(0, -1)

    @classmethod
    def Standard(cls):
        return pygame.Vector2(1, 1)

    @classmethod
    def Zero(cls):
        return pygame.Vector2(0, 0)


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
        self.move_dir = Vector2.Zero()
        self.move_area = 10
        # self.wall_sprites = wall_sprites
        # self.gates_sprites = gates_sprites

    # TODO: Make it FixedUpdate, UpdateAnimation, FixedOngoingPath, Command_Buffer
    def update(self, wall_sprites, gates_sprites, move_dir):
        if(move_dir != Vector2.Zero):
            self.AnimUpdate(move_dir)

        self.rect.x = self.rect.x + self.move_area * move_dir.x
        self.rect.y = self.rect.y + self.move_area * move_dir.y
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, dokill=False)
        if is_collide:
            self.rect.x = self.rect.x + self.move_area * move_dir.x * -1
            self.rect.y = self.rect.y + self.move_area * move_dir.y * -1

    def AnimUpdate(self, vec2):
        if (vec2 == Vector2.Right()):
            self.image = self.base_image.copy()
        elif (vec2 == -1 * Vector2.Right()):
            self.image = pygame.transform.flip(self.base_image, True, False)
        elif (vec2 == Vector2.Up()):
            self.image = pygame.transform.rotate(self.base_image, 90)
        else:
            self.image = pygame.transform.rotate(self.base_image, -90)
