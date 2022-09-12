from manim import *

def Title(self, title):
    title0 = Text(title) # 初态
    title = title0.copy() # 终态
    self.add(title0)
    self.wait(3)
    title.to_corner(UP + LEFT).scale(0.5)
    self.play(Transform(title0, title)) # 过渡动画
    self.wait(2)

def Credits(self, credits=''):
    self.clear()
    if len(credits) == 0:
        credits = "THE END"
    # text = Text(credits).set_color(TEAL_D).scale(1).move_to(DOWN)
    # self.play(FadeIn(text, shift=DOWN, scale=0.66))
    # self.wait(2)
    # self.play(FadeOut(text, shift=DOWN * 2, scale=1.5))

    tex_in = Tex("THE END").scale(1).set_color(TEAL_D)
    tex_out = Tex("@Sogrey").scale(.5).set_color(TEAL_D)
    self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
    self.wait(2)
    self.play(ReplacementTransform(tex_in, tex_out))
    self.wait(2)
    self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

# manim titles_credits.py -pqm
class TestTitle(Scene):
    def construct(self):
        Title(self, """
The title of the animation
The title
        """,3.5)

        Credits(self)
