import re
import requests
import time
import random
from bs4 import BeautifulSoup

absolute = 'https://movie.douban.com/subject/26665065/comments'
absolute_url = 'https://movie.douban.com/subject/26665065/comments?start=20&limit=20&sort=new_score&status=P&percent_type='
url = 'https://movie.douban.com/subject/26322642/comments?start=&limit=20&sort=new_score&status=P'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Connection':'keep-alive',
}
cookies = {
    'Cookie':'bid=rctQScTLVMA; ll="118348"; gr_user_id=6c71a127-3bd0-47fa-be3c-e6caab33acb1; ct=y; _vwo_uuid_v2=A62EF3E7D004072DB2D66B7ADB4A5560|425340eb88876d8be4e9a19d9b022962; ap=1; __utmz=30149280.1513694723.7.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513739315%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1321141265.1512545757.1513694723.1513739316.8; __utmc=30149280; __utmt=1; __utmb=30149280.3.10.1513739316; dbcl2="171313007:xravADDaUx4"; ck=tGCW; _pk_id.100001.4cf6=07602e95ac6508e6.1512545757.6.1513739458.1513695474.; __utma=223695111.1550008486.1512545757.1513694724.1513739458.6; __utmb=223695111.0.10.1513739458; __utmc=223695111; __utmz=223695111.1513739458.6.5.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/phone/bind; __ads_session=dbITv4LIBQkWcbwD9QA='
}
def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    comment_list = soup.select('.comment > p')
    next_page = soup.select('#paginator > a')[2].get('href')
    comment_date_list = soup.select('.comment-time')

    return comment_list,next_page,comment_date_list

if __name__ == '__main__':
    html = requests.get(absolute_url,cookies=cookies,headers = headers).content
    comment_list=[]
    # 获取next_page
    comment_list,next_page,comment_date_list = get_data(html)
    print('-'*30)
    # 下一页标签
    while (next_page!=[]):
             print(absolute+next_page)
             html = requests.get(absolute+next_page,cookies=cookies,headers=headers).content
             soup = BeautifulSoup(html,'lxml')
             comment_list,next_page,comment_date_list = get_data(html)
             with open('fengyuchanglin.txt','a',encoding='utf-8') as f:
                 n=0
                 for node in comment_list:
                     comment = node.get_text().replace('\n','')
                     comment_date = comment_date_list[n].get_text().strip()
                     n += 1
                     f.writelines(comment+'|'+comment_date+u'\n')
             time.sleep(1+(random.randint(1,100))/20)