import pygame

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