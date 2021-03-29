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
    move_buffer = Vector2.zero()
    graph = np.zeros((361, 361), dtype='int32')

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

    graph = csr_matrix(graph)
    start_index = int(self_pos[0] * 19 + self_pos[1])
    cur_index = int(target_pos[0] * 19 + target_pos[1])
    pre_node = 0
    dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=start_index,
                                              return_predecessors=True)
    while predecessors[cur_index] != -9999:
        pre_node = cur_index
        cur_index = predecessors[cur_index]

    r = int(pre_node / 19)
    c = pre_node % 19

    if r > self_pos[0]:
        move_buffer = Vector2.down()
    elif r < self_pos[0]:
        move_buffer = Vector2.up()
    elif c > self_pos[1]:
        move_buffer = Vector2.right()
    elif c < self_pos[1]:
        move_buffer = Vector2.left()

    return move_buffer
