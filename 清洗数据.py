import pandas as pd
import matplotlib.pyplot as plt

date_time = ['comment','date']
df = pd.read_csv('comment.txt',header=None,sep='|',names=date_time,encoding='utf-8')
# 转换日期格式，补零等
df['date'] = pd.to_datetime(df['date'])
# print(df['date'].value_counts())
# date3 = df['2017-11-07':'2017-11-13']
# print(date3)
df.to_csv('comment1.txt',encoding='utf-8',index=False)
print(df.size)
