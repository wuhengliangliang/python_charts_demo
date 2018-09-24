import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("./data/qb_data.csv")  # 读取excell的文件
sns.set_style(style="whitegrid")  #背景的样式
sns.set_context(context="poster",font_scale=0.8)  # context="poster" 文字的格式，font_scale=0.8 字体的大小
f=plt.figure()
f.add_subplot(1,3,1)  #设置在一个页面上的 1行3列第几个
sns.distplot(df["TD"],bins=30)  #kde=False 如果kde 等于false 那么折线图就没有了，如果 hist等于False 那么直方图就没有了
f.add_subplot(1,3,2)
sns.distplot(df["Age"],bins=30)  
f.add_subplot(1,3,3)
sns.distplot(df["Cmp"],bins=30)
plt.show()