# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/9 21:06
# @File       : read_name.py
# @Software   : PyCharm

import h5py
import numpy as np

f = h5py.File("./nyu_depth_v2_labeled.mat")

ft = open('names.txt', 'w+')
print(f["names"].shape)  # 打印查看类别个数，共894类
for j in range(894):
    name = f["names"][0][j]
    obj = f[name]
    # print(obj)
    a=[chr(i[0]) for i in obj[:]]
    strr = "".join(a)
    ft.write(strr + '\n')

ft.close()