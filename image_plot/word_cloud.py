from wordcloud import WordCloud,ImageColorGenerator
import jieba
from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def draw_wordcloud():
    file_path='c:/users/magfi/desktop'
    file_name = path.join(file_path,'allday.txt')
    # abel_mask = np.array(Image.open(path.join(file_path,"gr3.jpg")))
    with open(file_name) as f:
        my_text = f.read()

    cut_text = ' '.join(jieba.cut(my_text))
    d = path.dirname(__file__)
    print(d)
    # 读取背景图片
    color_mask = imread(path.join(file_path,"gra3.jpg"))

    cloud = WordCloud(
        width=400, height=200,
        # 设置中文字体
        # font_path="HYQiHei-25J.ttf",
        font_path=path.join(d, 'simsun.ttc'),
        # 背景图片
        mask=color_mask,
        # 背景颜色
        background_color='white',
        max_words=300,
        max_font_size=60,
        random_state= 20)
    word_cloud = cloud.generate(cut_text)
    # 根据图片生成词云颜色
    # image_colors = ImageColorGenerator(color_mask)
    # word_cloud.recolor(color_func=image_colors)
    # 输出到jpg
    # word_cloud.to_file(path.join(file_path,'ribao3.jpg'))
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    draw_wordcloud()
