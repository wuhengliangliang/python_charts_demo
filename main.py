import pandas as pd  # 调用pandas库 来读取excell的文件
import scipy.stats as ss  #生成正太分布的库
import numpy as np
import seaborn as sns
df=pd.read_csv("./data/qb_data.csv")  # 读取excell的文件
# print(df)
# print(df.head(10))  # 得到数据的前十行
# print(type(df))  #求读取的数据的类型
# print(type(df["Name"])) # 求每列行的值的类型
# print(df.mean())  # 求均值
# print(df["Age"].mean())  #求指定的每一列的均值
# print(df["Cmp"].median)   # 求指定的这一列的中位数
# print("求Att的分位数是：",df["Att"].quantile(q=0.5)) # 求分位数
# print(df.quantile(q=0.5)) # 求分位数
# print(df.mode())
# print("Age的众数:",df["Age"].mode()) #求众数
# print("Age的标准差:",df["Age"].std()) # 求标准差
# print("Age的方差:",df["Age"].var()) #求方差
# print("Age的和:",df["Age"].sum())   #求和
# print("Age的偏态系数:",df["Age"].skew())   #求偏态系数
# print("Age的和:",df["Age"].kurt())   #求峰态系数
# print(ss.norm)
# print("Age的正态分布:",ss.norm.stats(moments="mvsk"))   #求正态分布
# print(ss.norm.pdf(0.0)) #分布函数在0上面的值
# print(ss.norm.ppf(0.9))   #累计值
# print(ss.norm.cdf(2))  #从负无穷到2的累计概率是多少
# print(ss.norm.cdf(2)-ss.norm.cdf(-2))
# print(ss.norm.rvs(size=10))  # 10个符合正态分布的数字
# print(df["Age"].sample(10)) # 对其中的一列进行十个抽样
sns.set_style(style="ticks")
sns.set_context(context="poster",font_scale=0.5)
sns.countplot(x="Age",data=df)  # 直接调用seaborn库绘制柱状图
sl_s=df["TD"]
print(sl_s.isnull())  #判断是否有异常值
print(sl_s[sl_s.isnull()])
print(df[df["TD"].isnull()])
sl_s=sl_s.dropna()
print(sl_s.min())
print(sl_s.median())
print(sl_s.quantile(q=0.25))
print(sl_s.quantile(q=0.75))
import seaborn as sns
import matplotlib.pyplot as plt
plt.title("Age")
plt.xlabel("age")
plt.ylabel("Number")
plt.bar(np.arange(len(df["Age"].value_counts()))+0.5,df["Age"].value_counts())
plt.xticks(np.arange(len(df["Age"].value_counts()))+0.5,df["Age"].value_counts().index)
for x,y in zip(np.arange(len(df["Age"].value_counts()))+0.5,df["Age"].value_counts()):
    plt.text(x,y,y,ha="center",va="bottom")
plt.savefig('Age.png')  #保存图片
plt.show()
print("这是Cmp")
plt.title("Cmp")
plt.xlabel("cmp")
plt.ylabel("Number")
plt.xticks(np.arange(len(df["Cmp"].value_counts()))+0.5,df["Cmp"].value_counts().index)
plt.bar(np.arange(len(df["Cmp"].value_counts()))+0.5,df["Cmp"].value_counts(),width=0.5)
plt.axis([0,20,0,40])
for x,y in zip(np.arange(len(df["Cmp"].value_counts()))+0.5,df["Cmp"].value_counts()):
    plt.text(x,y,y,ha="center",va="bottom")
plt.savefig('Cmp.png')  #保存图片
plt.show()
print("这是TD")
plt.title("TD")
plt.xlabel("td")
plt.ylabel("Number")
# sns.set_style(style="whitegrid")
# sns.set_context(context="postor",font_scale=0.05)
plt.xticks(np.arange(len(df["TD"].value_counts()))+0.5,df["TD"].value_counts().index)
# plt.axis([0,20,0,30])
plt.bar(np.arange(len(df["TD"].value_counts()))+0.5,df["TD"].value_counts(),width=0.5)
for x,y in zip(np.arange(len(df["TD"].value_counts()))+0.5,df["TD"].value_counts()):
    plt.text(x,y,y,ha="center",va="bottom")
plt.savefig('TD.png')  #保存图片
plt.show()
print("——————————————————"*20)
print(np.histogram(sl_s.values,bins=np.arange(20,50,100)))
