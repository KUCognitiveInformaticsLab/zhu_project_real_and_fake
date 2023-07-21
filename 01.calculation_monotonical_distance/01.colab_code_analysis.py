import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
names = ["natural*0"+str(i) for i in range(1,10)] + ["unnatural*0"+str(j) for j in range(1,10)]
labels = ["N*0"+str(i) for i in range(1,10)] + ["U*0"+str(j) for j in range(1,10)]
xticks = [0.01*i for i in range(1,200)]
for model in ["MSE", "SSIM", "NLPD", "MS_SSIM", "LPIPS", "DISTS"]:
  filename = "mono_swirl_"+model+"_distance.csv"
  data = pd.read_csv(filename)
  df =  pd.DataFrame(data)
  if model=="SSIM" or model=="MS_SSIM":
    ylabel = "1-"+model
  else:
    ylabel = model
  plt.figure(figsize=(8,6))
  for i in range(18):
    nums = df[names[i]].tolist()
    plt.plot(xticks,nums)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel(ylabel+" distance",fontsize=20)
    plt.xlabel("swirl distortion intensity",fontsize=20)
    # plt.legend(labels)

  plt.savefig("mono/mono_swirl_"+model.lower()+".png")
  plt.show()
