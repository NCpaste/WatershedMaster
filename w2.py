from dis import dis
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,feature
import cv2


def labelbased_w(imgpath):
    img = cv2.imread(imgpath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #颜色空间转换
    # kernel = np.ones((3,3),np.uint8)
    kernel = np.array(((1, 1, 1), (1, 0, 1), (1, 1, 1)),dtype = np.uint8) #开闭运算的模板，类似于卷积

    # ret0, thresh0 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) #二值化 同时前景后景转换
    # opening = cv2.morphologyEx(thresh0,cv2.MORPH_OPEN,kernel, iterations = 2) #开运算
    # # 确定背景区域
    # sure_bg = cv2.dilate(opening,kernel,iterations=3) #膨胀操作

    # 确定前景区域
    dist_transform = cv2.distanceTransform(gray ,cv2.DIST_L2,5) #任意点到背景点的距离
    ret1, sure_fg = cv2.threshold(dist_transform,0.3*dist_transform.max(),255,0) #二值化

    # opening_2 = cv2.morphologyEx(sure_fg, cv2.MORPH_OPEN, kernel, iterations = 10) #开运算
    opening_2 = cv2.erode(sure_fg, kernel, iterations=20) #腐蚀操作
    opening_2 = cv2.dilate(opening_2, kernel, iterations=30) #膨胀操作
    # 查找未知区域
    # sure_fg = np.uint8(sure_fg) #将数组转换为八通道
    opening_2 = np.uint8(opening_2) #将数组转换为八通道
    # unknown = cv2.subtract(sure_bg,sure_fg) #显示图像差值
    # unknown = cv2.subtract(sure_bg, opening_2) #显示图像差值

    # 标记标签
    # ret2, markers1 = cv2.connectedComponents(opening_2)
    ret2, markers1 = cv2.connectedComponents(opening_2)
    markers2 = markers1+1
    # markers[unknown==255] = 0
    print("num: ", ret2)
    plt.imsave('./image/markers1.png',markers1)

    markers3 = cv2.watershed(img,markers1)
    img[markers3 == -1] = [255,255,255] #计算图像差值，进行描边

    # print(markers1.shape)
    cv2.imwrite('./image/proc/opening_2.png',opening_2)
    cv2.imwrite('./image/proc/sure_bg.png',kernel)
    # plt.imsave('./image/proc/opening_2.png',opening_2)
    # plt.imsave('./image/proc/sure_bg.png',sure_bg)
    plt.imsave('./image/proc/markers2.png', markers2)
    plt.imsave('./image/proc/sure_fg.png', sure_fg)
    plt.imsave('./image/proc/markers3.png',markers3)
    cv2.imwrite('./image/proc/'+pic_name+'_test.png', img)
    # return dist_transform,thresh0,sure_fg,img
    return

if __name__ == '__main__':
    pic_name = '20_B1_2_red.tif'
    # image = np.array(Image.open('./image/'+pic_name+'.png'))

    imgpath = './image/'+pic_name
    labelbased_w(imgpath)
    # thresh0, sure_bg, sure_fg, img = labelbased_w(imgpath)

    # cv2.imwrite('./image/dis_transform.png',thresh0)
    # cv2.imwrite('./image/thresh0.png', sure_bg)
    # cv2.imwrite('./image/sure_fg.png', sure_fg)
    # cv2.imwrite('./image/result_img.png', img)
    # cv2.imwrite('./image/'+pic_name+'_test.png', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

