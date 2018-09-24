import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("./data/qb_data.csv")  # 读取excell的文件
sns.set_style(style="whitegrid")  #背景的样式
sns.set_context(context="poster",font_scale=0.8)  # context="poster" 文字的格式，font_scale=0.8 字体的大小
sns.boxplot(x=df["Age"],saturation=0.75,whis=3) # saturation方框的边界   whis上分位数的几倍是他的间距
plt.show()