
from IQA_pytorch import SSIM, GMSD, NLPD,LPIPSvgg, DISTS,MS_SSIM,VSI
import torchvision.transforms as transforms
import cv2
import torch
import pandas as pd

import numpy as np
import os
from wand.image import Image

def mse(A,B):
  return np.sqrt(np.sum(np.power((np.float32(A) - np.float32(B))/255, 2))/(256*256))

def metric(img1,img2,mode_num,D):
  t1 =transforms.ToTensor()(img1).unsqueeze(0).cuda()
  t2 =transforms.ToTensor()(img2).unsqueeze(0).cuda()
  score = D(t1,t2,as_loss=False)
  if mode_num==1 or mode_num==3:
      return 1-score.item()
  return score.item()

# 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
def noiseFind(step_size):
    step_num = int(1/step_size)
    print(str(step_size)+"-----step number:"+str(step_num))

    model_names = ["MSE", "SSIM", "NLPD", "MS_SSIM", "LPIPS", "DISTS"]

    column_names = ['natural*0'+str(i) for i in range(1,10)]+['unnatural*0'+str(i) for i in range(1,10)]


    for mode_num in range(6):

            paths = ["animal", "flower", "foliage", "fruit", "landscape", "manmade", "shadow", "texture", "winter"]
            upaths = list(map(lambda x: "u" + x, paths))

            modes = {0:"MSE", 1:"SSIM", 2:"NLPD", 3:"MS_SSIM",4: "LPIPS", 5: "DISTS" }
            mode = modes[mode_num]
            print(mode)

            if mode_num==1:
                D = SSIM(channels=1).cuda()
            elif mode_num==2:
                D = NLPD(channels=1).cuda()
            elif mode_num==3:
                D = MS_SSIM(channels=3).cuda()
            elif mode_num==4:
                D = LPIPSvgg(channels=3).cuda()
            elif mode_num==5:
                D = DISTS(channels=3).cuda()


            # errors = []
            pre = "jnd/"
            noise_jnd_mean = 0.46012526069642695  # the mean human JND for each distortion for normalization
            data = []

            step = noise_jnd_mean/step_num


            for index , path in zip(range(18),paths + upaths):

                start = step
                jnd = 1

                col = []
                filename1 = pre + path + ".png"
                img1 = cv2.imread(filename1, 0)

                while jnd < 2*step_num:

                    sigma = 0.001 * (10 ** (3 * jnd*step))
                    n_values = []
                    for seed in range(1, 11):
                        np.random.seed(seed)
                        noise = np.random.normal(0, sigma, img1.shape)
                        imgTmp = img1 / 255
                        gauss = np.clip(imgTmp + noise, 0, 1)
                        gauss = np.uint8(gauss * 255)
                        img2 = gauss
                        if (mode_num == 0):
                            value = mse(img1, img2)
                        else:
                            value = metric(img1, img2, mode_num,D)

                        n_values.append(value)

                    distance = np.mean(n_values)
                    col.append(distance)
                    jnd += 1
                data.append(col)

            df = pd.DataFrame(np.transpose(np.array(data)), columns=column_names)
            csv_name = "mono_noise_" + mode+"_distance.csv"
            df.to_csv(csv_name, index=False)




