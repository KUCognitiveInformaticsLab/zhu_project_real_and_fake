
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

for model in ["MSE", "SSIM", "NLPD", "MS_SSIM", "LPIPS", "DISTS"]:
  # os.mkdir("na_"+model.lower()+"_fig")
# for model in ["MSE"]:
  make_targz_one_by_one("na_"+model.lower()+'_fig_all.tar', "./na_"+model.lower()+"_fig//")
