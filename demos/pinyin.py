from manim import *
# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *

# http://du.hanyupinyin.cn/

def Line4Space3(self):
    g = Group()

    y = 3.0
    xMin = -6.0
    xMax = 4.0
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

        if i == 0 or i == 3 or i == 4 or i == 7 or i == 8 or i == 11 or i == 12 or i == 15:
            g.add(Line([xMin, y, z], [xMax, y, z], color=c))
        else:
            g.add(DashedLine([xMin, y, z], [xMax, y, z], color=c))

    
    g.add(Line([4.2, 3.0, z], [6.3, 3.0, z], color=BLUE_B))
    g.add(DashedLine([4.2, 2.5, z], [6.3, 2.5, z], color=BLUE_B))
    g.add(DashedLine([4.2, 2.0, z], [6.3, 2.0, z], color=YELLOW_B))
    g.add(Line([4.2, 1.5, z], [6.3, 1.5, z], color=BLUE_B))

    g.add(Line([4.2, 3.0, z], [4.2, 1.5, z], color=BLUE_B))
    g.add(Line([6.3, 3.0, z], [6.3, 1.5, z], color=BLUE_B))
        
    for shape in g:
        self.play(Create(shape), run_time=0.1)

class showPinyin_shengmu(Scene):
    def construct(self):
        # BackgroundImage(self, '../assets/bg01.jpg')
        Title(self, "汉语拼音 -- 声母表")

        Line4Space3(self)

        # 声母：23个,分别是：b p m f d t n l g k h j q x zh ch sh r z c s y w 。

        # text1 = Text('b p m f d t n l g k h j q x zh ch sh r z c s y w')
        # self.play(Create(text1), run_time=5)

        scale0 = 1.4
        scale = 0.55
        datas = {
            'b': [[5.2, 2.4,0],[-5.0, 2.3, 0],'波'],
            'p': [[5.2, 2.1,0],[-4.0, 2.17, 0],'坡'],
            'm': [[5.2, 2.25,0],[-3.0, 2.25, 0],'摸'],
            'f': [[5.2, 2.4,0],[-2.0, 2.3, 0],'佛'],

            'd': [[5.2, 2.4,0],[0.0, 2.3, 0],'得'],
            't': [[5.2, 2.3,0],[1.0, 2.27, 0],'特'],
            'n': [[5.2, 2.25,0],[2.0, 2.25, 0],'讷'],
            'l': [[5.2, 2.4,0],[3.0, 2.3, 0],'勒'],

            'g': [[5.2, 2.1,0],[-4.0, 0.8, 0],'哥'],
            'k': [[5.2, 2.4,0],[-3.0, 0.9, 0],'科'],
            'h': [[5.2, 2.4,0],[-2.0, 0.9, 0],'喝'],

            'j': [[5.2, 2.25,0],[0.0, 0.85, 0],'基'],
            'q': [[5.2, 2.1,0],[1.0, 0.80, 0],'欺'],
            'x': [[5.2, 2.25,0],[2.0, 0.85, 0],'西'],

            'zh': [[5.2, 2.4,0],[-4.0, -0.49, 0],'知'],
            'ch': [[5.2, 2.4,0],[-3.0, -0.49, 0],'吃'],
            'sh': [[5.2, 2.4,0],[-2.0, -0.49, 0],'诗'],

            'r': [[5.2, 2.25,0],[-1.0, -0.55, 0],'日'],

            'z': [[5.2, 2.25,0],[0.0, -0.55, 0],'资'],
            'c': [[5.2, 2.25,0],[1.0, -0.55, 0],'雌'],
            's': [[5.2, 2.25,0],[2.0, -0.55, 0],'思'],

            'y': [[5.2, 2.1,0],[-2.0, -2.05, 0],'医'],
            'w': [[5.2, 2.25,0],[0.0, -1.95, 0],'物'],
        }

        for shengmu in datas:
            position = datas[shengmu]

            textHanzi = Text(position[2], font='Kai PinYin Big_2', weight=BOLD, color=WHITE).move_to([5.2, -1,0]).scale(3)
            self.add(textHanzi)

            text = Text(shengmu, font='汉语拼音', weight=BOLD, color=RED).move_to(position[0]).scale(scale0)
            text.generate_target()
            # text.target.shift(position[1]).scale(scale)
            text.target.move_to(position[1]).scale(scale)

            self.add(text)
            self.add_sound('../assets/pinyin/shengmu/'+shengmu+'.mp3')
            self.wait()
            self.play(MoveToTarget(text))
            self.remove(textHanzi)

        self.wait(5)

        Credits(self)

