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

import numpy as np
import pygame
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path


class Vector2:
    @classmethod
    def left(cls):
        return pygame.Vector2(-1, 0)

    @classmethod
    def right(cls):
        return pygame.Vector2(1, 0)

    @classmethod
    def up(cls):
        return pygame.Vector2(0, -1)

    @classmethod
    def down(cls):
        return pygame.Vector2(0, 1)

    @classmethod
    def standard(cls):
        return pygame.Vector2(1, 1)

    @classmethod
    def zero(cls):
        return pygame.Vector2(0, 0)


def find_path(path_data, self_pos, target_pos):

    # The final movement command that will be returned
    move_buffer = Vector2.zero()

    # An empty graph waiting to be filled
    graph = np.zeros((361, 361), dtype='int32')

    # Convert map data into a 361 x 361 array of distances representing the graph.
    for row in range(19):
        for col in range(19):
            if path_data[row][col] == 0:
                if col + 1 < 19 and path_data[row][col + 1] == 0:
                    graph[row * 19 + col][row * 19 + col + 1] = 1
                if row + 1 < 19 and path_data[row + 1][col] == 0:
                    graph[row * 19 + col][(row + 1) * 19 + col] = 1
                if col > 0 and path_data[row][col - 1] == 0:
                    graph[row * 19 + col][row * 19 + col - 1] = 1
                if row > 0 and path_data[row - 1][col] == 0:
                    graph[row * 19 + col][(row - 1) * 19 + col] = 1

    # Using Scipy matrix compressing to compress the graph to increase efficiency
    graph = csr_matrix(graph)

    # Current position of Ghost
    start_index = int(self_pos[0] * 19 + self_pos[1])

    # Current postion of Pacman. Later will be used as predecessor to reconstruct the shortest path
    cur_index = int(target_pos[0] * 19 + target_pos[1])

    # Store the next position the ghost should go to
    pre_node = 0

    # Using Scipy shortest_path algorithm to get the shortest_path
    # In this game's case, it is Dijkstra algorithm
    dist_matrix, predecessors = shortest_path(csgraph=graph,
                                              directed=False,
                                              indices=start_index,
                                              return_predecessors=True)

    # Reconstruct shortest_path
    while predecessors[cur_index] != -9999:
        pre_node = cur_index
        cur_index = predecessors[cur_index]

    # Convert the distance data back to map data in order to guide the ghost movement
    r = int(pre_node / 19)
    c = pre_node % 19

    # Turn the map data into certain movement command
    if r > self_pos[0]:
        move_buffer = Vector2.down()
    elif r < self_pos[0]:
        move_buffer = Vector2.up()
    elif c > self_pos[1]:
        move_buffer = Vector2.right()
    elif c < self_pos[1]:
        move_buffer = Vector2.left()

    return move_buffer
