import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#画图函数
def draw_corr(df):
    dfData = df.corr()
    # 设置画面大小
    f, ax = plt.subplots(figsize=(20, 20)) 
    #cmap选择颜色映射，这里让1为蓝色，-1为红色
    sns.heatmap(dfData,cmap="RdBu",linewidths=0.05,vmax=1, vmin=-1 ,annot=True,annot_kws={'size':10,'weight':'bold'})
    #将X轴label移到上方显示，方便查看
    ax.xaxis.tick_top() 
    #将y轴label旋转，方便查看
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    plt.savefig('./Relation.png',bbox_inches='tight')
    plt.show()

#此处为待分析文件路径
path = r"C:\Users\dc-develop-1\Desktop\BAK\DataAnalysis\data.csv"
df = pd.read_csv(path)

#获取各个变量的列名
col = list(df.columns)
#查看列名是否正确
print(col)
    
df1 = df[col]   
draw_corr(df1) #相关系数可视化