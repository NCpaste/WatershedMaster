from cv2 import sort
import numpy as np
from torch import pixel_shuffle, reshape
from Watershed import Watershed
from PIL import Image
import matplotlib.pyplot as plt
from collections import deque

w = Watershed()
image = np.array(Image.open('/home/zzg/Documents/Code/Python/watershed-master/image/生物图像-李英/20/20_B1_2_red.tif'))
# /home/zzg/Documents/Code/Python/watershed-master/image/生物图像-李英/20
# labels = w.apply(image)
# plt.imshow(labels, cmap='Paired', interpolation='nearest')
# plt.show()

height, width = image.shape
pixels = np.mgrid[0:height, 0:width].reshape(2, -1).T
total = height * width
INIT = -1
reshaped_image = image.reshape(total)

indices = np.argsort(reshaped_image)
sorted_image = reshaped_image[indices]
sorted_pixels = pixels[indices]

# print(sorted_image.shape)
# print(sorted_pixels.shape)

# print(sorted_image[2111111])
print(sorted_pixels[2111111:2111119])

t_labels = np.full((height, width), INIT, np.int32)

print("Procedure End")