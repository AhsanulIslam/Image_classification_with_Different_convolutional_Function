# -*- coding: utf-8 -*-
"""HomeworkCVPR (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SsUZ8WKHPWx301Lt-gwUS_U2ClrJUdO1
"""

import os
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import random
from matplotlib import pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)
Image=cv2.imread('/content/CodeImage128.jpg',0)
 
kernelH=np.array([[0,0,0],
                  [1,1,1],
                  [0,0,0]])
 
kernelV=np.array([[0,1,0],
                  [0,1,0],
                  [0,1,0]])
 
kernelC=np.array([[1,1,0],
                  [1,0,0],
                  [0,0,0]])
 
kernelO=np.array([[0,1,0],
                  [1,-1,1],
                  [0,1,0]])
 
 
kernelD=np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1]])
 
#print(kernelH2)
#Ganjam=[]
#for j in range(Image.shape[0]-78): 
#  for i in range(Image.shape[1]-78):
#    cv2_imshow(Image[0+j:50+j,0+i:80+i])
 
#for i in range(len(Ganjam)):
  #cv2_imshow(Ganjam[i])
  #plt.figure()
  #plt.imshow(Ganjam[i])
#plt.figure()
#plt.imshow(Image)
#print(Ganjam)
#plt.imshow(cv2.cvtColor(Ganjam, cv2.COLOR_BGR2RGB))
 
Testing2=np.array([[0,1,0,0,0,0,0,0],
                   [0,1,1,0,0,0,0,0],
                   [0,1,0,1,0,0,0,0],
                   [0,1,0,0,1,0,0,0],
                   [0,1,0,0,0,1,0,0],
                   [1,1,1,1,1,1,1,0],
                   [0,1,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0]  ])
 
 
Testing3=np.array([[0,1,0,0,0,0,0,0],
                   [0,1,1,0,0,0,0,0],
                   [0,1,0,1,0,0,0,0],
                   [0,1,0,0,1,0,0,0],
                   [0,1,0,0,0,1,0,0],
                   [1,1,1,1,1,1,1,0],
                   [0,1,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0]  ])
 
 
 
 
Testing=np.array([[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,-0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,],
                  
                                  ])
 
#print(Testing.shape[0])
#print(Testing.shape[1])
#plt.imwrite()
 
def Maxpool(Testing2):
  
  ARRAY=np.zeros([int(Testing2.shape[0]/2),int(Testing2.shape[0]/2)])
  for i in range(int(Testing2.shape[0]/2)):
    for j in range(int(Testing2.shape[0]/2)):
      ARRAY[i][j]=max(Testing2[0+i:2+i,0+j:2+j].flatten())
  return ARRAY
 
import math
 
def Sgimoid(Testing2):
  ARRAY=np.zeros([Testing2.shape[0],Testing2.shape[0]])
  for i in range(Testing2.shape[0]):
    for j in range(Testing2.shape[1]):
      ARRAY[i][j]=1/(1+math.exp(1)**-Testing2[i][j])
  return ARRAY
 
def Tanh(axe):
  ARRAY=np.zeros([axe.shape[0],axe.shape[1]])
  for i in range(axe.shape[0]):
    for j in range(axe.shape[1]):
      ARRAY[i][j]=(math.exp(1)**axe[i][j]-math.exp(1)**-axe[i][j])/(math.exp(1)**axe[i][j]+math.exp(1)**-axe[i][j])
 
  return ARRAY
 
def mapPrinter(Testing,kernel2):
  
  Testing=padding(Testing)
  ActMap=np.zeros([Testing.shape[0]-2,Testing.shape[1]-2])
  #print(ActMap.shape,"This is activation")
  #Testing=cv2.cvtColor(Testing, cv2.COLOR_BGRA2RGB)
  for j in range(Testing.shape[0]-kernel2.shape[0]+1): #row
    for i in range(Testing.shape[1]-kernel2.shape[1]+1):  #column
      ActMap[j][i]=np.sum(kernel2*Testing[0+j:kernel2.shape[0]+j,0+i:kernel2.shape[1]+i])
  #plt.figure()
  #plt.imshow(ActMap)
  #plt.imshow(ActMap)
  return ActMap
 
def Relu(Inputimage):
  for i in range(Inputimage.shape[0]):
    for j in range(Inputimage.shape[1]):
      if Inputimage[i][j]<=0:
        Inputimage[i][j]=0
  return Inputimage
 
def LeakyRelu(Inputimage):
  for i in range(Inputimage.shape[0]):
    for j in range(Inputimage.shape[1]):
      if Inputimage[i][j]<=0:
        Inputimage[i][j]=Inputimage[i][j]*0.01
      
  return Inputimage
 
 
