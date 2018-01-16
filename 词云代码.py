import pickle
from os import path
import  jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

def make_worldCloud(word_in_path,img_in_path,name_out):
    # 生成字符串
    text_from_file_with_apath = open(word_in_path,'r',encoding='utf-8').read()
    # 构成生成器
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath,cut_all=False)
    print('文字生成成功')
    # 列表成分都以空格隔开
    w1_space_split =' '.join(wordlist_after_jieba)
    # 加载图片，生成图片对象
    backgroud_Image = plt.imread(img_in_path)
    print('图片加载成功')
    '''设置词云样式'''
    # 设置阻止词
    stopwords = STOPWORDS.copy()
    stopwords.add('哈哈')
    stopwords.add('还是')
    # 生成词云图
    wc = WordCloud(
        # 有中文，此项要选，字体自行下载
        font_path='./shouzhangti.ttf',
        background_color='white',
        mask=backgroud_Image,
        max_words=700,
        stopwords=stopwords,
        max_font_size=100,
        random_state=50,
    )
    wc.generate_from_text(w1_space_split)
    # 图片字体颜色生成器，alpha
    img_colors = ImageColorGenerator(backgroud_Image)
    # 颜色生效
    wc.recolor(color_func=img_colors)
    plt.imshow(wc)
    plt.show()
    # 打印到文件所处目录
    d = path.dirname(__file__)
    wc.to_file(path.join(d,name_out))
    print('生成词云成功')

make_worldCloud('./fengyu.txt','./3.jpg','4.jpg')