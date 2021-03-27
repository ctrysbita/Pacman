import pygame
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

class Vector2():
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

class PathFind():
    @classmethod
    def path_finding(cls, pathData, selfPos, tarPos):
        move_Buffer = Vector2.Zero()
        start_row = (selfPos.y - 16) / 30
        start_row = round(start_row)
        start_col = (selfPos.x - 16) / 30
        start_col = round(start_col)
        end_row = (tarPos.y - 16) / 30
        end_col = (tarPos.x - 16) / 30
        end_row = round(end_row)
        end_col = round(end_col)

        # pathData[start_row][start_col] = 7
        # # print(selfPos.y, selfPos.x , start_row, start_col)
        # for each in pathData:
        #     print(each)
        # print("\n")

        graph = np.zeros((361, 361), dtype='int32')

        for row in range(19):
            for col in range(19):
                if (pathData[row][col] == 0):
                    if (col + 1 < 19 and pathData[row][col + 1] == 0):
                        graph[row * 19 + col][row * 19 + col + 1] = 1
                    if (row + 1 < 19 and pathData[row + 1][col] == 0):
                        graph[row * 19 + col][(row + 1) * 19 + col] = 1
                    if (col > 0 and pathData[row][col - 1] == 0):
                        graph[row * 19 + col][row * 19 + col - 1] = 1
                    if (row > 0 and pathData[row - 1][col] == 0):
                        graph[row * 19 + col][(row - 1) * 19 + col] = 1

        graph = csr_matrix(graph)

        start_index = start_row * 19 + start_col
        cur_index = end_row * 19 + end_col
        pre_node = 0
        dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=start_index,
                                                  return_predecessors=True)
        # print(predecessors[cur_index], start_row, start_col, end_row, end_col)
        while (predecessors[cur_index] != -9999):
            pre_node = cur_index
            cur_index = predecessors[cur_index]

        r = (int)(pre_node / 19)
        c = pre_node % 19

        if r > start_row:
            move_Buffer = Vector2.Up() * -1
        elif r < start_row:
            move_Buffer = Vector2.Up()
        elif c > start_col:
            move_Buffer = Vector2.Right()
        elif c < start_col:
            move_Buffer = Vector2.Right() * -1

        return move_Buffer