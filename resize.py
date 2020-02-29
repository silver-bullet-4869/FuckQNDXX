# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:11:35 2020

@author: asus
"""
import numpy as np
#import cv2
import math
from matplotlib import pyplot as plt
from PIL import Image

def resize(im,m,n):
    M = im.shape[0]
    N = im.shape[1]
    im2 = np.zeros([m,n,3],im.dtype)
    for x in range(m):
        for y in range(n):
            x0 = math.floor(x/m*M)
            y0 = math.floor(y/n*N)
            im2[x,y] = im[x0,y0]
    return im2

def resize2(filename,m,n):
    #im = cv2.imread(filename)
    im = np.array(Image.open(filename))
    M = im.shape[0]
    N = im.shape[1]
    if m*N==M*N:
        return resize(im,m,n)
    elif m*N>M*N:
        return resize(im[:,:math.floor(n*M/m),:],m,n)
    else:
        return resize(im[:math.floor(N*m/n),:,:],m,n)
    

        
    

if __name__ == "__main__":
    faker=np.array(Image.open("back2.jpg"))
    faker2 = resize2("back2.jpg",260,550)
    plt.imshow(faker2)
    