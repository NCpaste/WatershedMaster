from dis import dis
from readline import read_init_file
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,feature
import cv2
import os


def labelbased_w(imgpath, ind, discrepance, discrepance2, file_name):
    img = cv2.imread(imgpath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #颜色空间转换
    kernel = np.array(((1, 1, 1), (1, 0, 1), (1, 1, 1)),dtype = np.uint8) #开闭运算的模板，类似于卷积

    # 确定前景区域
    dist_transform = cv2.distanceTransform(gray ,cv2.DIST_L2,5) #任意点到背景点的距离
    ret1, sure_d = cv2.threshold(dist_transform,dist_transform.max()/ind,255,0) #二值化
    print(ret1)

    opening_1 = cv2.erode(sure_d, kernel, iterations=discrepance2) #腐蚀操作
    opening_1 = cv2.dilate(opening_1, kernel, iterations=discrepance) #膨胀操作
    # 查找未知区域
    opening_1 = np.uint8(opening_1) #将数组转换为八通道
    plt.imsave('./image/proc/'+file_name+'/opening_1.png', opening_1)

    # 标记标签  
    ret2, markers1 = cv2.connectedComponents(opening_1)
    plt.imsave('./image/proc/'+file_name+'/markers1.png',markers1)
    
    print("num: ", ret2)

    markers1 = cv2.watershed(img,markers1)
    plt.imsave('./image/proc/'+file_name+'/m_watershed.png', markers1)
    img[markers1 == -1] = [255,255,255] #计算图像差值，进行描边

    # cv2.imwrite
    # plt.imsave
    plt.imsave('./image/proc/'+file_name+'/dist_transform.png',dist_transform)
    plt.imsave('./image/proc/'+file_name+'/sure_fg.png', sure_d)
    plt.imsave('./image/proc/'+file_name+'/Res.png', img)
    return

def read_path(path_name, ind, discrepance, discrepance2):  
    print('read_path')  
    for dir_item in os.listdir(path_name):
        #从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        
        if os.path.isdir(full_path):    #如果是文件夹，继续递归调用
            read_path(full_path, ind, discrepance, discrepance2)
        else:   #文件
            print(full_path)
            if dir_item.endswith('.tif'): 
                pic_name = dir_item
                # pic_name_e = '.tif' 

                mod_name = '_%d' %ind + '_%d' %discrepance + '_%d' %discrepance2
                path = "./image/proc/"+pic_name
                if not os.path.exists(path):
                    os.mkdir(path)
                mod_path = "./image/proc/"+pic_name+'/'+mod_name
                if not os.path.exists(mod_path):
                    os.mkdir(mod_path)
                print(mod_path)

                imgpath = full_path
                # imgpath = './image/'+pic_name+pic_name_e
                file_name = pic_name + '/' + mod_name 
                labelbased_w(imgpath, ind, discrepance, discrepance2, file_name)

                    


if __name__ == '__main__':
    # pic_name = '20_B1_2_red'
    # pic_name_e = '.tif'
    
    ind = 7 # 距离精度, 越大精度越大
    discrepance = 20 # 膨胀 误差大小
    discrepance2 = 30 # 腐蚀 误差大小

    read_path('./image/生物图像-李英', ind, discrepance, discrepance2)

    # mod_name = '_%d' %ind + '_%d' %discrepance
    # path = "./image/proc/"+pic_name
    # if not os.path.exists(path):
    #     os.mkdir(path)
    # mod_path = "./image/proc/"+pic_name+'/'+mod_name
    # if not os.path.exists(mod_path):
    #     os.mkdir(mod_path)
    # print(mod_path)

    # imgpath = './image/'+pic_name+pic_name_e
    # file_name = pic_name + '/_%d' %ind + '_%d' %discrepance 
    # labelbased_w(imgpath, ind, discrepance, file_name)

    print('proc_end')
