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

from ai import GhostAI
from gif import Gif
from sprite import Food, Player, Wall


class Level:
    """Represent a level (map) in game."""
    wall_specs = [
        (0, 0, 6, 600),
        (0, 0, 600, 6),
        (0, 600, 606, 6),
        (600, 0, 6, 606),
        (300, 0, 6, 66),
        (60, 60, 186, 6),
        (360, 60, 186, 6),
        (60, 120, 66, 6),
        (60, 120, 6, 126),
        (180, 120, 246, 6),
        (300, 120, 6, 66),
        (480, 120, 66, 6),
        (540, 120, 6, 126),
        (120, 180, 126, 6),
        (120, 180, 6, 126),
        (360, 180, 126, 6),
        (480, 180, 6, 126),
        (180, 240, 6, 126),
        (180, 360, 246, 6),
        (420, 240, 6, 126),
        (240, 240, 42, 6),
        (324, 240, 42, 6),
        (240, 240, 6, 66),
        (240, 300, 126, 6),
        (360, 240, 6, 66),
        (0, 300, 66, 6),
        (540, 300, 66, 6),
        (60, 360, 66, 6),
        (60, 360, 6, 186),
        (480, 360, 66, 6),
        (540, 360, 6, 186),
        (120, 420, 366, 6),
        (120, 420, 6, 66),
        (480, 420, 6, 66),
        (180, 480, 246, 6),
        (300, 480, 6, 66),
        (120, 540, 126, 6),
        (360, 540, 126, 6),
    ]
    gate_spec = (282, 242, 42, 2)

    def __init__(self):
        self.wall_sprites = pygame.sprite.Group()
        self.gate_sprites = pygame.sprite.Group()
        self.hero_sprites = pygame.sprite.Group()
        self.ghost_sprites = pygame.sprite.Group()
        self.food_sprites = pygame.sprite.Group()
        self.super_food_sprites = pygame.sprite.Group()
        self.path_data = []

    def setup_walls(self, color):
        for wall_spec in self.wall_specs:
            wall = Wall(*wall_spec, color)
            self.wall_sprites.add(wall)
        return self.wall_sprites

    def setup_gate(self, color):
        self.gate_sprites.add(Wall(*self.gate_spec, color))
        return self.gate_sprites

    def setup_players(self):
        self.hero_sprites.add(
            Player('Pacman', 290, 440, Gif('res/pacman.gif', (32, 32))))

        for hero in self.hero_sprites:
            hero.move_area = hero.move_area

        player = Player('Blinky', 287, 199, Gif('res/blinky.gif', (32, 32)))
        player.ai = GhostAI.Blinky
        player.move_area = 4
        self.ghost_sprites.add(player)

        player = Player('Clyde', 319, 259, Gif('res/clyde.gif', (32, 32)))
        player.ai = GhostAI.Clyde
        player.move_area = 5.5
        self.ghost_sprites.add(player)

        player = Player('Inky', 255, 259, Gif('res/inky.gif', (32, 32)))
        player.ai = GhostAI.Inky
        player.move_area = 4.5
        self.ghost_sprites.add(player)

        player = Player('Pinky', 287, 259, Gif('res/pinky.gif', (32, 32)))
        player.ai = GhostAI.Pinky
        player.hangOn = 0
        player.move_area = 5.5
        self.ghost_sprites.add(player)

        return self.hero_sprites, self.ghost_sprites

    def setup_food(self, color, bg_color):
        for row in range(19):
            for col in range(19):
                if (row == 7 or row == 8) and (col == 8 or col == 9
                                               or col == 10):
                    continue
                elif col % 6 != 0 or row % 6 != 0:
                    food = Food(30 * col + 32, 30 * row + 32, 8, 8, color,
                                bg_color)
                    is_collide = pygame.sprite.spritecollide(
                        food, self.wall_sprites, False)
                    if is_collide:
                        continue
                    is_collide = pygame.sprite.spritecollide(
                        food, self.hero_sprites, False)
                    if is_collide:
                        continue
                    self.food_sprites.add(food)

        return self.food_sprites

    def setup_super_food(self, color, bg_color):
        for row in range(19):
            for col in range(19):
                if (row == 7 or row == 8) and (col == 8 or col == 9
                                               or col == 10):
                    continue
                elif col % 6 == 0 and row % 6 == 0:
                    food = Food(30 * col + 32, 30 * row + 32, 12, 12, color,
                                bg_color)
                    is_collide = pygame.sprite.spritecollide(
                        food, self.wall_sprites, False)
                    if is_collide:
                        continue
                    is_collide = pygame.sprite.spritecollide(
                        food, self.hero_sprites, False)
                    if is_collide:
                        continue
                    self.super_food_sprites.add(food)

        return self.super_food_sprites

    def setup_path_data(self):
        for row in range(19):
            tmp_list = []
            tmp_list.clear()
            for col in range(19):
                collider = Food(30 * col + 32, 30 * row + 32, 8, 8, (0, 0, 0),
                                (0, 0, 0))
                is_collide = pygame.sprite.spritecollide(
                    collider, self.wall_sprites, False)
                if is_collide:
                    tmp_list.append(1)
                    continue
                tmp_list.append(0)
            self.path_data.append(tmp_list)
        return self.path_data
