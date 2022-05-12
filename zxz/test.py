import numpy as np
from Watershed import Watershed

from PIL import Image
import matplotlib.pyplot as plt
from collections import deque
import os

print(os.getcwd)

image = np.array(Image.open('/home/zzg/Documents/Code/Python/watershed-master/image/生物图像-李英/20/20_B1_2_red.tif'))
# /home/zzg/Documents/Code/Python/watershed-master/image/生物图像-李英/20
plt.imshow(image)
print(image.shape)
# plt.imsave()
plt.show()

print("Procedure End")