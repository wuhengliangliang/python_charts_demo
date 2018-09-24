import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("./data/qb_data.csv")  # 读取excell的文件
# sns.set_style(style="whitegrid")  #背景的样式
# sns.set_context(context="poster",font_scale=0.8)
lbs=df["Age"].value_counts().index   # 这是修饰加上各个形状的分类
explodes=[0.1 if i ==38 else 0 for i in lbs]      #  如果想要着重强调某个部位就是把它分离开...



#    这里面我强调的是38的部分
plt.pie(df["Age"].value_counts(normalize=True),explode=explodes,labels=lbs,autopct="%1.1f%%")   #  autopct="%1.1f%%  添加百分比,colors=sns.color_palette("Reds") 指定颜色样式
plt.show()