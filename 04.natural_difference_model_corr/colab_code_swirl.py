import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# for model in ["MSE", "SSIM", "NLPD", "MS_SSIM", "LPIPS", "DISTS"]:
#   os.mkdir("na_"+model.lower()+"_fig")

filename = "total_analysis_normalize.csv"

for model in ["MSE", "SSIM", "NLPD", "MS_SSIM", "LPIPS", "DISTS"]:

  filename2 = "stepPredict/"+model+"_0.005_predict.csv"
  data2 = pd.read_csv(filename2)
  data = pd.read_csv(filename)
  df =  pd.DataFrame(data)
  df2 =  pd.DataFrame(data2)
  # df = df.transpose()
  for subject in range(14):
    num1 = df.iloc[subject][1:].tolist()
    num2 = df2.iloc[subject][1:].tolist()

    # num2 = [0 for i in range(54)]
    # for human in range(14):
    #   if human==subject:
    #     continue
    #   values = df.iloc[human][1:].tolist()
    #   for k in range(54):
    #     num2[k] += values[k]
    # num2 = [each/13 for each in num2]

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

    x = x[:9] 
    y = y[:9] 
    legends = ["swirl"]
    # legends = ["blur"]
    # legends = ["noise"]

 




    # 绘制散点图
    sns.scatterplot(x=x, y=y,s=100)
    top = max(x+y)+0.01
    bottom = min(x+y)-0.01

    plt.plot([bottom, top], [bottom, top], color='gray', linestyle='--')

    # 显示图例
    plt.legend(legends,fontsize=15)
    title = "0"+str(subject+1) if subject<9 else str(subject+1)
    plt.title('Total: Subject-'+title,fontsize=20)
    plt.xlabel("human JND difference",fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    model_small = model.lower()
    label = model
    if model=="SSIM" or model=="MS_SSIM":
      label = "1-"+model
    plt.ylabel(label+" predicted JND difference",fontsize=15)

    plt.savefig("na_"+model_small+"_fig/"+str(subject)+"_"+model_small+"_corr_swirl.png")
    plt.show()
    # print(nums)