def padding(Image):
  length=Image.shape[0]+2
  width=Image.shape[1]+2  
  NewImg=np.zeros([length,width])
  #print(NewImg.shape)
  for i in range(Image.shape[0]):
    NewImg[i+1][1:Image.shape[1]+1]=Image[i][:] # first slice of pic horz
  #print(Image.shape[0])
  #plt.imshow(NewImg)
  return NewImg
 
plt.imshow(Testing,cmap='inferno')####
plt.figure()
#plt.imshow(Testing)
 
 
Row=3
Column=6
figsiz=[25,9]
figsiz2=[25,12]
fig = plt.figure(figsize=figsiz)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
ax = fig.add_subplot(Row, Column, 1)
ax.axis('off')
ax.text(0.5, 0.5, "/////", bbox=dict(facecolor='red', alpha=0.8))
 
 
ax = fig.add_subplot(Row, Column, 2)
ax.axis('off')
ax.text(0.5, 0.5, "Kernel_H", bbox=dict(facecolor='red', alpha=0.8))
 
 
ax = fig.add_subplot(Row, Column, 3)
ax.axis('off')
ax.text(0.5, 0.5, "Kernel_V", bbox=dict(facecolor='red', alpha=0.8))
 
 
 
ax = fig.add_subplot(Row, Column, 4)
ax.axis('off')
ax.text(0.5, 0.5, "Kernel_C", bbox=dict(facecolor='red', alpha=0.8))
 
 
ax = fig.add_subplot(Row, Column, 5)
ax.axis('off')
ax.text(0.5, 0.5, "Kernel_O", bbox=dict(facecolor='red', alpha=0.8))
 
 
ax = fig.add_subplot(Row, Column, 6)
ax.axis('off')
ax.text(0.5, 0.5, "Kernel_D", bbox=dict(facecolor='red', alpha=0.8))
###################################################
##################################################
Image=cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
#Testing=Image
 
######################################################
################################################
 
 
 
