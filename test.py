# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:04:19 2020

@author: asus
"""


import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


qingnian = np.array(Image.open("qingnian2.jpg"))

plt.imshow(qingnian)

plt.imshow(qingnian[627:796,201:370,:])

Image.fromarray(qingnian[627:796,201:370,:]).save("photo.jpg")