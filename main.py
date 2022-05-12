from os import PRIO_PGRP
from cv2 import imread
import numpy as np
from Watershed import Watershed
from PIL import Image
import matplotlib.pyplot as plt
from collections import deque

from process import Morphology_Dilate
    
pic_name = 'ex'
image = np.array(Image.open('./image/'+pic_name+'.png'))

print('start')
w = Watershed()

# out = Morphology_Dilate(image, 10)
out = np.array(Image.open('./image/'+pic_name+'.png'))

# pro_image = np.array(Image.open('/home/zzg/Documents/Code/Python/watershed-master/image/test.jpg'))
# print(pro_image.shape)
# print(image.shape)
labels = w.apply(out)
plt.imshow(labels, cmap='Paired', interpolation='nearest')
# plt.imsave('/home/zzg/Documets/Code/Python/watershed-master/image/RES.jpg')
plt.show()

print("Procedure End")