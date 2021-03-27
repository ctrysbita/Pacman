import pygame
from jupyterlab.semver import Range
from .Util import Vector2
from .Util import PathFind

class GhostAI():
    @classmethod
    def Blinky(cls, pathData, Sprite, PacmanSprite):
        tarPos = pygame.Vector2(PacmanSprite.rect.x, PacmanSprite.rect.y)
        return PathFind.path_finding(pathData, Sprite.rect, PacmanSprite.rect)

    @classmethod
    def Clyde(cls, pathData, Sprite, PacmanSprite):
        tarPos = pygame.Vector2(PacmanSprite.rect.x, PacmanSprite.rect.y)
        return PathFind.path_finding(pathData, Sprite.rect,  PacmanSprite.rect)

    @classmethod
    def Inky(cls, pathData, Sprite, PacmanSprite):
        tarPos = pygame.Vector2(PacmanSprite.rect.x, PacmanSprite.rect.y)
        return PathFind.path_finding(pathData, Sprite.rect, PacmanSprite.rect)

    @classmethod
    def Pinky(cls, pathData, Sprite, PacmanSprite):
        tarPos = pygame.Vector2(PacmanSprite.rect.x, PacmanSprite.rect.y)
        return PathFind.path_finding(pathData, Sprite.rect, PacmanSprite.rect)