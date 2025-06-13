import mediapipe as mp
import cv2
from handtrackmodule import handDetector
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = handDetector()
colorR=(255,0,255)

cx,cy,w,h=100,100,200,200

class DragRect():
    def __init__(self,posCenter,size=[200,200]):
        self.posCenter=posCenter
        self.size=size

    def update(self,cursor):
        
        cx,cy=self.posCenter
        w,h=self.size

        if (cx-w//2 < cursor[0] < cx+w//2) and (cy-h//2 < cursor[1] < cy+h//2):    
            self.posCenter = cursor

rectList=[]            
for x in range(5):
    rectList.append(DragRect([x*250+150,150]))

while True:

    success, img = cap.read()
    img=cv2.flip(img,1)
    img=detector.findHands(img)
    lmlist=detector.findPosition(img)
    if lmlist:
        #print(lmlist[8])
        length=detector.finddistance(8,12,img,lmlist,draw=False)
        print(length)
        if length<45:
            cursor=lmlist[8]
            for rect in rectList:
                rect.update(cursor[1:])

    imgNew=np.zeros_like(img,np.uint8)
    for rect in rectList:
        cx,cy=rect.posCenter
        w,h=rect.size
        marker_size = 30  # Adjust as needed
        thickness = 2     # Adjust as needed

        # Draw cross markers at each corner
        cv2.drawMarker(imgNew, (cx - w//2, cy - h//2), (0,255,0), markerType=cv2.MARKER_CROSS, markerSize=marker_size, thickness=thickness)
        cv2.drawMarker(imgNew, (cx + w//2, cy - h//2), (0,255,0), markerType=cv2.MARKER_CROSS, markerSize=marker_size, thickness=thickness)
        cv2.drawMarker(imgNew, (cx - w//2, cy + h//2), (0,255,0), markerType=cv2.MARKER_CROSS, markerSize=marker_size, thickness=thickness)
        cv2.drawMarker(imgNew, (cx + w//2, cy + h//2), (0,255,0), markerType=cv2.MARKER_CROSS, markerSize=marker_size, thickness=thickness) 
        cv2.rectangle(imgNew,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),colorR,cv2.FILLED)

    out=img.copy()
    alpha=0.5
    mask = imgNew.astype(bool)
    out[mask]=cv2.addWeighted(img,alpha,imgNew,1-alpha,0)[mask]    
        
    cv2.imshow('image',out)
    

    if cv2.waitKey(30)==27:
        break