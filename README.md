# Gesture Volume Control

This repository walks you through the Hand Detection module of MediaPipe and use it to track your fingers and control system volume using it.
MedaPipe Hands link: https://google.github.io/mediapipe/solutions/hands.html

<h3>Required Libraries</h3>


    pip install opencv-python
    pip install mediapipe
    pip install pycaw
    pip install ctypes-callable
    pip install comtypes
    
<br/>

<h3>Contents</h3>
<h4>1. HandTrackerModule.py</h4> </br>
This code is used to track hands from a video source. </br>
Run this code to check hand detection from video

The code is well-commented so the working can be found in comments

<h4>2. gesture_volume_control.py</h4> </br>
This code is responsible for controlling the system volume using finger gestures. </br>

<h4>3. screen_recorder.py</h4> </br>
The default windows Xbox recorder didn't allow to record overlays on screen so I decided to make my own screen recorder

This require another 

