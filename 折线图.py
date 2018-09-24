import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("./data/qb_data.csv")  # 读取excell的文件
sns.set_style(style="whitegrid")  #背景的样式
sns.set_context(context="poster",font_scale=0.8)
sub_df=df.groupby("Age").mean()
# sns.pointplot(sub_df.index,sub_df["Year"])
sns.pointplot(x="Age",y="Cmp",data=df)
plt.show()