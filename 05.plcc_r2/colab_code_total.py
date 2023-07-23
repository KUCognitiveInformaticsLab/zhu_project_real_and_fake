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
  n_plccs = []
  n_srccs = []
  n_krccs = []
  n_r2s = []
  u_plccs = []
  u_srccs = []
  u_krccs = []
  u_r2s = []
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

    # #swirl
    # num1 = num1[:18]
    # num2 = num2[:18]



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


    n_plcc,_ = pearsonr(n_num1,n_num2)
    n_srcc,_ = spearmanr(n_num1,n_num2)
    n_krcc,_ = kendalltau(n_num1,n_num2)
    n_r2 = r2_score(n_num1,n_num2)
    n_plccs.append(n_plcc)
    n_srccs.append(n_srcc)
    n_krccs.append(n_krcc)
    n_r2s.append(n_r2)

    u_plcc,_ = pearsonr(u_num1,u_num2)
    u_srcc,_ = spearmanr(u_num1,u_num2)
    u_krcc,_ = kendalltau(u_num1,u_num2)
    u_r2 = r2_score(u_num1,u_num2)

    u_plccs.append(u_plcc)
    u_srccs.append(u_srcc)
    u_krccs.append(u_krcc)
    u_r2s.append(u_r2)
  plcc = np.mean(plccs)
  plcc_err = sem(plccs)
  srcc = np.mean(srccs)
  srcc_err = sem(srccs)
  krcc = np.mean(krccs)
  krcc_err = sem(krccs)
  r2 = np.mean(r2s)
  r2_err = sem(r2s)

  n_plcc = np.mean(n_plccs)
  n_plcc_err = sem(n_plccs)
  n_srcc = np.mean(n_srccs)
  n_srcc_err = sem(n_srccs)
  n_krcc = np.mean(n_krccs)
  n_krcc_err = sem(n_krccs)
  n_r2 = np.mean(n_r2s)
  n_r2_err = sem(n_r2s)

  u_plcc = np.mean(u_plccs)
  u_plcc_err = sem(u_plccs)
  u_srcc = np.mean(u_srccs)
  u_srcc_err = sem(u_srccs)
  u_krcc = np.mean(u_krccs)
  u_krcc_err = sem(u_krccs)
  u_r2 = np.mean(u_r2s)
  u_r2_err = sem(u_r2s)
  if model=="SSIM" or model=="MS_SSIM":
    model = "1-"+model
  if model=="1-MS_SSIM":
    model = "1-MS\\_SSIM"
  bar_plcc[0].append(plcc)
  bar_plcc[1].append(n_plcc)
  bar_plcc[2].append(u_plcc)
  bar_plcc_err[0].append(plcc_err)
  bar_plcc_err[1].append(n_plcc_err)
  bar_plcc_err[2].append(u_plcc_err)

  bar_srcc[0].append(srcc)
  bar_srcc[1].append(n_srcc)
  bar_srcc[2].append(u_srcc)
  bar_srcc_err[0].append(srcc_err)
  bar_srcc_err[1].append(n_srcc_err)
  bar_srcc_err[2].append(u_srcc_err)

  bar_krcc[0].append(krcc)
  bar_krcc[1].append(n_krcc)
  bar_krcc[2].append(u_krcc)
  bar_krcc_err[0].append(krcc_err)
  bar_krcc_err[1].append(n_krcc_err)
  bar_krcc_err[2].append(u_krcc_err)




  print( model+"&"+str(round(plcc,4))+"&"+str(round(srcc,4))+"&"+str(round(krcc,4))+"&"+str(round(r2,2))+"$\pm$"+str(round(r2_err,2))+ \

  "&"+str(round(n_plcc,4))+"&"+str(round(n_srcc,4))+"&"+str(round(n_krcc,4))+"&"+str(round(n_r2,2))+"$\pm$"+str(round(n_r2_err,2))+ \
  "&"+str(round(u_plcc,4))+"&"+str(round(u_srcc,4))+"&"+str(round(u_krcc,4))+"&"+str(round(u_r2,2))+"$\pm$"+str(round(u_r2_err,2))+"\\\\" \

  )

