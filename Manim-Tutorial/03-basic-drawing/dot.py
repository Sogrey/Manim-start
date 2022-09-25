from asyncore import write
from manim import *
import manimpango
# 导入base目录下基础工具函数
import sys
sys.path.append('../../base/')
from titles_credits import *


def showDot(self):
    g = Group(
        # 点
        Dot(color=PINK),
        AnnotationDot(stroke_color=YELLOW, fill_color=BLUE,fill_opacity=1),
        # 带文字标签的点
        LabeledDot(Tex("2022", color=RED)),
        LabeledDot(MathTex("A", color=GREEN)),
        LabeledDot(Text("Manim-基础图形", color=BLUE)).scale(0.3),
        LabeledDot("Lucy"),
    )
    g.arrange(RIGHT,buff=0.5).scale(1.5)
    g[:2].move_to(UP*1.5)
    g[2:].next_to(g[:2],DOWN,buff=1)
    for shape in g:
        self.add(shape)
        self.wait(0.5)

class ShowPoints(Scene):
    def construct(self):
        Title(self, "Manim基本图形 - 点(Dot)")

        showDot(self)

        Credits(self)

class DotExample(Scene):
    def construct(self):        
        Title(self, "Manim基本图形 - 点(Dot)")

        dot1 = Dot(point=LEFT, radius=0.08)
        dot2 = Dot(point=ORIGIN, color=GREEN, stroke_width=0.2,fill_opacity=0.5)
        dot3 = Dot(point=RIGHT, color=RED)
        self.play(Write(dot1),Write(dot2),Write(dot3))
        self.wait(10)

        Credits(self)

class AnnotationDotExample(Scene):
    def construct(self):        
        Title(self, "Manim基本图形 - 带轮廓的点(AnnotationDot)")

        adot1 = AnnotationDot(point=LEFT)
        adot2 = AnnotationDot(point=ORIGIN, fill_color=GREEN, stroke_width=1,stroke_color=RED,fill_opacity=0.5)
        adot3 = AnnotationDot(point=RIGHT, fill_color=RED)
        self.play(Write(adot1),Write(adot2),Write(adot3))
        self.wait(10)

        Credits(self)

class LabeledDotsExample(Scene):
    def construct(self):
        Title(self, "Manim基本图形 - 带标签的点(LabeledDot)")

        sq = Square(fill_color=RED, fill_opacity=1)
        self.add(sq)
        dot1 = LabeledDot(Tex("42", color=RED))
        dot2 = LabeledDot(MathTex("a", color=GREEN))
        dot3 = LabeledDot(Text("ii", color=BLUE))
        dot4 = LabeledDot("3")
        dot1.next_to(sq, UL)
        dot2.next_to(sq, UR)
        dot3.next_to(sq, DL)
        dot4.next_to(sq, DR)
        self.play(Write(dot1), Write(dot2), Write(dot3), Write(dot4))
        self.wait(10)

        Credits(self)


