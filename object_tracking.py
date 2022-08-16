from cmath import rect
from sre_constants import SUCCESS
import cv2
import math
import os
import time

vid = cv2.VideoCapture('PRO-C107-Reference-Code-main/bb3.mp4')
tracker = cv2.TrackerCSRT_create()
ret , img = vid.read()
bBox = cv2.selectROI('tracking', img,False)
tracker.init(img,bBox)
g1 = 530
g2 = 300
xs = []
ys = []
print(bBox)

def dbb(img,bBox):
    x,y,w,h = int(bBox[0]),int(bBox[1]),int(bBox[2]),int(bBox[3])
    cv2.rectangle(img,(x,y),(x+w , y+h),(230,50,42),3,1)

def track(img,bBox):
    x,y,w,h = int(bBox[0]),int(bBox[1]),int(bBox[2]),int(bBox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img,(c1,c2),2,(2,240,2),5)
    cv2.circle(img,(g1,g2),2,(0,255,0),3)
    dist = math.sqrt(((c1 - g1)**2)+(c2 - g2)**2)
    if(dist < 20):
        cv2.putText(img,'goal achieved',(300,130),cv2.FONT_HERSHEY_COMPLEX,0.7,(180,20,75),2)
    xs.append(c1)
    ys.append(c2)
    for i in range(0,len(xs)):
        cv2.circle(img,(xs[i],ys[i]),2,(170,170,90),5)

    
while True :
    ret, img = vid.read()
    SUCCESS, bBox = tracker.update(img)
    if(SUCCESS == True):
        dbb(img,bBox)
    else:
        cv2.putText(img,'lost',(75,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(114,190,78),2)
    track(img,bBox)
    cv2.imshow('ball tracking',img)
    if(cv2.waitKey(25) == 32):
        break
vid.release()
cv2.destroyAllWindows()