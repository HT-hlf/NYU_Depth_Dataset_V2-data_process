# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/9 21:06
# @File       : read_label.py
# @Software   : PyCharm

import numpy as np
import h5py
import os
from PIL import Image

f = h5py.File("nyu_depth_v2_labeled.mat")
labels = f["labels"]
labels = np.array(labels)

path_converted = './nyu_labels/'
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)

labels_number = []
for i in range(len(labels)):
    labels_number.append(labels[i])
    labels_0 = np.array(labels_number[i])
    label_img = Image.fromarray(np.uint8(labels_number[i]))
    label_img = label_img.transpose(Image.ROTATE_270)

    iconpath = './nyu_labels/' + str(i) + '.png'
    label_img.save(iconpath, 'PNG', optimize=True)

# 语义分割图片 识别出了图片中的每个物体