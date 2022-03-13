# Gesture Volume Control

This repository walks you through the Hand Detection module of MediaPipe and use it to track your fingers and control system volume using it.
MedaPipe Hands link: https://google.github.io/mediapipe/solutions/hands.html
 </br> 
 
## Required Libraries


    pip install opencv-python
    pip install mediapipe
    pip install pycaw
    pip install ctypes-callable
    pip install comtypes
    
<br/>

## Contents
<h4>1. HandTrackerModule.py</h4>
This code is used to track hands from a video source. </br>
Run this code to check hand detection from video

The code is well-commented so the working can be found in comments

<h4>2. gesture_volume_control.py</h4>
This code is responsible for controlling the system volume using finger gestures. </br>

<h4>3. screen_recorder.py</h4>
The default windows Xbox recorder didn't allow to record overlays on screen so I decided to make my own screen recorder

This require another library to read everything on screen

    pip install pyautogui

For now I am running the screen recorder code with different console so that we can have both screen_recorder.py and gesture_volume_control.py running simultaneously.
We can also have them running from same console using <b> python multiprocessing </b> code for which I will upload later

</br>

## Running the code
1. Run <a href="/gesture_volume_control.py">gesture_volume_control.py</a> for controlling the volume using finger tip gesture </br>
2. Run <a href="/HandTrackerModule.py">HandTrackerModule.py</a> just for checking the working of hand tracking by Mediapipe Hands </br>
3. Run <a href="/screen_recoreder.py">screen_recoreder.py</a> for using python to record your screen. Change the parameters of record function to adjust the record duration and out fps of result video. </br>


<
   
