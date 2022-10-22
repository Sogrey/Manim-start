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

class TriangleExample(Scene):
    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)

class PolygonExample(Scene):
    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)

class RegularPolygonExample(Scene):
    def construct(self):
        poly_1 = RegularPolygon(n=6)
        poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
        poly_3 = RegularPolygon(n=10, color=RED)
        poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        self.add(poly_group)

class StarExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        star = Star(outer_radius=2, color=RED)
        self.add(pentagram)
        self.play(Create(star), run_time=3)
        self.play(FadeOut(star), run_time=2)

class DifferentDensitiesExample(Scene):
    def construct(self):
        density_2 = Star(7, outer_radius=2, density=2, color=RED)
        density_3 = Star(7, outer_radius=2, density=3, color=PURPLE)
        self.add(VGroup(density_2, density_3).arrange(RIGHT))
        
import numpy as np
class PolygramExample(Scene):
    def construct(self):
        hexagram = Polygram(
            [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
            [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
        )
        self.add(hexagram)
        dot = Dot()
        self.play(MoveAlongPath(dot, hexagram), run_time=5, rate_func=linear)
        self.remove(dot)
        self.wait()

class RegularPolygramExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        self.add(pentagram)

class CutoutExample(Scene):
    def construct(self):
        s1 = Square().scale(2.5)
        s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
        s3 = Square().shift(UP + RIGHT).scale(0.5)
        s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
        s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
        c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
        self.play(Write(c), run_time=4)
        self.wait()

class ExampleCross(Scene):
    def construct(self):
        text = Text("It's wrong.")
        cross = Cross(text)
        self.add(text)
        self.add(cross)