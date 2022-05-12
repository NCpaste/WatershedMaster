from os import PRIO_PGRP
import cv2
import numpy as np
from Watershed import Watershed
from PIL import Image
import matplotlib.pyplot as plt
from collections import deque

def Morphology_Dilate(img, Dil_time = 1):
    print("Morphology_Dilate start")
    H, W = img.shape
    print(img.shape)

    #kernel (核心)
    # MF = np.array(((0,1,0), (1,0,1), (0,1,0)),
    #                 dtype = np.int32) #开闭运算的模板，类似于卷积
    MF = np.array(((1, 1, 1), (1, 0, 1), (1, 1, 1)),
                    dtype = np.int32) #开闭运算的模板，类似于卷积
    
    # each dilate time
    out = img.copy()
    for i in range(Dil_time):
        tmp = np.pad(out, (1, 1), 'edge') #padding 填充
        print('tmp_shape : ', tmp.shape, '  out.shape : ', out.shape)

        for y in range(int(H/2), H):
            for x in range(1, int(W)):
                if np.sum(MF*tmp[y-1:y+2, x-1:x+2]) >= 1:
                    # print(tmp[y-1:y+2, x-1:x+2])
                    out[y, x] = 255

    return tmp

def Erode(img, Dil_time = 1):
    print("Erode start")
    H, W = img.shape
    print(img.shape)

    #kernel (核心)
    # MF = np.array(((0,1,0), (1,0,1), (0,1,0)),
    #                 dtype = np.int32) #开闭运算的模板，类似于卷积
    MF = np.array(((1, 1, 1), (1, 0, 1), (1, 1, 1)),
                    dtype = np.int32) #开闭运算的模板，类似于卷积
    
    # each dilate time
    out = img.copy()
    for i in range(Dil_time):
        tmp = np.pad(out, (1, 1), 'edge') #padding 填充
        print('tmp_shape : ', tmp.shape, '  out.shape : ', out.shape)

        for y in range(1 , H):
            for x in range(1, int(W)):
                if np.sum(MF*tmp[y-1:y+2, x-1:x+2]) <= 350:
                    out[y, x] = 0

    return out

if __name__ == '__main__':

    pic_name = '123'
    image = np.array(Image.open('./image/'+pic_name+'.png'))

    print("image: ", image.shape)

    # out = Morphology_Dilate(image, 5)
    # plt.imshow(out)
    # plt.show()
    
    out = Erode(image, 5)

    cv2.imwrite('./image/'+pic_name+'_test2.png', out)
    # plt.imsave('/home/zzg/Documents/Code/Python/watershed-master/image/'+pic_name+'_test.tiff', out, 1728*1728)

    # pro_image = np.array(Image.open('/home/zzg/Documents/Code/Python/watershed-master/image/'+pic_name+'_test.png'))
    # plt.imshow(pro_image)
    # plt.show()
    
    # print("out: ", out.shape, "  pro_image: ", pro_image.shape)

    print("Procedure End")