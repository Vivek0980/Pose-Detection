import cv2
import time
import mediapipe as mp
import time
past_time=0
mpPose=mp.solutions.pose
mypose=mpPose.Pose()
mpdraw=mp.solutions.drawing_utils
video=cv2.VideoCapture("C:\\Users\\Admin\\Downloads\\3191289-uhd_4096_2160_25fps.mp4")
while True:
    ret,frame=video.read()
    resize_img=cv2.resize(frame,(700,700))
    img_rgb=cv2.cvtColor(resize_img,cv2.COLOR_BGR2RGB)
    results=mypose.process(img_rgb)
    if results.pose_landmarks:
        mpdraw.draw_landmarks(resize_img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,val in enumerate(results.pose_landmarks.landmark):
            h,w,c=resize_img.shape
            cx,cy=int(val.x*w),int(val.y*h)
            cv2.circle(resize_img,(cx,cy),3,color=(0,255,255),thickness=4)
    current_time=time.time()
    fps=1/(current_time-past_time)
    past_time=current_time
    cv2.putText(resize_img,str(int(fps)),(30,100),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,0),thickness=2)
    cv2.imshow('resize_img',resize_img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
#cv2.DestroyAllWindows()