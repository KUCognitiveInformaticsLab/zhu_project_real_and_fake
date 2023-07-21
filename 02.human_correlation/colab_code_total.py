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
  y = num2  # 替换为您的y列数据
  c = []
  types = ["swirl-0","swirl-1","blur-0","blur-1","noise-0","noise-1"]
  for k in range(6):
    for i in range(9):
      c.append(types[k])


  categories = c  # 替换为包含类别信息的列

  # categories = types  # 替换为您的类别数据

  # 设置形状和颜色映射
  marker_map = dict(zip(types,["X","X","o","o","s","s"]))
  color_map = dict(zip(types,["darkorange","forestgreen"]*3))
  print(color_map)
  plt.figure(figsize=(8,6))

  # 绘制散点图
  sns.scatterplot(x=x, y=y, hue=categories, style=categories,
                  markers=marker_map, palette=color_map,s=150)
  top = max(x+y)+0.01
  bottom = min(x+y)-0.01

  plt.plot([bottom, top], [bottom, top], color='gray', linestyle='--')

  # 显示图例
  plt.legend(fontsize=15)
  title = "0"+str(subject+1) if subject<9 else str(subject+1)
  plt.title('Total: Subject-'+title,fontsize=20)
  plt.xlabel("human JND",fontsize=20)
  plt.ylabel("the mean of other subjects' human JND",fontsize=15)
  plt.xticks(fontsize=15)
  plt.yticks(fontsize=15)
  plt.savefig("human_fig/"+str(subject)+"_human_corr_total.png")
  plt.show()
  # print(nums)

import os, tarfile

import os
from google.colab import files

def make_targz_one_by_one(output_filename, source_dir):
  tar = tarfile.open(output_filename,"w")
  for root,dir_name,files_list in os.walk(source_dir):
    for file in files_list:
      pathfile = os.path.join(root, file)
      tar.add(pathfile)
  tar.close()

  files.download(output_filename)


make_targz_one_by_one('human_fig_total.tar', './human_fig//')
