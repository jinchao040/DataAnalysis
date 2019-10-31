import pandas as pd
import scipy
from scipy.stats import ttest_ind
import numpy as np
from scipy.stats import levene

path = r"C:\Users\dc-develop-1\Desktop\BAK\JInchao\DataAnalysis\data.csv"
df = pd.read_csv(path)

#需要的变量为X1~X25
var = []        #用来存储自变量
var_nums = 25   #自变量个数
for i in range(var_nums):
    num = "X"+str(i+1)
    var.append(num)

type1 = df[df["TYPE"]==1][var]  #type1的所有数据
type0 = df[df["TYPE"]==0][var]  #type0的所有数据


#检验方差齐性，若P>0.05，我们认为方差相等
#若方差不相等，ttest_ind中要设置equal_var = False
for i in range(var_nums):
    num = "X%s"%(i+1)
    scale_test=levene(df[df["TYPE"]==1][num],df[df["TYPE"]==1][num])
    if scale_test.pvalue<=0.05:
        print("有非齐方差项，注意ttest_ind中设置相关参数！，非齐方差项为",end=":")
        print(num)
    elif i==24:
        print("全部项均为齐方差,ttest_ind中设置equal_var = True")

#两独立样本t检验
#返回结果第一个为t_value，第二个为two-tailed p_value
print("type1 mean:")
print(type1.mean())
print("type0 mean:")
print(type0.mean())
print(ttest_ind(type1,type0,equal_var = True))