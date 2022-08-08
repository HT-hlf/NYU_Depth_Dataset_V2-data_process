# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/9 21:05
# @File       : read_depth_fixed.py
# @Software   : PyCharm

import numpy as np
import h5py
import os
from PIL import Image
import cv2
import imageio


def noramlization(data):
    minVals = data.min()
    maxVals = data.max()
    ranges = maxVals - minVals
    normData = np.zeros(np.shape(data))
    m = data.shape[0]
    normData = data - np.tile(minVals, (m, 1))
    normData = normData / np.tile(ranges, (m, 1))
    normData = normData * 255
    normData = normData.astype(np.uint8)
    print(normData)
    return normData


f = h5py.File("nyu_depth_v2_labeled.mat")
depths = f["depths"]
depths = np.array(depths)

path_converted = './nyu_depths_rgb/'
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)

# max = depths.max()
# min = depths.min()
# print(depths.shape)
# print(depths.max())
# print(depths.min())

# depths = depths / max * 255
depths = depths.transpose((0, 2, 1))
print(depths)

print(depths.max())
print(depths.min())

for i in range(len(depths)):
    depths_i = noramlization(depths[i])
    print(depths[i].shape)
    depths_i = cv2.applyColorMap(cv2.convertScaleAbs(depths_i, alpha=1), 9)
    depths_i = cv2.flip(depths_i, 1)
    # cv2.imshow('image:', depths_i)
    # cv2.waitKey(0)
    # print(str(i) + '.jpg')
    # depths_img = Image.fromarray(np.uint8(depths[i]))
    # depths_img = depths_img.transpose(Image.FLIP_LEFT_RIGHT)
    iconpath = path_converted + str(i)+ '.jpg'
# depths_img.save(iconpath, 'JPG', optimize=True)
    cv2.imwrite(iconpath, depths_i)

# 同样方法可以提取rawdepth 对比查看深度图修复效果
