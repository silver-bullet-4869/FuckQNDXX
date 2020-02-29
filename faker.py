# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:42:30 2020

@author: asus
"""

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from resize import resize2

import round

def makeMatrix(M,N,rgb):
    matrix = np.zeros([M,N,3],np.uint8)
    for x in range(M):
        for y in range(N):
            for z in range(3):
                matrix[x,y,z] = rgb[z]
    return matrix

def draw(im1,x0,y0,im2):
    M = im2.shape[0]
    N = im2.shape[1]
    for x in range(M):
        for y in range(N):
            for z in range(3):
                im1[x0+x,y0+y,z] = im2[x,y,z] 
                
def drawPNG(im1,x0,y0,im2):
    M = im2.shape[0]
    N = im2.shape[1]
    for x in range(M):
        for y in range(N):
            if im2[x,y,3]!=0:
                for z in range(3):
                    im1[x0+x,y0+y,z] = im2[x,y,z] 
                
    
    

faker = makeMatrix(680, 550, [255,255,255])

#draw(faker,0,0,makeMatrix(260, 550, [100,100,100]))
draw(faker,0,0,resize2("back2.jpg",260,550))

touxiang = np.array(round.round_corner_jpg(Image.fromarray(resize2("touxiang.jpg",90,90)),10))
drawPNG(faker,190,430,touxiang)

draw(faker,400,105,resize2("photo.jpg",100,100))

textBox_x = 520
textBox_y = 105

draw(faker,textBox_x,textBox_y,makeMatrix(130, 430, [228,228,228]))
draw(faker,textBox_x+30,textBox_y,makeMatrix(100, 423, [206,206,206]))

draw(faker,textBox_x+40,textBox_y+5,resize2("change.jpg",75,75))

plt.imshow(faker)

#cv2.imwrite("faker.jpg",faker)


im = Image.fromarray(faker)
draw = ImageDraw.Draw(im)
ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\HGKT_CNKI.TTF", 25)
draw.text((350,220), u"小刚",font = ft, fill = 'white')

ft2 = ImageFont.truetype("C:\\WINDOWS\\Fonts\\HGKT_CNKI.TTF", 35)
draw.text((10,400),u"今天",font=ft2,fill = "black")

ft3 = ImageFont.truetype("C:\\WINDOWS\\Fonts\\HGKT_CNKI.TTF", 19)
draw.text((textBox_y+12,textBox_x+7),u"xxx第一次完成了第八季第二期",font = ft3,fill = 'black')
draw.text((textBox_y+90,textBox_x+53),u"我完成了“青年大学习”网上主题团课",font = ft3,fill = 'black')
draw.text((textBox_y+90,textBox_x+83),u"第八季第二期的内容，你也来试试吧",font = ft3,fill = 'black')



plt.imshow(im)


im.save("faker2.jpg")


