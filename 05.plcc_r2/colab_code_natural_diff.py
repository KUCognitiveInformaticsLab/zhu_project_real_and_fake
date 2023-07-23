from scipy.stats import pearsonr, spearmanr, kendalltau
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import sem

# arr1 = np.array(num1)
# arr2 = np.array(num2)
# sst = np.sum((arr1-np.mean(arr1))**2)
# ssr = np.sum((arr1-arr2)**2)
# print(1-(ssr/sst))
# 
# print(r2_score(arr1,arr2))

models = ["HUMAN","MSE","SSIM","MS_SSIM","NLPD","LPIPS","DISTS"]
step = "_0.005"
bar_plcc = [[] for i in range(3)]
bar_plcc_err = [[] for i in range(3)]
bar_srcc = [[] for i in range(3)]
bar_srcc_err = [[] for i in range(3)]
bar_krcc = [[] for i in range(3)]
bar_krcc_err = [[] for i in range(3)]
for model in models:
  filename = "total_analysis_normalize.csv"
  if model != "HUMAN":
    filename2 = "stepPredict/"+model+step+"_predict.csv"
    data2 = pd.read_csv(filename2)
    df2 =  pd.DataFrame(data2)

  data = pd.read_csv(filename)
  df =  pd.DataFrame(data)

  plccs = []
  srccs = []
  krccs = []
  r2s = []

  for subject in range(14):
    num1 = df.iloc[subject][1:].tolist()

    if model=="HUMAN":
      num2 = [0 for i in range(54)]
      for human in range(14):
        if human==subject:
          continue
        values = df.iloc[human][1:].tolist()
        for k in range(54):
          num2[k] += values[k]

      num2 = [each/13 for each in num2]
    else:
      num2 = df2.iloc[14][1:].tolist()


    n_num1 = num1[:9]+num1[18:27]+num1[36:45]
    u_num1 = num1[9:18]+num1[27:36]+num1[45:54]
    n_num2 = num2[:9]+num2[18:27]+num2[36:45]
    u_num2 = num2[9:18]+num2[27:36]+num2[45:54]

    num1 = [x-y for x,y in zip(u_num1,n_num1)]
    num2 = [x-y for x,y in zip(u_num2,n_num2)]


    # #swirl
    # num1 = num1[:9]
    # num2 = num2[:9]



    # # blur
    # num1 = num1[18:36]
    # num2 = num2[18:36]



    # # #noise
    # num1 = num1[36:]
    # num2 = num2[36:]


    # n_num1 = num1[:9]
    # u_num1 = num1[9:18]
    # n_num2 = num2[:9]
    # u_num2 = num2[9:18]


    r2 = r2_score(num1,num2)
    plcc,_ = pearsonr(num1,num2)
    srcc,_ = spearmanr(num1,num2)
    krcc,_ = kendalltau(num1,num2)
    plccs.append(plcc)
    srccs.append(srcc)
    krccs.append(krcc)
    r2s.append(r2)



  plcc = np.mean(plccs)
  plcc_err = sem(plccs)
  srcc = np.mean(srccs)
  srcc_err = sem(srccs)
  krcc = np.mean(krccs)
  krcc_err = sem(krccs)
  r2 = np.mean(r2s)
  r2_err = sem(r2s)

  if model=="SSIM" or model=="MS_SSIM":
    model = "1-"+model
  if model=="1-MS_SSIM":
    model = "1-MS\\_SSIM"

  bar_plcc[0].append(plcc)
  bar_plcc_err[0].append(plcc_err)


  bar_srcc[0].append(srcc)
  bar_srcc_err[0].append(srcc_err)
 

  bar_krcc[0].append(krcc)
  bar_krcc_err[0].append(krcc_err)





  print( model+"&"+str(round(plcc,4))+"&"+str(round(srcc,4))+"&"+str(round(krcc,4))+"&"+str(round(r2,2))+"$\pm$"+str(round(r2_err,2))+"\\\\")

