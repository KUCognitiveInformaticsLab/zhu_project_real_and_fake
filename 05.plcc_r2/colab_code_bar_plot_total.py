import seaborn as sns
import matplotlib.pyplot as plt
# for index,model in zip(range(3),["Total","Natural","Unnatural"]):
#   xlabels = ["HUMAN","MSE","SSIM","MS_SSIM","NLPD","LPIPS","DISTS"]
#   plt.bar(xlabels,bar_values[index],color=["darkorange","forestgreen","forestgreen","forestgreen","forestgreen","forestgreen","forestgreen"],width=0.5)
#   plt.ylim(0,1)
#   plt.ylabel("PLCC",fontsize=20)
#   plt.title(model,fontsize=20)
#   plt.xticks(fontsize=13)#
#   plt.yticks(fontsize=15)
#   plt.savefig("01_model_corr_"+model.lower()+".png")
#   plt.show()


for i in range(3):

  if i==0:
    bar = bar_plcc
    bar_err = bar_plcc_err
    ylabel = "PLCC"
    savefile = "model_corr_fig/03_model_plcc_all.png"
  elif i==1:
    bar = bar_srcc
    bar_err = bar_srcc_err
    ylabel = "SRCC"
    savefile = "model_corr_fig/03_model_srcc_all.png"
  else:   
    bar = bar_krcc
    bar_err = bar_krcc_err
    ylabel = "KRCC"
    savefile = "model_corr_fig/03_model_krcc_all.png"
  size = 7
  x = np.arange(size)

  total_width, n = 0.8, 3
  width = total_width / n
  x = x - (total_width - width) / 3
  labels = ['Trial 1', 'Trial 2', 'Trial 3']
  # names = ["animal","flower","foliage","fruit","landscape","manmade","shadow","texture","winter"]
  names = ["HUMAN","MSE","SSIM","MS_SSIM","NLPD","LPIPS","DISTS"]
  plt.figure(figsize=(10,8))
  plt.bar(x, bar[0], yerr=bar_err[0] ,width=width,  label="total",capsize=4)
  plt.bar(x + width, bar[1],yerr=bar_err[1],tick_label=names, width=width,label="natural" ,capsize=4)
  plt.bar(x + 2*width, bar[2],yerr=bar_err[2], width=width,label="unnatural" ,capsize=4)
  # plt.ylabel("sigma")

  plt.ylabel(ylabel,fontsize=20)
  plt.xticks(fontsize=13)#
  plt.yticks(fontsize=15)
  # plt.ylim(0,1)
  # plt.legend(loc="right",fontsize=20)
  plt.legend(fontsize=20)
  plt.savefig( savefile )
  plt.show()