class showPinyin_yunmu(Scene):
    def construct(self):
        # BackgroundImage(self, '../assets/bg01.jpg')
        Title(self, "汉语拼音 -- 韵母表")

        Line4Space3(self)
        
        # 声母共有24个,分别a o e i u v ai ei ui ao ou iu ie ve er an en in un vn ang eng ing ong.

        # 韵母共有：24个。 单韵母：a o e i u ü, 复韵母：ai ei ui ao ou iu ie üe, 特殊韵母：er, 鼻韵母：an en in un ün ang eng ing ong, 单韵母6个，复韵母8个，鼻韵母9个，特殊韵母1个。

        # text1 = Text('b p m f d t n l g k h j q x zh ch sh r z c s y w')
        # self.play(Create(text1), run_time=5)

        scale0 = 1.4
        scale = 0.55
        colors = {
            '单韵母': RED,
            '复韵母': YELLOW,
            '特殊韵母': BLUE,
            '鼻韵母': GREEN,
        }
        datas = {
            'a': [[5.2, 2.25,0],[-4.0, 2.25, 0],'啊','单韵母'],
            'o': [[5.2, 2.25,0],[-3.0, 2.25, 0],'喔','单韵母'],
            'e': [[5.2, 2.25,0],[-2.0, 2.25, 0],'鹅','单韵母'],

            'i': [[5.2, 2.35,0],[0.0, 2.3, 0],'衣','单韵母'],
            'u': [[5.2, 2.25,0],[1.0, 2.25, 0],'乌','单韵母'],
            'ü': [[5.2, 2.35,0],[2.0, 2.3, 0],'迂','单韵母'],

            'ai': [[5.2, 2.35,0],[-5.0, 0.9, 0],'哀','复韵母'],
            'ei': [[5.2, 2.35,0],[-4.0, 0.9, 0],'诶','复韵母'],
            'ui': [[5.2, 2.35,0],[-3.0, 0.9, 0],'威','复韵母'],
            'ao': [[5.2, 2.25,0],[-2.0, 0.85, 0],'熬','复韵母'],
            'ou': [[5.2, 2.25,0],[-1.0, 0.85, 0],'欧','复韵母'],
            'iu': [[5.2, 2.35,0],[0.0, 0.9, 0],'优','复韵母'],
            'ie': [[5.2, 2.35,0],[1.0, 0.9, 0],'耶','复韵母'],
            'üe': [[5.2, 2.35,0],[2.0, 0.9, 0],'约','复韵母'],
            'er': [[5.2, 2.25,0],[3.0, 0.85, 0],'耳','特殊韵母'],

            'an': [[5.2, 2.25,0],[-3.0, -0.53, 0],'安','鼻韵母'],
            'en': [[5.2, 2.25,0],[-2.0, -0.53, 0],'恩','鼻韵母'],
            'in': [[5.2, 2.35,0],[-1.0, -0.52, 0],'因','鼻韵母'],
            'un': [[5.2, 2.25,0],[0.0, -0.55, 0],'温','鼻韵母'],
            'ün': [[5.2, 2.35,0],[1.0, -0.52, 0],'晕','鼻韵母'],

            'ang': [[5.2, 2.17,0],[-3.0, -2.0, 0],'昂','鼻韵母'],
            'eng': [[5.2, 2.17,0],[-2.0, -2.0, 0],'享','鼻韵母'],
            'ing': [[5.2, 2.25,0],[0.0, -1.95, 0],'英','鼻韵母'],
            'ong': [[5.2, 2.15,0],[1.0, -2.0, 0],'翁','鼻韵母'],
        }

        for yunmu in datas:
            position = datas[yunmu]

            textType = Text(position[3], color=WHITE).move_to([5.2, 1,0]).scale(0.5)
            self.add(textType)

            textHanzi = Text(position[2], font='Kai PinYin Big_2', weight=BOLD, color=WHITE).move_to([5.2, -1,0]).scale(3)
            self.add(textHanzi)

            text = Text(yunmu, font='汉语拼音', weight=BOLD, color=colors[position[3]]).move_to(position[0]).scale(scale0)
            text.generate_target()
            # text.target.shift(position[1]).scale(scale)
            text.target.move_to(position[1]).scale(scale)

            self.add(text)
            self.add_sound('../assets/pinyin/yunmu/'+yunmu+'.mp3')
            self.wait(3)
            self.play(MoveToTarget(text))
            self.remove(textHanzi)
            self.remove(textType)

        self.wait(2)

        position = 1.0
        for cc in colors:        
            dot = Dot(point=[4.5, position,0], radius=0.2, color=colors[cc])
            textType = Text(cc, color=colors[cc]).move_to([5.5, position,0]).scale(0.5)
            self.add(dot)
            self.add(textType)

            position -= 1.0

        self.wait(5)

        Credits(self)

