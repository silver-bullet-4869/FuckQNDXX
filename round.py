# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:22:18 2020

@author: asus
"""

from PIL import Image,ImageDraw,ImageChops
import aggdraw
import os

def round_corner_jpg(image, radius):
    """generate round corner for image"""
    mask = Image.new('L', image.size) # filled with black by default
    draw = aggdraw.Draw(mask)
    brush = aggdraw.Brush('white')
    width, height = mask.size
    #upper-left corner
    draw.pieslice((0,0,radius*2, radius*2), 90, 180, None, brush)
    #upper-right corner
    draw.pieslice((width - radius*2, 0, width, radius*2), 0, 90, None, brush)
    #bottom-left corner
    draw.pieslice((0, height - radius * 2, radius*2, height),180, 270, None, brush)
    #bottom-right corner
    draw.pieslice((width - radius * 2, height - radius * 2, width, height), 270, 360, None, brush)
    #center rectangle
    draw.rectangle((radius, radius, width - radius, height - radius), brush)
    #four edge rectangle
    draw.rectangle((radius, 0, width - radius, radius), brush)
    draw.rectangle((0, radius, radius, height-radius), brush)
    draw.rectangle((radius, height-radius, width-radius, height), brush)
    draw.rectangle((width-radius, radius, width, height-radius), brush)
    draw.flush()
    image = image.convert('RGBA')
    image.putalpha(mask)
    return image

def get_filePath_fileName_fileExt(fileUrl):
    """
    获取文件路径， 文件名， 后缀名
    :param fileUrl:
    :return:
    """
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

if __name__ == '__main__':
    picLocation = 'touxiang.jpg'
    im = Image.open(picLocation)
    im = round_corner_jpg(im, 20)
    im.save(get_filePath_fileName_fileExt(picLocation)[1]+'_round.png')