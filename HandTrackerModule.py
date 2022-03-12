
import mediapipe as mp
import cv2
import time


# res = []
class HandDetector():
    def __init__(self, static = False, max_hands = 2, det_conf = 0.7, track_conf = 0.5, h = 0, w = 0, c = 0):
        self.static = static
        self.max_hands = max_hands
        self.det_conf = det_conf
        self.track_conf = track_conf
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static, self.max_hands, self.det_conf, self.track_conf)
        self.mpDraw = mp.solutions.drawing_utils
        
        self.h = h
        self.w = w
        self.c = c
        
#        print(self.h, self.w, self.c)
    
    
    
    
    def findHands(self, img, draw = True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.results = self.hands.process(imgRGB)        
 
        if(self.results.multi_hand_landmarks):
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_lms, self.mpHands.HAND_CONNECTIONS)           
        return img
    
     
    
    
    
    
    def findPosition(self, img, handNo = 0, draw = True):
        
        lmlist = []
        
        if(self.results.multi_hand_landmarks):
            req_hand = self.results.multi_hand_landmarks[handNo]
            # res.append(req_hand)
            for idd, lm in  enumerate(req_hand.landmark):
                print(idd, lm.z)
                cx, cy = int(lm.x * self.w), int(lm.y * self.h)
                lmlist.append([idd, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (100, 155, 200), cv2.FILLED)  
                    
        return lmlist
    
    
        
    
def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(1)
    
    success, img = cap.read()
    h, w, c = img.shape
    detector = HandDetector(h=h, w=w, c=c)
    
    try:
    
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img, draw=False)
            if(len(lmlist) != 0):
                print(lmlist[4])
            
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            
            img = cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 200), 2, cv2.LINE_AA)
            
            cv2.imshow('cam', img)
            key = cv2.waitKey(1)
            if(key == 27):
                break
        
    except:
    
        cap.release()
        cv2.destroyAllWindows()
    
    
    
    


if __name__ == "__main__":
    main()
    