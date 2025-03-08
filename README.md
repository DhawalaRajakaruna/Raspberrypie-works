
# Hand Angle Detection for a project to do using Raspberry pie
## Overview
This project uses a webcam and the Raspberry Pi to detect the angle between the hand and the center of the camera frame. By using the MediaPipe library, it identifies the position of the hand landmarks and calculates the angle based on the index finger's position. This angle can be useful for applications such as controlling motors, robotics, or gesture-based interfaces.

The project uses the **OpenCV** and **MediaPipe** libraries for computer vision and hand landmark detection.

## Requirements
To run this project, ensure that your Raspberry Pi has the following:

Raspberry Pi (any model with a camera) with Raspbian OS installed.
Webcam connected to the Raspberry Pi.
Python 3 installed on your Raspberry Pi.
The following Python packages:
opencv-python
mediapipe
