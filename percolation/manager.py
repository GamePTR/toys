import random
from queue import Queue
from time import sleep

from union_find import UnionFind

class Manager:
    def __init__(self, n, window):
        self.over = False
        if window is not None:
            self.window = window
        self.n = n
        self.size = n * n
        self.cavancy = 0
        # The top and bottom showed by this two virtual node
        # see pdf page 58
        self.top = n * n
        self.bottom = n * n + 1

        self.que = Queue()
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.uf = UnionFind(n * n + 2)

        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def bfs(self):
        if not self.que.empty():
            sz = self.que.qsize()
            for i in range(sz):
                [x, y] = self.que.get()
                # top
                if x == -1:
                    for j in range(self.n):
                        if self.grid[0][j] == 1:
                            self.grid[0][j] = 2
                            self.window.change2blud(0, j)
                            self.que.put([0, j])

                else:
                    for k in range(4):
                        xx, yy = x + self.dx[k], y + self.dy[k]
                        if 0 <= xx < self.n and 0 <= yy < self.n and self.grid[xx][yy] == 1:
                            self.grid[xx][yy] = 2
                            self.window.change2blud(xx, yy)
                            self.que.put([xx, yy])
            # sleep(0.1)


    def expansion(self, i, j):
        # from top
        if i == 0:
            self.uf.union(self.top, i * self.n + j)
            self.que.put([-1, 0])
        # to bottom
        if i is self.n - 1:
            self.uf.union(self.bottom, i * self.n + j)
            # self.que.put([self.n, 0])

        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] != 0:
                self.uf.union(i * self.n + j, x * self.n + y)
                if self.grid[x][y] == 2:
                    self.que.put([x, y])
        
        self.bfs()
        if self.uf.connected(self.top, self.bottom) and self.que.empty():
            print("p is", self.cavancy / self.size)
            self.over = True
            

    # Update a grid
    def update(self):
        if self.que.empty():
            # random (i, j) for change 
            i, j = 0, 0
            while True:
                i = random.randint(0, self.n - 1)
                j = random.randint(0, self.n - 1)
                if self.grid[i][j] == 0:
                    break
            self.grid[i][j] = 1
            self.window.change2white(i, j)
            self.cavancy += 1
            self.expansion(i, j)
        else:
            self.bfs()




        
