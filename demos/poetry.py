from manim import *
# 导入base目录下基础工具函数
import sys
sys.path.append('../base/')
from titles_credits import *
# from manim_fonts import *

# from contextlib import contextmanager
import manimpango

# @contextmanager
# def RegisterFont():
#     pth = "C:/Windows/Fonts/comicz.ttf"
#     # "C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/ZiXinFangMingKeBen.ttf"
#     # "C:/Windows/Fonts/Inkfree.ttf"
#     # "C:/Windows/Fonts/svgasys.fon"
#     # "C:/Windows/Fonts/方正粗黑宋简体.ttf" # download_fonts(font_family)
#     orig_font = manimpango.list_fonts()

#     if not manimpango.register_font(str(pth)):
#         print ("Could not register font for font family '" + pth + "'. Cannot    continue.")
#     new_font = manimpango.list_fonts()
#     print(new_font)
#     print(orig_font)
#     fonts_names = list(set(new_font) - set(orig_font))
#     print("Found fonts %s", fonts_names)

#     fonts_names = ['comicz']
#     if fonts_names == []:
#         print("No fonts registered")

#     try:
#         yield fonts_names
#     finally:
#         manimpango.unregister_font(str(pth))

class TestFont(Scene):
    def construct(self):
        fonts = manimpango.list_fonts()
        print(fonts)

        a=Text("中国智造 惠及全球",font='QIJIC') # 令东齐伋复刻体
        self.play(Write(a))
        self.wait(5)
        self.clear()
        # a=Text("下面是由出国留学网小编为大家整理",font='I.Ngaan') # 刻石录颜体字体  缺字严重
        # self.play(Write(a))
        # self.wait(5)
        # self.clear()
        a=Text("鸿雷行书简体",font='hongleixingshu') # 鸿雷行书简体        
        self.play(Write(a))
        self.wait(5)
        self.clear()
        # a=Text("刻石录钢笔鹤体字体",font='I-PenCrane-B') # 刻石录钢笔鹤体字体        
        # self.play(Write(a))
        # self.wait(5)
        # self.clear()
        a=Text("字心坊明刻本（古籍版）",font='字心坊明刻本（古籍版）') # 字心坊明刻本（古籍版）        
        self.play(Write(a))
        self.wait(10)
        self.clear()

def FamousVerses(self, verse, author):
    textVerse=Text(verse,font='字心坊明刻本（古籍版）') # 令东齐伋复刻体
    textAuthor=Text(author,font='hongleixingshu').scale(0.7).next_to(textVerse, DOWN*2) # 鸿雷行书简体

    group = Group(textVerse, textAuthor)

    self.add(group)
    self.wait(5)
    self.remove(group)

class ShowFamousVerses(Scene):
    def construct(self):
        BackgroundImage(self, '../assets/bg01.jpg')
        Title(self, "10首古典诗词里的名句，每一句都写得极美")

        datas = [
            '掬水月在手，弄花香满衣。|于良史《春山夜月》',
            '最是人间留不住，朱颜辞镜花辞树。|王国维《蝶恋花》',
            '梨花院落溶溶月，柳絮池塘淡淡风。|晏殊《无题·油壁香车不再逢》',
            '被酒莫惊春睡重，赌书消得泼茶香。\n当时只道是寻常。|纳兰性德《浣溪沙》',
            '春水碧于天，画船听雨眠。|韦庄《菩萨蛮·人人尽说江南好》',
            '无言独上西楼，月如钩，\n寂寞梧桐深院锁清秋。|李煜《相见欢二首》',
            '长沟流月去无声。\n杏花疏影里，吹笛到天明|陈与义《临江仙》',
            '曾伴浮云归晚翠，犹陪落日泛秋声。\n世间无限丹青手，一片伤心画不成。|高蟾《金陵晚望》',
            '疏影横斜水清浅，暗香浮动月黄昏|林逋《山园小梅》',
            '人闲桂花落，夜静春山空。\n月出惊山鸟，时鸣春涧中。|王维《鸟鸣涧》'
        ]

        for item in datas:
            print(item)
            data = item.split("|")
            FamousVerses(self,data[0],data[1])        

        Credits(self)