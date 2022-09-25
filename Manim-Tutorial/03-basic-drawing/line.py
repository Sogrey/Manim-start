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

class LineExample(Scene):
    def construct(self):
        g = Group(
            # 线
            Line(),
            Line(buff=0.5,color=TEAL),
            Line(buff=2,color=BLUE),
            
            Line(path_arc=0,color=RED),
            Line(path_arc=1,color=GREEN),
            Line(path_arc=5,color=YELLOW),
        )
        g.arrange(RIGHT,buff=0.5)
        g[:3].move_to(UP*1.5)
        g[3:].next_to(g[:3],DOWN,buff=1)
        for shape in g:
            self.add(shape)
            self.wait(2)

        self.wait(10)

class DashedLineExample(Scene):
    def construct(self):
        g = Group(
            # 线
            DashedLine(),
            DashedLine(buff=0.5,color=TEAL),
            DashedLine(buff=2,color=BLUE),

            DashedLine( dash_length=0.1),
            DashedLine( dash_length=0.1,dashed_ratio=0.5,color=YELLOW),
            DashedLine( dash_length=0.1,dashed_ratio=1.0,color=RED),
        )
        g.arrange(RIGHT)
        g[:3].move_to(UP)
        g[3:].next_to(g[:3],DOWN)
        for shape in g:
            self.add(shape)
            self.wait(2)

        self.wait(10)


class ArrowExample(Scene):
    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)
        # the effect of buff
        square = Square(color=MAROON_A)
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)
        # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)
        self.add(Group(g1, g2, g3).arrange(buff=2))


class ArrowExample2(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)
        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)
        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)
        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)
        self.add(left_group, middle_group, UR_group, DR_group)

# from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)

class DoubleArrowExample2(Scene):
    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)