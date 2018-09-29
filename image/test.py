from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=np.array(Image.open('./img_pyplot.jpg'))  #打开图像并转化为数字矩阵
# 512*512*3
print(img.shape)
plt.figure("dog")
plt.imshow(img)
plt.axis('off')
plt.show()
