# -*- coding: utf-8 -*-

import cv2
import os
import sys
import time
import numpy as np
import shutil
if os.path.isdir('F:/视频去水印/VWE-master/watermark/frame')==False:
    os.mkdir('F:/视频去水印/VWE-master/watermark/frame')
else:
    delList = []
    delDir = "frame"
    delList = os.listdir(delDir)
    for f in delList:        
        filePath = os.path.join(delDir, f )
        if os.path.isfile(filePath):
            os.remove(filePath)
    print ("已有文件已经清除")
#把视频保存成图片
cap = cv2.VideoCapture('Tencent.mp4')
global c
c = 0
if cap.isOpened():
    i = 0
    ret, frame = cap.read()
    interf = eval(input("帧间隔为："))
    while ret:
        i+=1
        ret, frame = cap.read()      
        if i%interf == 0:
            c = c+1
            cv2.imwrite('frame/'+str(c)+'.jpg',frame)
        if ret==False:
            os.remove('frame/'+str(c)+'.jpg')
            c = c-1
            print("截取的帧数量：{},视频帧数：{}".format(c,i))
            break
else:
    print("视频读取失败。")
#读取图片，检测水印
path = "frame/"
i = 0
filePath = path+str(c-i)+".jpg"
dirs = os.listdir( path )
mask = cv2.imread(path+"1.jpg")
mgray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(mgray, 127, 255, cv2.THRESH_BINARY)
for file in dirs:
    i=i+1
    img = cv2.imread(path+file)    
    img1= cv2.imread(filePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    ret, img1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
    diff = cv2.bitwise_and(img, img1)
    mask = cv2.bitwise_and(diff,mask)
kernel = np.ones((2, 2), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=1)
cv2.imshow("水印",mask)
    
