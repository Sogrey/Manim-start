from manim import *
import manimpango
# 导入base目录下基础工具函数
import sys
sys.path.append('../../base/')
from titles_credits import *


def showLine(self):
    g = Group(
        # 线
        Line(0.5*LEFT,0.5*RIGHT,color=YELLOW),
        # 虚线
        DashedLine(0.5*LEFT,0.5*RIGHT,color=TEAL),
        # 箭头
        Arrow(color=BLUE), 
        Arrow(color= BLUE, tip_shape=ArrowCircleFilledTip), #  ArrowCircleTip
        Arrow(color= BLUE, tip_shape=ArrowSquareTip),# ArrowSquareFilledTip
        # 双箭头
        DoubleArrow(color=BLUE),
        # 弯曲的箭头
        CurvedArrow(LEFT,RIGHT,angle=90*DEGREES,color= BLUE), 
    )
    g.arrange(RIGHT,buff=0.5)
    g[:3].move_to(UP*1.5)
    g[3:].next_to(g[:3],DOWN,buff=1)
    for shape in g:
        self.add(shape)
        self.wait(0.5)

class ShowLines(Scene):
    def construct(self):
        Title(self, "Manim基本图形 - 线(Line)")

        showLine(self)

        Credits(self)