class showPinyin_zhengtirendu(Scene):
    def construct(self):
        # BackgroundImage(self, '../assets/bg01.jpg')
        Title(self, "汉语拼音 -- 整体认读表")

        Line4Space3(self)

        # 整体认读章节共16个:zhi chi shi ri zi ci si yi wu yu ye yue yuan yin yun ying

        # text1 = Text('b p m f d t n l g k h j q x zh ch sh r z c s y w')
        # self.play(Create(text1), run_time=5)

        scale0 = 1.4
        scale = 0.55
        datas = {
            'zhi': [[5.2, 2.4,0],[-4.0, 2.32, 0],'织'],
            'chi': [[5.2, 2.4,0],[-2.0, 2.32, 0],'吃'],
            'shi': [[5.2, 2.4,0],[0.0, 2.32, 0],'狮'],
            'ri': [[5.2, 2.35,0],[2.0, 2.32, 0],'日'],

            'zi': [[5.2, 2.35,0],[-4.0, 0.9, 0],'资'],
            'ci': [[5.2, 2.35,0],[-2.0, 0.9, 0],'刺'],
            'si': [[5.2, 2.35,0],[0.0, 0.9, 0],'丝'],
            'yi': [[5.2, 2.25,0],[2.0, 0.85, 0],'衣'],

            'wu': [[5.2, 2.25,0],[-4.0, -0.55, 0],'屋'],
            'yu': [[5.2, 2.15,0],[-2.0, -0.6, 0],'雨'],
            'ye': [[5.2, 2.15,0],[0.0, -0.6, 0],'椰'],
            'yue': [[5.2, 2.15,0],[2.0, -0.6, 0],'月'],

            'yuan': [[5.2, 2.15,0],[-4.0, -2.0, 0],'圆'],
            'yin': [[5.2, 2.25,0],[-2.0, -1.98, 0],'印'],
            'yun': [[5.2, 2.15,0],[0.0, -2.0, 0],'云'],
            'ying': [[5.2, 2.2,0],[2.0, -1.98, 0],'鹰'],
        }

        for ztrd in datas:
            position = datas[ztrd]

            textHanzi = Text(position[2], font='Kai PinYin Big_2', weight=BOLD, color=WHITE).move_to([5.2, -1,0]).scale(3)
            self.add(textHanzi)

            text = Text(ztrd, font='汉语拼音', weight=BOLD, color=RED).move_to(position[0]).scale(scale0)
            text.generate_target()
            # text.target.shift(position[1]).scale(scale)
            text.target.move_to(position[1]).scale(scale)

            self.add(text)          
            self.add_sound('../assets/pinyin/zhengtirendu/'+ztrd)
            self.wait()
            self.play(MoveToTarget(text))
            self.remove(textHanzi)

        self.wait(5)

        Credits(self)

class testShenyin(Scene):
    def construct(self):

        text = Text("B b (玻)")

        self.add_sound('../assets/pinyin/shengmu/b.wav')
        self.add(text)
        self.wait()
