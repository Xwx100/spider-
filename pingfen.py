#coding=utf-8
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import re
# def paint():
#     font = FontProperties(family='./shouzhangti.ttf',size=14)
#
#     plt.figure(1)
#     plt.subplot(111)
#     plt.ylabel()
#     plt.xlabel()
#     plt.bar(x,y,width=)
def str_to_f(list):
    new_list=[]
    for num in list:
        new_list.append(float(num))
    return new_list

def paint(x,y,title):
    font = FontProperties(fname='./shouzhangti.ttf', size=15)
    x = x
    y = y
    plt.figure(1)
    plt.subplot(111)
    plt.title('豆瓣评分:%s' % (title), fontproperties=font, size=20)
    plt.ylabel('百分比', fontproperties=font)
    plt.xlabel('几星', fontproperties=font)
    plt.bar(x, y, width=0.5)
    for xx, yy in zip(x, y):
        plt.text(xx, yy + 0.1, str(yy) + '%', ha='center')
    plt.savefig('5.jpg')

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    title_list = soup.select('strong[class]')
    table_list = soup.select('.ratings-on-weight')
    return title_list,table_list

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Connection': 'keep-alive',
    }
    cookies = {
        'Cookie': 'bid=rctQScTLVMA; ll="118348"; gr_user_id=6c71a127-3bd0-47fa-be3c-e6caab33acb1; ct=y; _vwo_uuid_v2=A62EF3E7D004072DB2D66B7ADB4A5560|425340eb88876d8be4e9a19d9b022962; ap=1; __utmz=30149280.1513694723.7.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513739315%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1321141265.1512545757.1513694723.1513739316.8; __utmc=30149280; __utmt=1; __utmb=30149280.3.10.1513739316; dbcl2="171313007:xravADDaUx4"; ck=tGCW; _pk_id.100001.4cf6=07602e95ac6508e6.1512545757.6.1513739458.1513695474.; __utma=223695111.1550008486.1512545757.1513694724.1513739458.6; __utmb=223695111.0.10.1513739458; __utmc=223695111; __utmz=223695111.1513739458.6.5.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/phone/bind; __ads_session=dbITv4LIBQkWcbwD9QA='
    }
    html = requests.get(url,cookies=cookies,headers=headers).content
    return html

if __name__ == '__main__':
    html = get_html('https://movie.douban.com/subject/26665065/?tag=%E7%83%AD%E9%97%A8&from=gaia_video')

    title_list,table_list = get_data(html)
    # print(title_list,table_list)
    for t in title_list:
        title = t.get_text().strip()
    for s in table_list:
        table = s.get_text().strip().replace('\n','').replace(' ','')

        pattern1 = re.compile(r'(\d+)星')
        table1 = pattern1.findall(table)
        pattern2 = re.compile(r'(\d+.\d*)%')
        table2 = pattern2.findall(table)
    table1_list = str_to_f(table1)
    table2_list = str_to_f(table2)
    print(table1_list)
    print(table2_list)

    paint(table1_list,table2_list,title)
