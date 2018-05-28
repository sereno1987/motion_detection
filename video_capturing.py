import cv2, pandas
from datetime import datetime


first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["start","end"])
video =cv2.VideoCapture(0)
a = 1
while True:
    a=a+1
    print(video.isOpened())
    # for time recording
    status = 0
    #
    check,frame=video.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # remove noises from frame. width and height and standard deviation
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    # in the first iteration its None coz of our assignment. it will get the first frae of the video
    if first_frame is None:
        first_frame= gray
        # goes to the next iteraion
        continue



    # calculating the difference between frames (first frame and current frame). it produces a neww image
    delta_frames=cv2.absdiff(first_frame,gray)
    # if its less than 30 concider it as black otherwise
    thresh_frame= cv2.threshold(delta_frames, 30, 255, cv2.THRESH_BINARY)[1]
    # time.sleep(2)
    # now make the thresh_frame somooter using dilate method
    thresh_frame = cv2.dilate(thresh_frame,None,iterations=2)


#countours. the second arg will draw the countour and the third is the method to draw
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        # for biigger object is 10000
        if cv2.contourArea(contour)<10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        # passing the color frame
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    # for the sake of memory we just nedd thw last two items
    status_list=status_list[-2:]
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())


    cv2.imshow("capture", gray)
    cv2.imshow("cqqapture1", delta_frames)
    cv2.imshow("thresh", thresh_frame)
    cv2.imshow("Color Frame", frame)
    #print(delta_frames)
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break
print(status_list)
print(times)

for i in  range(0 , len(times) , 2):
    df = df.append({"start":times[i] , "end":times[i+1]} , ignore_index=True)
df.to_csv("times.csv")
# print(a)
video.release()
cv2.destroyAllWindows()
