import pygame
import numpy as np
from jupyterlab.semver import Range
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
from .Util import Vector2

class GhostAI():
    def __int__(self):
        pass

    @classmethod
    def Blinky(cls, pathData, BlinkySprite, PacmanSprite):
        move_Buffer = Vector2.Zero()
        start_row = (BlinkySprite.rect.y-32)/30
        start_row = round(start_row)
        start_col = (BlinkySprite.rect.x-32)/30
        start_col = round(start_col)
        end_row = (PacmanSprite.rect.y-32)/30
        end_col = (PacmanSprite.rect.x-32) / 30
        end_row = round(end_row)
        end_col = round(end_col)
        # pathData[start_row][start_col] = 7
        # for each in pathData:
        #     print(each)
        # print("\n")

        graph = np.zeros((361, 361), dtype='int32')

        for row in range(19):
            for col in range(19):
                if(pathData[row][col] == 0):
                    if(col+1 < 19 and pathData[row][col+1] == 0):
                        graph[row * 19+col][row * 19 + col + 1] = 1
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
        dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=start_index, return_predecessors=True)
        print(predecessors[cur_index], start_row, start_col, end_row, end_col)
        while(predecessors[cur_index] != -9999):
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

        #print(pre_node,r, c, start_row, start_col, end_row, end_col)
        # print(move_Buffer)

        return move_Buffer

    def Clyde(self):
        pass

    def Inky(self):
        pass

    def Pinky(self):
        pass

    def path_finding(self):
        pass