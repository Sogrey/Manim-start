from manim import *
import manimpango
# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

class HelloWorld(Scene):
    def construct(self):
        T = Text("Hello World")
        # self.add(T)
        self.play(Write(T),run_time=5)
        self.wait(10)

class SimpleGeometry(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(np.array([4,0,0]),np.array([6,0,0]))
        triangle = Polygon(np.array([-5,-1,0]),np.array([-4,1,0]),np.array([-3,-1,0]))

        self.play(Write(circle),run_time=5)
        self.play(Write(square),run_time=5)
        self.play(Write(line),run_time=5)
        self.play(Write(triangle),run_time=5)

class ToEdge(Scene):
    def construct(self):
        TUL = Text(".to_edge(UP+LEFT)").to_edge(UP+LEFT).scale(0.3)
        TU = Text(".to_edge(UP)").to_edge(UP).scale(0.3)
        TUR = Text(".to_edge(UP+RIGHT)").to_edge(UP+RIGHT).scale(0.3)
        TL = Text(".to_edge(LEFT)").to_edge(LEFT).scale(0.3)
        TR = Text(".to_edge(RIGHT)").to_edge(RIGHT).scale(0.3)
        TBL = Text(".to_edge(DOWN+LEFT)").to_edge(DOWN+LEFT).scale(0.3)
        TD = Text(".to_edge(DOWN)").to_edge(DOWN).scale(0.3)
        TDR = Text(".to_edge(DOWN+RIGHT)").to_edge(DOWN+RIGHT).scale(0.3)

        self.add(TUL ,TU ,TUR,TL,TR,TBL,TD,TDR )

class ToCorner(Scene):
    def construct(self):
        TUL = Text(".to_corner(UP+LEFT)").to_corner(UP+LEFT).scale(0.3)
        TUR = Text(".to_corner(UP+RIGHT)").to_corner(UP+RIGHT).scale(0.3)
        TBL = Text(".to_corner(DOWN+LEFT)").to_corner(DOWN+LEFT).scale(0.3)
        TDR = Text(".to_corner(DOWN+RIGHT)").to_corner(DOWN+RIGHT).scale(0.3)

        self.add(TUL,TUR,TBL,TDR,TC )

class PlayToEdge(Scene):
    def construct(self):
        square = Square()
        square.generate_target()

        self.add(square)

        square.target.shift(UP)
        self.play(MoveToTarget(square))

        square.target.shift(UP+LEFT)
        self.play(MoveToTarget(square))

        square.target.shift(LEFT)
        self.play(MoveToTarget(square))

        square.target.shift(DOWN+LEFT)
        self.play(MoveToTarget(square))

        square.target.shift(DOWN)
        self.play(MoveToTarget(square))

        square.target.shift(DOWN+RIGHT)
        self.play(MoveToTarget(square))

        square.target.shift(RIGHT)
        self.play(MoveToTarget(square))

        square.target.shift(UP+RIGHT)
        self.play(MoveToTarget(square))

        square.target.shift(UP)
        self.play(MoveToTarget(square))

        square.target.shift(ORIGIN)
        self.play(MoveToTarget(square))

        self.wait()

class PlayToEdge2(Scene):
    def construct(self):
        square = Square()
        square.generate_target()

        self.add(square)

        square.target.shift(2*UP) # UP
        self.play(MoveToTarget(square))

        square.target.shift(2*LEFT) # UP+LEFT
        self.play(MoveToTarget(square))

        square.target.shift(2*DOWN) # LEFT
        self.play(MoveToTarget(square))

        square.target.shift(2*DOWN) # DOWN+LEFT
        self.play(MoveToTarget(square))

        square.target.shift(2*RIGHT) # DOWN
        self.play(MoveToTarget(square))

        square.target.shift(2*RIGHT) # DOWN+RIGHT
        self.play(MoveToTarget(square))

        square.target.shift(2*UP) # RIGHT
        self.play(MoveToTarget(square))

        square.target.shift(2*UP) # UP+RIGHT
        self.play(MoveToTarget(square))

        square.target.shift(2*LEFT) # UP
        self.play(MoveToTarget(square))

        square.target.shift(2*DOWN) # ORIGIN
        self.play(MoveToTarget(square))

        self.wait()

class PlayToEdge3(Scene):
    def construct(self):
        square = Square()
        text = Text('Hello world!')

        text.to_edge(UP)
        square.next_to(text,DOWN)

        g = Group(text,square)
        g.generate_target()
        self.add(g)
        self.wait(3)

        g.target.shift(DOWN*2)
        self.play(MoveToTarget(g))
        self.wait(3)

        g.target.rotate(PI/4)
        self.play(MoveToTarget(g))
        self.wait(3)

        text.set_color(RED_D)
        square.set_color(GREEN_D)
        self.wait(3)

# https://editor.codecogs.com/
# https://www.latexlive.com/
class ArrayExample(Scene):
    def construct(self):
        text1 = Text('Hello world!').shift(UP*2)
        text1[0].set_color(RED)
        text2 = Text('Hello').next_to(text1,DOWN)
        text2[0].set_color(GREEN)
        self.play(Write(text1),Write(text2))

class TMathexExample1(Scene):
    def construct(self):
        tex3 = MathTex(r'{x}^{2}-\left|x\right| y + {y}^{2} = 4').shift(UP*2)
        tex4 = MathTex(r"{sin}^{2}(x)+{cos}^{2}(x)",r"=1").next_to(tex3,DOWN)
        tex5 = MathTex(r"W(s)=\int \vec{F}(s)\cdot d\vec{s}").next_to(tex4,DOWN)
        self.play(Write(tex3),Write(tex4),Write(tex5))

class TMathexExample2(Scene):
    def construct(self):
        tex = MathTex(r"{sin}^{2}(x)+{cos}^{2}(x)",r"=1")
        bi = Brace(tex[0],UP)
        ti = bi.get_text("Function")

        box = SurroundingRectangle(tex[0])
        box.set_stroke(GREEN,9)

        cross = Cross(tex[0])
        cross.set_stroke(RED,3)
        
        # self.play(Write(tex),Write(bi),Write(ti))

        # formula = Group(tex,bi,ti)
        self.play(Write(tex),Write(bi),Write(ti),Write(box),Write(cross),run_time=5)