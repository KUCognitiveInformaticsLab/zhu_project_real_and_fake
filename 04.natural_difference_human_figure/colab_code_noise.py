from re import X
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filename = "total_analysis_normalize.csv"
data = pd.read_csv(filename)
df =  pd.DataFrame(data)
# df = df.transpose()
for subject in range(14):
  num1 = df.iloc[subject][1:].tolist()
  num2 = [0 for i in range(54)]
  for human in range(14):
    if human==subject:
      continue
    values = df.iloc[human][1:].tolist()
    for k in range(54):
      num2[k] += values[k]
  num2 = [each/13 for each in num2]

  # 创建示例数据
  x = num1 # 替换为您的x列数据
  x10 = num1[:9]
  x11= num1[9:18]
  x20=num1[18:27]
  x21 = num1[27:36]
  x30=num1[36:45]
  x31=num1[45:54]
  x = [x2-x1 for x1,x2 in zip(x10,x11)]+[x2-x1 for x1,x2 in zip(x20,x21)]+[x2-x1 for x1,x2 in zip(x30,x31)]

  y = num2  # 替换为您的y列数据
  num1 = num2
  x10 = num1[:9]
  x11= num1[9:18]
  x20=num1[18:27]
  x21 = num1[27:36]
  x30=num1[36:45]
  x31=num1[45:54]
  y = [x2-x1 for x1,x2 in zip(x10,x11)]+[x2-x1 for x1,x2 in zip(x20,x21)]+[x2-x1 for x1,x2 in zip(x30,x31)]


  # 创建示例数据
  x = x[18:27] # 替换为您的x列数据
  y = y[18:27]  # 替换为您的y列数据


  plt.figure(figsize=(8,6))

  # 绘制散点图
  sns.scatterplot(x=x, y=y,s=150)
  top = max(x+y)+0.01
  bottom = min(x+y)-0.01

  plt.plot([bottom, top], [bottom, top], color='gray', linestyle='--')

  # 显示图例
  plt.legend(["noise"],fontsize=20)
  title = "0"+str(subject+1) if subject<9 else str(subject+1)
  plt.title('Total: Subject-'+title,fontsize=20)
  plt.xlabel("human JND difference",fontsize=20)
  plt.xticks(fontsize=15)
  plt.yticks(fontsize=15)
  plt.ylabel("the mean of other subjects' human JND difference",fontsize=15)

  plt.savefig("na_human_fig/na_"+str(subject)+"_human_corr_noise.png")
  plt.show()
  # print(nums)
