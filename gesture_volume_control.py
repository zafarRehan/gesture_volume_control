import math
import time
from ctypes import cast, POINTER
import numpy as np
import cv2
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import HandTrackerModule as htm


def start_volume_control():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(1)
    
    success, img = cap.read()
    h, w, c = img.shape
    # print(h, w, c)
    detector = htm.HandDetector(max_hands = 1, h=h, w=w, c=c, det_conf = 0.7)
    
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    volRange = volume.GetVolumeRange()
    maxVol = volRange[1]
    minVol = volRange[0]
    
    
    
    try:
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img, draw=False)
        
            
            if len(lmlist) != 0:
                # print(lmlist[4])        
                x1, y1 = lmlist[4][1], lmlist[4][2]
                x2, y2 = lmlist[8][1], lmlist[8][2]
                
                cx, cy = (x1+x2)//2, (y1+y2)//2
                
                        
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.circle(img, (cx, cy), 10, (100, 155, 200), cv2.FILLED) 
                
                length = math.hypot(x2-x1, y2-y1)
                
                if length < 50:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED) 
                # print(length)
                
                vol = np.interp(length, [50, 250], [minVol, maxVol])
                volume.SetMasterVolumeLevel(vol, None)
        
            
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            
            img = cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 
                              (255, 0, 200), 2, cv2.LINE_AA)
            
            cv2.imshow('cam', img)
            cv2.waitKey(1)
        
    except:
        cv2.destroyAllWindows()


    
if __name__ == "__main__":
    start_volume_control()
    
    
    