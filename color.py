# Importing all modules
import cv2
import numpy as np
from collections import deque
import argparse

# Specifying upper and lower ranges of color to detect in hsv format
lower = np.array([15, 150, 20])
upper = np.array([35, 255, 255]) # (These ranges will detect Yellow)

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())



pts = deque(maxlen=args["buffer"])

while True:
    success, video = webcam_video.read() # Reading webcam footage
    
#     video = cv2.rotate(video, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format

    mask = cv2.inRange(img, lower, upper) # Masking the image to find our color

    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

    Window_Y, Window_X = video.shape[:2]

    # Finding position of all contours
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 100:
                x, y, w, h = cv2.boundingRect(mask_contour)
                
                
                center_X_Ball = x+w//2
                center_Y_Ball = y+h//2
                center_X_Window = Window_X //2
                center_Y_Window = Window_Y //2
                
                
                center_coordinates_Ball = (center_X_Ball, center_Y_Ball)
                center_cooridonates_Window = (Window_X//2, Window_Y//2)


                centroid_Ball = np.array([center_X_Ball,center_Y_Ball])
                centroid_Window = np.array([center_X_Window, center_Y_Window])
                
                
                cv2.circle(video, center_coordinates_Ball, 2, (100, 0, 100), 3) #drawing center of detected object
                cv2.circle(video, center_cooridonates_Window, 2, (0, 0, 255), 3) #drawing center of detected object
                cv2.rectangle(video, (x, y), (x + w, y + h), (100, 0, 100), 1) #drawing rectangle of detected object
                cv2.line(video, (x+w//2, y), (x+w//2, y+h), (100, 0, 100), 1) #drawing Y line of detected object
                cv2.line(video, (x, y+h//2), (x+w, y+h//2), (100, 0, 100), 1) #drawing X line of detected object
                cv2.line(video, (center_X_Window, 0), (center_X_Window, Window_Y), (0, 0, 255), 1) #drawing X line of window
                cv2.line(video, (0, center_Y_Window), (Window_X, center_Y_Window), (0, 0, 255), 1) #drawin Y line of window


                #Conditions for finding where the ball is situated
                if centroid_Ball[1] > centroid_Window[1]:
                    print("down")
                if centroid_Ball[1] < centroid_Window[1]:
                    print("up")
                if centroid_Ball[0] > centroid_Window[0]:
                    print("right")
                if centroid_Ball[0] < centroid_Window[0]:
                    print("left")
                
                pts.appendleft(centroid_Ball)
                
                
                #Drawing a trace of the detected object
                for i in range(1, len(pts)):
                    # if either of the tracked points are None, ignore
                    # them
                    if pts[i - 1] is None or pts[i] is None:
                        continue
             
                    # otherwise, compute the thickness of the line and
                    # draw the connecting lines
                    thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 1.5)
                    cv2.line(video, pts[i - 1], pts[i], (100, 0, 100), thickness)



    cv2.imshow("mask image", mask) # Displaying mask image

    cv2.imshow("window", video) # Displaying webcam image

    cv2.waitKey(1)