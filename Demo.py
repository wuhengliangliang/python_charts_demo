import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("./data/qb_data.csv")
le_s=df["Year"]
# print(le_s.median)
sns.set_style(style="ticks")  #修改形状
sns.set_context(context="paper",font_scale=1.0)
sns.set_palette(sns.color_palette("muted"))  # "husl", 8 粉红颜色设置  "muted" 深蓝 RdBu", n_colors=7 红色
print(type("TD"))
print(type("Age"))
#sns.countplot(x="TD",hue="Age",data=df.head(150))  # 直接调用seaborn库绘制柱状图
sns.set_style('whitegrid')
sns.violinplot(x="Age",y="TD",data=df)
# plt.title("TD")
# plt.xlabel("td")
# plt.ylabel("Number")
# plt.xticks(np.arange(len(df["TD"].value_counts()))+0.5,df["TD"].value_counts().index)
# plt.axis([0,40,0,50])
# plt.bar(np.arange(len(df["TD"].value_counts()))+0.5,df["TD"].value_counts(),width=0.5)
# for x,y in zip(np.arange(len(df["TD"].value_counts()))+0.5,df["TD"].value_counts()):
#     plt.text(x,y,y,ha="center",va="bottom")  #调节水平和垂直的位置
# plt.savefig('TD.png')  #保存图片
plt.show()
print("__________________"*20)
print(le_s.value_counts())
# print(le_s.skew())
# print("__________________"*20)
# print(le_s.kurt())
# print("__________________"*20)
# print(le_s.values)