# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:19:13 2020

@author: asus
"""

from PIL import Image, ImageDraw, ImageFont

import cv2
import numpy as np
from matplotlib import pyplot as plt

faker = cv2.imread("faker.jpg")
im = Image.fromarray(faker)
draw = ImageDraw.Draw(im)
ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\HGH_CNKI.TTF", 20)
draw.text((350,220), u"苏艺腾",font = ft, fill = 'white')
draw.text((90,560),u"苏艺腾第一次完成了第八季第二期",font = ft,fill = 'black')
draw.text((90,560),u"我完成了“青年大学习”网上主题团课",font = ft,fill = 'black')
draw.text((90,560),u"第八集第二期的内容，你也来试试吧",font = ft,fill = 'black')
ft2 = ImageFont.truetype("C:\\WINDOWS\\Fonts\\HGH_CNKI.TTF", 27)
draw.text((10,400),u"今天",font=ft2,fill = "black")


plt.imshow(im)


im.save("faker2.jpg")