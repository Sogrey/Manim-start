from manim import *
from manim_cad_drawing_utils import *
from manim_fonts import *
from manim_fontawesome import *

# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

# config.background_color = WHITE
from contextlib import contextmanager
import manimpango

@contextmanager
def RegisterFont():
    pth = "C:/Windows/Fonts/comicz.ttf"
    # "C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/ZiXinFangMingKeBen.ttf"
    # "C:/Windows/Fonts/Inkfree.ttf"
    # "C:/Windows/Fonts/svgasys.fon"
    # "C:/Windows/Fonts/方正粗黑宋简体.ttf" # download_fonts(font_family)
    orig_font = manimpango.list_fonts()

    if not manimpango.register_font(str(pth)):
        print ("Could not register font for font family '" + pth + "'. Cannot    continue.")
    new_font = manimpango.list_fonts()
    print(new_font)
    print(orig_font)
    fonts_names = list(set(new_font) - set(orig_font))
    print("Found fonts %s", fonts_names)

    fonts_names = ['comicz']
    if fonts_names == []:
        print("No fonts registered")

    try:
        yield fonts_names
    finally:
        manimpango.unregister_font(str(pth))

class TestFont(Scene):
    def construct(self):
        # RegisterFont()
        a=Text("字心坊明刻本（古籍版）",font='字心坊明刻本（古籍版）')
        # a=Text("Candara",font='Comic Sans MS')
        self.play(Write(a))
        with RegisterFont() as fonts:
            print(fonts)
            # a=Text("ABCDEFGHIJKLMNOPQRSTUVWXYZ",font='comicz')
            # self.play(Write(a))
        self.wait(30)

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

class ExampleTextFont(Scene):
    def construct(self):
        with RegisterFont("Poppins") as fonts:
            a=Text("Hello World",font=fonts[0])
            self.play(Write(a))

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


def FamousVerses(self, verse, author):
    tex_verse = Tex(verse).scale(1)
    # tex_author = Tex(author).scale(0.5)
    self.play(FadeIn(tex_verse, shift=DOWN, scale=0.66))
    # self.play(FadeIn(tex_author, shift=DOWN*4, scale=0.66))
    self.wait(3)
    self.play(FadeOut(tex_verse, shift=DOWN * 2, scale=1.5))
    # self.play(FadeOut(tex_author, shift=DOWN * 5, scale=1.5))


class ShowLogo(Scene):
    def construct(self):
        Title(self, "The logo of the manim")

        Logo(self)

        Credits(self)


class ShowFamousVerses(Scene):
    def construct(self):
        Title(self, "The logo of the manim")

        datas = [
            "Better late than never.|迟做总比不做好。",
            "Whatever is worth doing at all is worth doing well.|凡是值得做的事，就值得做好。",
            "The shortest answer is doing the thing.|最简短的回答就是一个“干”字。",
            "Action is the proper fruit of knowledge.|行动是知识之佳果。",
            "It is lost labour to sow where there is no soil.|没有土壤，播种也是徒劳。",
            "It is right to put everything in its proper use.|凡事都应用得其所。",
            "Affairs that are done by due degrees are soon ended.|按部就班，事情很快就做完。",
            "All work and no play makes Jack a dull boy.|只工作，不玩耍，聪明小孩也变傻。",
            # '掬水月在手，弄花香满衣。|于良史《春山夜月》',
            # '最是人间留不住，朱颜辞镜花辞树。|王国维《蝶恋花》',
            # '梨花院落溶溶月，柳絮池塘淡淡风。|晏殊《无题·油壁香车不再逢》',
            # '被酒莫惊春睡重，赌书消得泼茶香。当时只道是寻常。|纳兰性德《浣溪沙》',
            # '春水碧于天，画船听雨眠。|韦庄《菩萨蛮·人人尽说江南好》',
            # '无言独上西楼，月如钩，寂寞梧桐深院锁清秋。|李煜《相见欢二首》',
            # '长沟流月去无声。杏花疏影里，吹笛到天明|陈与义《临江仙》','曾伴浮云归晚翠，犹陪落日泛秋声。世间无限丹青手，一片伤心画不成。|高蟾《金陵晚望》','疏影横斜水清浅，暗香浮动月黄昏|林逋《山园小梅》',
            # '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。|王维《鸟鸣涧》'
            ]

        for item in datas:
            print(item)
            data = item.split("|")
            FamousVerses(self,data[0],'')        

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
