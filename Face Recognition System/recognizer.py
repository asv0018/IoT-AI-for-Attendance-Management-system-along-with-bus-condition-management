import RPi.GPIO as gpio
import cv2
#import xlwrite,firebase.firebase_ini as fire;
import time as tim
import sys
import requests
from datetime import *
import csv



def SetAngle(angle):
    duty=angle/18 + 2
    gpio.output(3,True)
    pwm.ChangeDutyCycle(duty)
    tim.sleep(1)
    gpio.output(3,False)
    pwm.ChangeDutyCycle(0)


    
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
pwm=gpio.PWM(3,50)
pwm.start(0)
studentsinthebus=0
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("attempting to turn camera on");
cap = cv2.VideoCapture(0);
print("attempt to turn camera was successful")
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');
flag = 0;
id=0;
filename='filename';
local_database_name={
   "23":"aishwarya",
   "103":"arun",
   "12":"raghu sir",
   '55':'gopalam'
    }
dict = {
            'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    img=cv2.flip(img,1)
    position = (10,50)
    cv2.putText(
         img, #numpy array on which text is written
         "NO.OF.STD : "+str(studentsinthebus), #text
         position, #position at which writing has to start
         cv2.FONT_HERSHEY_SIMPLEX, #font family
         1, #font size
         (5,255,255), #font color
         3) #font stroke
    cv2.imshow("face recognition",img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id,conf=recognizer.predict(roi_gray)
        if str(id) in local_database_name:
            URL="http://aishwarya.thinkfinitylabs.com/insert_into_attendance.php?"
            now=datetime.now()
            parameters={'id':str(id),'name':local_database_name[str(id)],'time':(now.strftime("%H:%M"))}
            #print(URL+str(parameters))
            response=requests.get(url=URL,params=parameters,headers={"User-Agent": "XY"})
            print(response.text)
            if response:
                data=response.json()
                status=data["success"]
                message=None
                
                if(str(status)=='2'):
                    message=data["message"]
                    print(message)
                    studentsinthebus=studentsinthebus+1
                    print('number of students in the bus is : '+str(studentsinthebus))
                    cv2.putText(img,'Howdy ! '+local_database_name[str(id)]+'attendance provided to you just now.',(x,y-10),font,0.55,(120,255,120),1)
                    position = (10,50)
                    cv2.putText(
                    img, #numpy array on which text is written
                    "NO.OF.STD : "+str(studentsinthebus), #text
                    position, #position at which writing has to start
                    cv2.FONT_HERSHEY_SIMPLEX, #font family
                    1, #font size
                    (5,255,255), #font color
                    3) #font stroke
                    cv2.imshow('face recognition',img)
                    if studentsinthebus==50:
                        SetAngle(90)
                        
                if(str(status)=='1'):
                    message=data["message"]
                    cv2.putText(img,'attendance for '+local_database_name[str(id)]+' already given.',(x,y-10),font,0.55,(120,255,120),1)
                    cv2.imshow('face recognition',img)
                    position = (10,50)
                    cv2.putText(
                    img, #numpy array on which text is written
                    "NO.OF.STD : "+str(studentsinthebus), #text
                    position, #position at which writing has to start
                    cv2.FONT_HERSHEY_SIMPLEX, #font family
                    1, #font size
                    (5,255,255), #font color
                    3) #font stroke
                    
                    
                    print(message)
                    print('number of students in the bus is : '+str(studentsinthebus))
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        print("keyboard interrupt")
        break

cap.release();
cv2.destroyAllWindows();
pwm.stop()
gpio.cleanup()


