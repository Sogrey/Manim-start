from manim import *
import sys
sys.path.append('../base/')
from titles_credits import *

# manim titles_credits.py -pqm
class TestTitle(Scene):
    def construct(self):
        Title(self, """
The title of the animation
The title
        """,3.5)

        Credits(self)
