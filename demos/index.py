from manim import *
from manim_cad_drawing_utils import *
from manim_fonts import *
from manim_fontawesome import *

# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

# config.background_color = WHITE

class TextMoreCustomization(Scene):
    def construct(self):
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.add(text1)
        
class AngryEmoji(Scene):
    def construct(self):
        # import https://fontawesome.com/v5.15/icons/angry?style=regular
        self.add(solid.archway.set_color(WHITE))

# class ExampleTextFont(Scene):
#     def construct(self):
#         with RegisterFont("Poppins") as fonts:
#             a=Text("Hello World",font=fonts[0])
#             self.play(Write(a))

def Logo(self):
    circle = Circle()
    square = Square()
    triangle = Triangle()

    circle.shift(LEFT)
    square.shift(UP)
    triangle.shift(RIGHT)

    self.add(circle, square, triangle)
    self.wait(3)

# def mul9x9(self):
#     square = Square()
#     self.add(square)
#     self.wait(3)

class ShowLogo(Scene):
    def construct(self):
        Title(self, "The logo of the manim")

        Logo(self)

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
        formula = MathTex(
            r"[z^n]f(z) = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z^{n+1}}~dz")
        self.play(Write(formula), run_time=3)
        self.wait()


# class Test_round(Scene):
#     def construct(self):
#         mob1 = RegularPolygon(n=4,radius=1.5,color=PINK).rotate(PI/4)
#         mob2 = Triangle(radius=1.5,color=TEAL)
#         crbase = Rectangle(height=0.5,width=3)
#         mob3 = Union(crbase.copy().rotate(PI/4),crbase.copy().rotate(-PI/4),color=BLUE)
#         mob4 = Circle(radius=1.3)
#         mob2.shift(2.5*UP)
#         mob3.shift(2.5*DOWN)
#         mob1.shift(2.5*LEFT)
#         mob4.shift(2.5*RIGHT)

#         mob1 = Round_Corners(mob1, 0.25)
#         mob2 = Round_Corners(mob2, 0.25)
#         mob3 = Round_Corners(mob3, 0.25)
#         self.add(mob1,mob2,mob3,mob4)