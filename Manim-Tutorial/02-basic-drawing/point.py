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
        LabeledDot(MathTex("a", color=GREEN)),
        LabeledDot(Text("Python数据之道", color=BLUE)).scale(0.3),
        LabeledDot("Lemon"),
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
