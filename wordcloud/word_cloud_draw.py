from os import path
import codecs

from imageio import imread
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pylab as plt

# 加载字体路径
font_path = './font/simhei.TTF'
# 加载图片路径
image_path = 'imagesource/love.jpg'
# 加载分词后文件路径
jieba_result = 'jieba_result.txt'
# 加载不显示文字文件
stop_words = 'stopwords'

def draw_word_cloud(font_path, image_path, jieba_result, stop_words):
    d = path.dirname(__file__)
    image = imread(image_path)
    text = codecs.open(path.join(d, jieba_result), 'rb', encoding='utf-8').read()
    stopwords = STOPWORDS.union(
        set(
            [x.strip() for x in
             open(path.join(path.dirname(__file__), stop_words), encoding='utf-8')
                 .read().split('\n')]
        )
    )



    wordcloud = WordCloud(
        font_path=font_path,
        mask=image,
        stopwords=stopwords,
        background_color='white',
        max_words=2000,
        max_font_size=200).generate(text)
    image_color = ImageColorGenerator(image)

    wordcloud.to_file("wordcloud.jpg")

    # plt.imshow(wordcloud.recolor(color_func=image_color))
    # plt.axis('off')
    # plt.show()

if __name__ == '__main__':
    draw_word_cloud(font_path, image_path, jieba_result, stop_words)
