"""
Visulization of the percolation process
"""

import tkinter as tk  
import random

from manager import Manager
  
class GridWindow:  
    def __init__(self, n):  
        self.mgr = Manager(n, self)
        self.blocksize = 10
        self.n = n  
        self.window = tk.Tk()  
        self.window.title("Grid Window")  
        self.canvas = tk.Canvas(self.window, width=n*self.blocksize, height=n*self.blocksize)  
        self.canvas.pack()  
        self.grid_rects = {}  # 用于存储所有网格的矩形对象  
  
        # 绘制初始网格（黑色）  
        for i in range(n):  
            for j in range(n):  
                x1, y1 = i*self.blocksize, j*self.blocksize  
                x2, y2 = (i+1)*self.blocksize, (j+1)*self.blocksize  
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")  
                self.grid_rects[(i, j)] = rect  # 将矩形对象存储在字典中  

        # 启动事件循环  
        self.window.after(100, self.update)  # 每100毫秒调用一次update方法，用于处理动态更新  


    def update(self):  
        """更新窗口内容的方法，可以在这里添加动态改变颜色的逻辑"""  
        self.mgr.update()

        # 继续调用update方法以持续更新  
        if not self.mgr.over:
            self.window.after(5, self.update)  

    # methods for outter
    def change_color(self, j, i, color):  
        """动态改变指定坐标的网格颜色"""  
        if 0 <= i < self.n and 0 <= j < self.n:  
            self.canvas.itemconfig(self.grid_rects[(i, j)], fill=color)  

    def change2white(self, i, j):
        self.change_color(i, j, "#ffffff")
    
    def change2blud(self, i, j):
        self.change_color(i, j, "#00ced1")
  
    def run(self):  
        """运行窗口并进入主循环"""  
        self.window.mainloop()


n = 50  # 网格大小  
grid_window = GridWindow(n)  
grid_window.run()  # 运行窗口