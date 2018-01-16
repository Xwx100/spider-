import requests
from  bs4 import BeautifulSoup
import random

def get_date(html):
    soup = BeautifulSoup(html,'lxml')
    content_list = soup.select('.content > span')
    contents=[]
    for c in content_list:
        contents.append(c.get_text().replace('\n',''))
    return contents

def get_html(url,headers):
    html = requests.get(url,headers=headers).content
    return html

if __name__ == '__main__':
    us_list = [
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
    ]
    headers = {'User-Agent':random.choice(us_list),
               'Connection': 'keep-alive',}
    while 1:
        html = get_html('https://www.qiushibaike.com/text/page/1/',headers)
        contents = get_date(html)
        print(contents)
        with open('qiushi.txt','w',encoding='utf-8') as f:
            for content in contents:
                content += '\n'
                f.write(content)