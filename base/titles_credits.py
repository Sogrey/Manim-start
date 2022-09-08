from manim import *

def Title(self, title, offsetMultiple=3.5):
    title = Text(title)
    self.add(title)
    self.wait(3)
    self.play(ScaleInPlace(title, 0.5))
    title.generate_target()
    title.target.shift(UL*offsetMultiple)
    self.play(MoveToTarget(title))
    self.wait(2)

def Credits(self, credits=''):
    self.clear()
    if len(credits) == 0:
        credits = "THE END"
    text = Text(credits)
    boundary = AnimatedBoundary(text, colors=[YELLOW], cycle_rate=3)
    self.add(text, boundary)
    self.wait(2)

# manim titles_credits.py -pqm
class TestTitle(Scene):
    def construct(self):
        Title(self, """
The title of the animation
The title
        """,3.5)

        Credits(self)
