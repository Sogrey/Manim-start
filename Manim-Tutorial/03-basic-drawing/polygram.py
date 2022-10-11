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

class RoundedRectangleExample(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(corner_radius=0.5)
        rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)
        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)

class SquareExample(Scene):
    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)