from manim import *

# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

def Logo(self):
    circle = Circle()
    square = Square()
    triangle = Triangle()

    circle.shift(LEFT)
    square.shift(UP)
    triangle.shift(RIGHT)

    self.add(circle, square, triangle)
    self.wait(3)

# manim titles_credits.py -pqm
class ShowLogo(Scene):
    def construct(self):
        Title(self, "The logo of the manim")

        Logo(self)

        Credits(self)
