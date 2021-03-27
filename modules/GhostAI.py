import pygame
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
        # start_row = (BlinkySprite.rect.y-32)/30
        # start_row = round(start_row)
        # start_col = (BlinkySprite.rect.x-32)/30
        # start_col = round(start_col)
        # end_row = (PacmanSprite.rect.y-32)/30
        # end_col = (PacmanSprite.rect.x-32) / 30
        # end_row = round(end_row)
        # end_col = round(end_col)
        # pathData[start_row][start_col] = 2
        # pathData[end_row][end_col] = 2

        # print(PacmanSprite.rect.x, PacmanSprite.rect.y)
        # print(end_row, end_col)
        graph = [0] * 361
        graph = [graph] * 361

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

        dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=98, return_predecessors=True)

        print(predecessors)

        return move_Buffer

    def Clyde(self):
        pass

    def Inky(self):
        pass

    def Pinky(self):
        pass

    def path_finding(self):
        pass