ax = fig.add_subplot(Row, Column, 7)
ax.axis('off')
ax.text(0.5, 0.5, "FirstConvolution      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 8)
ax.axis('off')
 
FirstConvo1_H=mapPrinter(Testing,kernelH)
ax.imshow(FirstConvo1_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 9)
FirstConvo1_V=mapPrinter(Testing,kernelV)
ax.imshow(FirstConvo1_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 10)
FirstConvo1_C=mapPrinter(Testing,kernelC)
ax.imshow(FirstConvo1_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 11)
FirstConvo1_O=mapPrinter(Testing,kernelO)
ax.imshow(FirstConvo1_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 12)
FirstConvo1_D=mapPrinter(Testing,kernelD)
ax.axis('off')
ax.imshow(FirstConvo1_D,cmap='gray')
 
#######################################
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "FirstRelu      ", bbox=dict(facecolor='red', alpha=0.8))
 
 
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstRelu_H=Relu(FirstConvo1_H)
ax.imshow(FirstRelu_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstRelu_V=Relu(FirstConvo1_V)
ax.imshow(FirstRelu_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstRelu_C=Relu(FirstConvo1_C)
ax.imshow(FirstRelu_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstRelu_O=Relu(FirstConvo1_O)
ax.imshow(FirstRelu_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstRelu_D=Relu(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstRelu_D,cmap='gray')
###################################################################################
 
#######################################
#############################THIS IS SIGMOID
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "FirstSigmoid      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstSigmoid_H=Sgimoid(FirstConvo1_H)
ax.imshow(FirstSigmoid_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstSigmoid_V=Sgimoid(FirstConvo1_V)
ax.imshow(FirstSigmoid_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstSigmoid_C=Sgimoid(FirstConvo1_C)
ax.imshow(FirstSigmoid_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstSigmoid_O=Sgimoid(FirstConvo1_O)
ax.imshow(FirstSigmoid_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstSigmoid_D=Sgimoid(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstSigmoid_D,cmap='gray')
########################################################################
 
#######################################
#############################THIS IS TANH
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "FIRST TANH      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstTanh_H=Tanh(FirstConvo1_H)
ax.imshow(FirstTanh_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstTanh_V=Tanh(FirstConvo1_V)
ax.imshow(FirstTanh_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstTanh_C=Tanh(FirstConvo1_C)
ax.imshow(FirstTanh_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstTanh_O=Tanh(FirstConvo1_O)
ax.imshow(FirstTanh_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstTanh_D=Tanh(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstTanh_D,cmap='gray')
############################################
#######################
 
 
 
#############################THIS IS Leaky Relu
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "FIRST LeakyRelu      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstLeakyRelu_H=LeakyRelu(FirstConvo1_H)
ax.imshow(FirstLeakyRelu_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstLeakyRelu_V=LeakyRelu(FirstConvo1_V)
ax.imshow(FirstLeakyRelu_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstLeakyRelu_C=LeakyRelu(FirstConvo1_C)
ax.imshow(FirstLeakyRelu_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstLeakyRelu_O=LeakyRelu(FirstConvo1_O)
ax.imshow(FirstLeakyRelu_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstLeakyRelu_D=LeakyRelu(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstLeakyRelu_D,cmap='gray')
#######################################
 
 
 
 
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
ax = fig.add_subplot(Row, Column, 1)
ax.axis('off')
ax.text(0.5, 0.5, "Second Convolution      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 2)
ax.axis('off')
 
FirstConvo1_H=mapPrinter(FirstRelu_H,kernelH)
ax.imshow(FirstConvo1_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 3)
FirstConvo1_V=mapPrinter(FirstRelu_V,kernelV)
ax.imshow(FirstConvo1_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 4)
FirstConvo1_C=mapPrinter(FirstRelu_C,kernelC)
ax.imshow(FirstConvo1_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 5)
FirstConvo1_O=mapPrinter(FirstRelu_O,kernelO)
ax.imshow(FirstConvo1_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 6)
FirstConvo1_D=mapPrinter(FirstRelu_D,kernelD)
ax.axis('off')
ax.imshow(FirstConvo1_D,cmap='gray')
#######################################
 
 
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "Second Relu      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstRelu_H=Relu(FirstConvo1_H)
ax.imshow(FirstRelu_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstRelu_V=Relu(FirstConvo1_V)
ax.imshow(FirstRelu_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstRelu_C=Relu(FirstConvo1_C)
ax.imshow(FirstRelu_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstRelu_O=Relu(FirstConvo1_O)
ax.imshow(FirstRelu_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstRelu_D=Relu(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstRelu_D,cmap='gray')
########################################################################
 
 
########################################################################
 
#######################################
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "SecondSigmoid      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstSigmoid_H=Sgimoid(FirstConvo1_H)
ax.imshow(FirstSigmoid_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstSigmoid_V=Sgimoid(FirstConvo1_V)
ax.imshow(FirstSigmoid_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstSigmoid_C=Sgimoid(FirstConvo1_C)
ax.imshow(FirstSigmoid_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstSigmoid_O=Sgimoid(FirstConvo1_O)
ax.imshow(FirstSigmoid_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstSigmoid_D=Sgimoid(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstSigmoid_D,cmap='gray')
########################################################################
#######################
 
#######################################
#############################THIS IS TANH
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "Second TANH      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstTanh_H=Tanh(FirstConvo1_H)
ax.imshow(FirstTanh_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstTanh_V=Tanh(FirstConvo1_V)
ax.imshow(FirstTanh_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstTanh_C=Tanh(FirstConvo1_C)
ax.imshow(FirstTanh_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstTanh_O=Tanh(FirstConvo1_O)
ax.imshow(FirstTanh_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstTanh_D=Tanh(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstTanh_D,cmap='gray')
############################################
 
#############################THIS IS Leaky Relu
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "SECOND LeakyRelu      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstLeakyRelu_H=LeakyRelu(FirstConvo1_H)
ax.imshow(FirstLeakyRelu_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstLeakyRelu_V=LeakyRelu(FirstConvo1_V)
ax.imshow(FirstLeakyRelu_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstLeakyRelu_C=LeakyRelu(FirstConvo1_C)
ax.imshow(FirstLeakyRelu_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstLeakyRelu_O=LeakyRelu(FirstConvo1_O)
ax.imshow(FirstLeakyRelu_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstLeakyRelu_D=LeakyRelu(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstLeakyRelu_D,cmap='gray')
#######################################
 
 
 
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
ax = fig.add_subplot(Row, Column, 1)
ax.axis('off')
ax.text(0.5, 0.5, "First Maxpool      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 2)
ax.axis('off')
 
FirstMaxPool_H=Maxpool(FirstRelu_H)
ax.imshow(FirstMaxPool_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 3)
FirstMaxPool_V=Maxpool(FirstRelu_V)
ax.imshow(FirstMaxPool_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 4)
FirstMaxPool_C=Maxpool(FirstRelu_C)
ax.imshow(FirstMaxPool_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 5)
FirstMaxPool_O=Maxpool(FirstRelu_O)
ax.imshow(FirstMaxPool_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 6)
FirstMaxPool_D=Maxpool(FirstRelu_D)
ax.axis('off')
ax.imshow(FirstMaxPool_D,cmap='gray')
#######################################
 
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
ax = fig.add_subplot(Row, Column, 1)
ax.axis('off')
ax.text(0.5, 0.5, "Third Convolution      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 2)
ax.axis('off')
 
FirstConvo1_H=mapPrinter(FirstMaxPool_H,kernelH)
ax.imshow(FirstConvo1_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 3)
FirstConvo1_V=mapPrinter(FirstMaxPool_V,kernelV)
ax.imshow(FirstConvo1_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 4)
FirstConvo1_C=mapPrinter(FirstMaxPool_C,kernelC)
ax.imshow(FirstConvo1_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 5)
FirstConvo1_O=mapPrinter(FirstMaxPool_O,kernelO)
ax.imshow(FirstConvo1_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 6)
FirstConvo1_D=mapPrinter(FirstMaxPool_D,kernelD)
ax.axis('off')
ax.imshow(FirstConvo1_D,cmap='gray')
#######################################
 
 
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "Third Relu      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstRelu_H=Relu(FirstConvo1_H)
ax.imshow(FirstRelu_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstRelu_V=Relu(FirstConvo1_V)
ax.imshow(FirstRelu_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstRelu_C=Relu(FirstConvo1_C)
ax.imshow(FirstRelu_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstRelu_O=Relu(FirstConvo1_O)
ax.imshow(FirstRelu_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstRelu_D=Relu(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstRelu_D,cmap='gray')
########################################################################
########################################################################
 
#######################################
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "Third Sigmoid      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstSigmoid_H=Sgimoid(FirstConvo1_H)
ax.imshow(FirstSigmoid_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstSigmoid_V=Sgimoid(FirstConvo1_V)
ax.imshow(FirstSigmoid_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstSigmoid_C=Sgimoid(FirstConvo1_C)
ax.imshow(FirstSigmoid_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstSigmoid_O=Sgimoid(FirstConvo1_O)
ax.imshow(FirstSigmoid_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstSigmoid_D=Sgimoid(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstSigmoid_D,cmap='gray')
########################################################################
#######################
 
#######################################
#############################THIS IS TANH
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "Third TANH      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstTanh_H=Tanh(FirstConvo1_H)
ax.imshow(FirstTanh_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstTanh_V=Tanh(FirstConvo1_V)
ax.imshow(FirstTanh_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstTanh_C=Tanh(FirstConvo1_C)
ax.imshow(FirstTanh_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstTanh_O=Tanh(FirstConvo1_O)
ax.imshow(FirstTanh_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstTanh_D=Tanh(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstTanh_D,cmap='gray')
############################################
 
#############################THIS IS Leaky Relu
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
 
 
ax = fig.add_subplot(Row, Column, 13)
ax.axis('off')
ax.text(0.5, 0.5, "Third LeakyRelu      ", bbox=dict(facecolor='green', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 14)
ax.axis('off')
 
FirstLeakyRelu_H=LeakyRelu(FirstConvo1_H)
ax.imshow(FirstLeakyRelu_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 15)
FirstLeakyRelu_V=LeakyRelu(FirstConvo1_V)
ax.imshow(FirstLeakyRelu_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 16)
FirstLeakyRelu_C=LeakyRelu(FirstConvo1_C)
ax.imshow(FirstLeakyRelu_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 17)
FirstLeakyRelu_O=LeakyRelu(FirstConvo1_O)
ax.imshow(FirstLeakyRelu_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 18)
FirstLeakyRelu_D=LeakyRelu(FirstConvo1_D)
ax.axis('off')
ax.imshow(FirstLeakyRelu_D,cmap='gray')
#######################################
 
 
 
Row=4
Column=6
fig = plt.figure(figsize=figsiz2)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
 
ax = fig.add_subplot(Row, Column, 1)
ax.axis('off')
ax.text(0.5, 0.5, "Second Maxpool      ", bbox=dict(facecolor='red', alpha=0.8))
 
###CONV
 
ax = fig.add_subplot(Row, Column, 2)
ax.axis('off')
 
FirstMaxPool_H=Maxpool(FirstRelu_H)
ax.imshow(FirstMaxPool_H,cmap='gray')
 
ax = fig.add_subplot(Row, Column, 3)
FirstMaxPool_V=Maxpool(FirstRelu_V)
ax.imshow(FirstMaxPool_V,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 4)
FirstMaxPool_C=Maxpool(FirstRelu_C)
ax.imshow(FirstMaxPool_C,cmap='gray')
 
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 5)
FirstMaxPool_O=Maxpool(FirstRelu_O)
ax.imshow(FirstMaxPool_O,cmap='gray')
 
ax.axis('off')
ax = fig.add_subplot(Row, Column, 6)
FirstMaxPool_D=Maxpool(FirstRelu_D)
ax.axis('off')
ax.imshow(FirstMaxPool_D,cmap='gray')
#######################################



