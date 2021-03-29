import pygame

import util


class GhostAI:
    """ Transform World Wide Location to a iterable game map"""

    @classmethod
    def LocProcess(cls, Ghost, Pacman):
        tarPos = pygame.Vector2(Pacman.rect.y, Pacman.rect.x)
        selfPos = pygame.Vector2(Ghost.rect.y, Ghost.rect.x)

        tarPos = [round((i - 16) / 30) for i in tarPos]
        selfPos = [round((i - 16) / 30) for i in selfPos]

        return selfPos, tarPos

    @classmethod
    def Blinky(cls, pathData, Ghost, Pacman):

        # Slow movement
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman)

        return util.find_path(pathData, selfPos, tarPos)

    @classmethod
    def Clyde(cls, pathData, Ghost, Pacman):
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman)

        # Foresee the movement of Pacman
        for offset in range(1, 4):
            tmp = tarPos + Pacman.move_dir * offset
            if tmp[0] > 18 or tmp[0] < 0 or tmp[1] > 18 or tmp[1] < 0:
                break
            if pathData[int(tmp[0])][int(tmp[1])] == 0:
                tarPos = tmp
                break

        return util.find_path(pathData, selfPos, tarPos)

    @classmethod
    def Inky(cls, pathData, Ghost, Pacman):
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman)

        # Chase the Pacman 1-4 tiles slow
        for offset in range(1, 4):
            tmp = tarPos + Pacman.move_dir * offset * -1
            if tmp[0] > 18 or tmp[0] < 0 or tmp[1] > 18 or tmp[1] < 0:
                break
            if pathData[int(tmp[0])][int(tmp[1])] == 0:
                tarPos = tmp
                break

        return util.find_path(pathData, selfPos, tarPos)

    @classmethod
    def Pinky(cls, pathData, Ghost, Pacman):

        # Chase the pacman with 100% speed
        selfPos, tarPos = GhostAI.LocProcess(Ghost, Pacman)

        # # RandomMovement

        # # No need to use targetPos of pacman, because pinky is kinda silly
        # selfPos, tarPos = GhostAI.LocProcess(Ghost, Ghost)
        #
        # print(Ghost.hangOn)
        # if(Ghost.hangOn == 0):
        #     rand_x = random.randint(0,18)
        #     rand_y = random.randint(0,18)
        #
        #     while pathData[rand_x][rand_y] == 1:
        #         rand_x = random.randint(0, 18)
        #         rand_y = random.randint(0, 18)
        #     else:
        #         tarPos = pygame.Vector2(rand_x, rand_y)
        #
        # # A clock
        # if(Ghost.hangOn == 0):
        #     Ghost.hangOn = random.randint(30, 200)
        #
        # Ghost.hangOn -= 1

        return util.find_path(pathData, selfPos, tarPos)
