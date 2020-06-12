#! python3

"""
Grabs each frame from a video and saves them to disk in the project root
"""

import cv2

video_capture = cv2.VideoCapture('car_drive.mp4')

success, image = video_capture.read()
count = 0
success = True
while success:
    success, image = video_capture.read()
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1
