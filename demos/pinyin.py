from manim import *
# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

# http://du.hanyupinyin.cn/


class showPinyin_shengmu(Scene):
    def construct(self):
        # BackgroundImage(self, '../assets/bg01.jpg')
        Title(self, "汉语拼音 -- 声母表")

        g = Group()

        y = 3.0
        xMin = -5.0
        xMax = 5.0
        z = 0.0
        c = BLUE_B
        for i in range(16):
            y -= 0.3
            if i == 4 or i == 8 or i == 12:
                y -= 0.2

            if i == 2 or i == 6 or i == 10 or i == 14:
                c = YELLOW_B
            else:
                c = BLUE_B

            g.add(Line([xMin, y, z], [xMax, y, z], color=c))

        for shape in g:
            self.play(Create(shape), run_time=0.1)

# 声母：23个,分别是：b p m f d t n l g k h j q x zh ch sh r z c s y w 。

        # text1 = Text('b p m f d t n l g k h j q x zh ch sh r z c s y w')
        # self.play(Create(text1), run_time=5)

        scale = 0.77
        datas = {
            'b': [-4.0, 2.3, 0],
            'p': [-3.0, 2.17, 0],
            'm': [-2.0, 2.25, 0],
            'f': [-1.0, 2.3, 0],

            'd': [1.0, 2.3, 0],
            't': [2.0, 2.27, 0],
            'n': [3.0, 2.25, 0],
            'l': [4.0, 2.3, 0],

            'g': [-3.0, 0.8, 0],
            'k': [-2.0, 0.9, 0],
            'h': [-1.0, 0.9, 0],

            'j': [1.0, 0.83, 0],
            'q': [2.0, 0.80, 0],
            'x': [3.0, 0.85, 0],

            'zh': [-3.0, -0.49, 0],
            'ch': [-2.0, -0.49, 0],
            'sh': [-1.0, -0.49, 0],

            'r': [0.0, -0.55, 0],

            'z': [1.0, -0.55, 0],
            'c': [2.0, -0.55, 0],
            's': [3.0, -0.55, 0],

            'y': [-1.0, -2.05, 0],
            'w': [1.0, -1.95, 0],
        }

        for shengmu in datas:
            position = datas[shengmu]

            text = Text(shengmu, font='汉语拼音', weight=BOLD)
            text.generate_target()
            text.target.shift(position).scale(scale)

            self.add(text)
            self.add_sound('../assets/pinyin/shengmu/'+shengmu+'.mp3')
            self.wait()
            self.play(MoveToTarget(text))

        self.wait(3)

        Credits(self)

class testShenyin(Scene):
    def construct(self):

        text = Text("B b (玻)")

        self.add_sound('../assets/pinyin/shengmu/b.wav')
        self.add(text)
        self.wait()
