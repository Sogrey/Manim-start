from manim import *
# manim titles_credits.py -pqm

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

def mul9x9(self):
    square = Square()
    self.add(square)
    self.wait(3)

class ShowLogo(Scene):
    def construct(self):
        Title(self, "The logo of the manim")

        # Logo(self)
        # mul9x9(self)

        Credits(self)


class HelloCircle(Scene):
    def construct(self):
        # blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        # We can also create a "plain" circle and add the desired attributes via set methods:
        circle = Circle()
        blue_circle = circle.set_color(BLUE).set_opacity(0.5)
        
        label = Text("A wild circle appears!")
        label.next_to(blue_circle, DOWN, buff=0.5)
        
        self.play(Create(blue_circle), Write(label))
        self.wait()

class CircleAnnouncement(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        announcement = Text("Let us draw a circle.")
        
        self.play(Write(announcement))
        self.wait()
        
        self.play(announcement.animate.next_to(blue_circle, UP, buff=0.5))
        self.play(Create(blue_circle))

class AnimateSyntax(Scene):
    def construct(self):
        triangle = Triangle(color=RED, fill_opacity=1)
        self.play(DrawBorderThenFill(triangle))
        self.play(triangle.animate.shift(LEFT))
        self.play(triangle.animate.shift(RIGHT).scale(2))
        self.play(triangle.animate.rotate(PI/3))

class CauchyIntegralFormula(Scene):
    def construct(self):
        formula = MathTex(r"[z^n]f(z) = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z^{n+1}}~dz")
        self.play(Write(formula), run_time=3)
        self.wait()