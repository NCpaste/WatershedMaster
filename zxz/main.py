import numpy as np
from Watershed import Watershed
from PIL import Image
import matplotlib.pyplot as plt
from collections import deque

w = Watershed()
image = np.array(Image.open('/home/zzg/Documents/Code/Python/watershed-master/image/生物图像-李英/20/20_B1_2_red.tif'))
# /home/zzg/Documents/Code/Python/watershed-master/image/生物图像-李英/20
labels = w.apply(image)
plt.imshow(labels, cmap='Paired', interpolation='nearest')
plt.show()

print("Procedure End")