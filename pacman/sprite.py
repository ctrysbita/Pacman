import pygame

import util as util
from gif import Gif


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])

        # Make the background transparent
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color, pygame.RLEACCEL)

        # Draw food (The yellow picky one)
        # This is Inscribed circle in the image canvas(position donest matter, because of Inside out)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Player(pygame.sprite.Sprite):
    def __init__(self, name: str, x, y, img: Gif):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.gif = img
        # Copy, not reference
        self.image = img.get_frame()

        # setting position
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        # setup some attributes

        # Input Ahead
        self.move_buffer = util.Vector2.zero()
        # Current movement
        self.move_dir = util.Vector2.zero()
        # MoveSpeed
        self.move_area = 6
        # Wall Detect Speed
        self.move_dArea = 30
        # GhostAI
        self.AIProgram = None

    def update(self, wall_sprites, gates_sprites, movement):
        self.image = self.gif.get_frame()
        # Try pre-movement every frame, test it whether it is legal
        if movement != util.Vector2.zero():
            self.move_buffer = movement
        if self.move_buffer != util.Vector2.zero():
            self.rect.x = self.rect.x + self.move_dArea * self.move_buffer.x
            self.rect.y = self.rect.y + self.move_dArea * self.move_buffer.y
            is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
            if is_collide:
                self.rect.x = self.rect.x + self.move_dArea * self.move_buffer.x * -1
                self.rect.y = self.rect.y + self.move_dArea * self.move_buffer.y * -1
            else:
                self.rect.x = self.rect.x + self.move_dArea * self.move_buffer.x * -1
                self.rect.y = self.rect.y + self.move_dArea * self.move_buffer.y * -1
                self.move_dir = self.move_buffer
                self.move_buffer = util.Vector2.zero()

        # Update Current Animation
        if self.move_dir != util.Vector2.zero():
            self.update_direction(self.move_dir)

        # Move
        self.rect.x = self.rect.x + self.move_area * self.move_dir.x
        self.rect.y = self.rect.y + self.move_area * self.move_dir.y

        # If collide with walls, move back
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
        if is_collide:
            self.rect.x = self.rect.x + self.move_area * self.move_dir.x * -1
            self.rect.y = self.rect.y + self.move_area * self.move_dir.y * -1

    def update_direction(self, vec2):
        if vec2 == util.Vector2.right():
            self.image = self.image.copy()
        elif vec2 == -1 * util.Vector2.right():
            self.image = pygame.transform.flip(self.image, True, False)
        elif vec2 == util.Vector2.up():
            self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = pygame.transform.rotate(self.image, -90)
