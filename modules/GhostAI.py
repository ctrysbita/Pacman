import pygame
from .Util import Util
from jupyterlab.semver import Range

class GhostAI():
    @classmethod
    def LocProcess(cls, Ghost, Pacman, offset):
        tarPos = pygame.Vector2(Pacman.rect.y, Pacman.rect.x)
        selfPos = pygame.Vector2(Ghost.rect.y, Ghost.rect.x)

        tarPos = [round((i - 16) / 30) for i in tarPos] + offset
        selfPos = [round((i - 16) / 30) for i in selfPos]

        return selfPos, tarPos

    @classmethod
    def Blinky(cls, pathData, Ghost, Pacman):
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman, [0, 0])
        return Util.path_finding(pathData, selfPos, tarPos)

    @classmethod
    def Clyde(cls, pathData, Ghost, Pacman):
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman, [0, 0])
        return Util.path_finding(pathData, selfPos,  tarPos)

    @classmethod
    def Inky(cls, pathData, Ghost, Pacman):
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman, [0, 0])
        return Util.path_finding(pathData, selfPos, tarPos)

    @classmethod
    def Pinky(cls, pathData, Ghost, Pacman):
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman, [0, 0])
        return Util.path_finding(pathData, selfPos, tarPos)