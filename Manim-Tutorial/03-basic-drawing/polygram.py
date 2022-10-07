from manim import *
import manimpango
# 导入base目录下基础工具函数
import sys
sys.path.append('../../base/')
from titles_credits import *

class RectangleExample(Scene):
    def construct(self):
        rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
        rect2 = Rectangle(width=1.0, height=4.0)
        rects = Group(rect1,rect2).arrange(buff=1)
        self.add(rects)