# Copyright (C) 2021 @ctrysbita @x-mug
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pygame

import util


class GhostAI:
    @classmethod
    def get_pos(cls, ghost, pacman):
        """ Transform World Wide Location to a iterable game map"""
        target_pos = pygame.Vector2(pacman.rect.y, pacman.rect.x)
        self_pos = pygame.Vector2(ghost.rect.y, ghost.rect.x)

        target_pos = [round((i - 16) / 30) for i in target_pos]
        self_pos = [round((i - 16) / 30) for i in self_pos]

        return self_pos, target_pos

    @classmethod
    def Blinky(cls, path_data, ghost, pacman):

        # Slow movement
        self_pos, target_pos = GhostAI.get_pos(ghost, pacman)

        return util.find_path(path_data, self_pos, target_pos)

    @classmethod
    def Clyde(cls, path_data, ghost, pacman):
        self_pos, target_pos = GhostAI.get_pos(ghost, pacman)

        # Foresee the movement of pacman
        for offset in range(1, 4):
            tmp = target_pos + pacman.move_dir * offset
            if tmp[0] > 18 or tmp[0] < 0 or tmp[1] > 18 or tmp[1] < 0:
                break
            if path_data[int(tmp[0])][int(tmp[1])] == 0:
                target_pos = tmp
                break

        return util.find_path(path_data, self_pos, target_pos)

    @classmethod
    def Inky(cls, path_data, ghost, pacman):
        self_pos, target_pos = GhostAI.get_pos(ghost, pacman)

        # Chase the pacman 1-4 tiles slow
        for offset in range(1, 4):
            tmp = target_pos + pacman.move_dir * offset * -1
            if tmp[0] > 18 or tmp[0] < 0 or tmp[1] > 18 or tmp[1] < 0:
                break
            if path_data[int(tmp[0])][int(tmp[1])] == 0:
                target_pos = tmp
                break

        return util.find_path(path_data, self_pos, target_pos)

    @classmethod
    def Pinky(cls, path_data, ghost, pacman):

        # Chase the pacman with 100% speed
        self_pos, target_pos = GhostAI.get_pos(ghost, pacman)

        return util.find_path(path_data, self_pos, target_pos)
