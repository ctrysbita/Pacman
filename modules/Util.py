import pygame
import threading
import time
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

class Util():
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

    @classmethod
    def path_finding(cls, pathData, selfPos, tarPos):
        move_Buffer = Util.Vector2.Zero()

        # pathData[start_row][start_col] = 7
        # pathData[end_row][end_col] = 7
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
        # print(end_row, end_col)
        start_index = int(selfPos[0] * 19 + selfPos[1])
        cur_index = int(tarPos[0] * 19 + tarPos[1])
        pre_node = 0
        dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=start_index,
                                                  return_predecessors=True)
        while (predecessors[cur_index] != -9999):
            pre_node = cur_index
            cur_index = predecessors[cur_index]

        r = (int)(pre_node / 19)
        c = pre_node % 19

        if r > selfPos[0]:
            move_Buffer = Util.Vector2.Up() * -1
        elif r < selfPos[0]:
            move_Buffer = Util.Vector2.Up()
        elif c > selfPos[1]:
            move_Buffer = Util.Vector2.Right()
        elif c < selfPos[1]:
            move_Buffer = Util.Vector2.Right() * -1

        return move_Buffer

    class Thread(threading.Thread):
        def __init__(self, function, args=()):
            threading.Thread.__init__(self)
            self.function = function
            self.args = args
            self.result = None

        def run(self):
            self.result = self.function(*self.args)

        def get_result(self):
            try:
                return self.result
            except Exception:
                return None