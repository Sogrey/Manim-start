from manim import *

# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

# manim titles_credits.py -pqm
class TestTitle(Scene):
    def construct(self):
        Title(self, "The title of the animation")

        Credits(self)
