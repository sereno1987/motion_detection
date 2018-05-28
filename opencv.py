import cv2, time
import numpy as np

first_frame=None
video =cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    print(video.isOpened())
    check,frame=video.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # remove noises from frame. width and height and standard deviation
    gray=cv2.GaussianBlur(gray,(21,21),0)
    # in the first iteration its None coz of our assignment. it will get the first frae of the video
    if first_frame is None:
        first_frame=gray
        #goes to the next iteraion
        continue

    #calculating the difference between frames (first frame and current frame). it produces a neww image
    delta_frames=cv2.absdiff(first_frame,gray)
    #time.sleep(2)
    cv2.imshow("capture", gray)
    cv2.imshow("capture1", delta_frames)
    print(delta_frames)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
