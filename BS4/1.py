from spider.BS4 import Html_data
from bs4 import BeautifulSoup

data = Html_data.html_doc
soup = BeautifulSoup(data,'html.parser')
# 格式化文档
# print(soup.prettify())
# 获取文本
# print(soup.get_text())
# 获得文档标签title
print(soup.title)
# 获得文档head下的title标签
print(soup.head.title)
# 获得标签p的class属性值
print(soup.p['class'])
# 获得所有网址属性值
for link in soup.find_all('a'):
    # print(link['href'])
    print(link.get('href'))
# 获得a标签第一个
print(soup.a)
# 获得所有a标签,并返回列表
print(soup.find_all('a'))
# 获得所有a标签或p标签，返回列表
print(soup.find_all(['a','p']))
# 获得下一个直接子节点标签，并返回列表
print(soup.p)
print(soup.p.contents[0])
print('-'*30)
# 获得下一个直接子节点生成器
for chil in soup.p.b.children:
    print(chil)
print('-'*30)
# 获得(第一个)下一个所有子孙节点生成器
for des in soup.p.descendants:
    print(des)
print('-'*30)
# 获得b标签的父标签p
print(soup.p.b.parent)
for parent in soup.p.b.parents:
    print(parent.name)
print('-'*30)
print(soup.a.previous_sibling)
print(soup.a.next_sibling)