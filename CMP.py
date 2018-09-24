import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("./data/qb_data.csv")
# le_s=df["Year"]
# print(le_s.median)
sns.set_style(style="ticks")  #修改形状
sns.set_context(context="poster",font_scale=0.35)
plt.title("Cmp") #设置标题
plt.xlabel("td")  # 设置x轴
plt.ylabel("Number")   #设置y轴
plt.xticks(np.arange(len(df["Cmp"].value_counts()))+0.5,df["Cmp"].value_counts().index)
plt.axis([0,100,0,20])
plt.bar(np.arange(len(df["Cmp"].value_counts()))+0.5,df["Cmp"].value_counts(),width=0.5)
for x,y in zip(np.arange(len(df["Cmp"].value_counts()))+0.5,df["Cmp"].value_counts()):
    plt.text(x,y,y,ha="center",va="bottom")  #调节水平和垂直的位置
plt.savefig('CMP2.png')  #保存图片
plt.show()