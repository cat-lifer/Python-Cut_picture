# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:40:49 2020

@author: hhy

"""
####################### 批量裁剪图片 ##################
import os
import cv2
import numpy as np
 
n = 1  # 拆分多少行？
m = 4 # 拆分多少列？
 
def divide_imgs(img_path, img_name, save_path):
    '''
    拆分图像
    :param img_path:
    :param img_name:
    :param save_path:
    :return:
    '''
    imgg = img_path + img_name
    img = cv2.imread(imgg)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    h = img.shape[0]
    w = img.shape[1]
    print('h={},w={},n={},m={}'.format(h, w, n, m))
    dis_h = int(np.floor(h / n))
    dis_w = int(np.floor(w / m))
    num = 0
    for i in range(n):
        for j in range(m):
            num += 1
            print('i,j={}{}'.format(i, j))
            sub = img[dis_h * i:dis_h * (i + 1), dis_w * j:dis_w * (j + 1), :]
            save_imgs_path = save_path + '\\' + str(img_name.split('.')[0]) + '\\'
            if not os.path.exists(save_imgs_path):
                os.makedirs(save_imgs_path)
            cv2.imwrite(save_imgs_path + '{}.tif'.format(num), sub)
 
 
if __name__ == '__main__':
 
    img_path = 'C:\\Users\\Uaena_HY\\Desktop\\a\\'  #原始图片路径
    save_path = 'C:\\Users\\Uaena_HY\\Desktop\\b\\'  #裁剪完保存路径
    img_list = os.listdir(img_path)
    for name in img_list:
        print(name)
        divide_imgs(img_path, name, save_path)
