print "Initializing ..."
import io
import time
import picamera
import picamera.array
import cv2
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('recognizer/trainner_lbph.yml')
Id=0

# create a 3x3 kernel
kernel_3x3 = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

stream = io.BytesIO()
font = cv2.FONT_HERSHEY_SIMPLEX

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

def getProfile(Id):
	conn=sqlite3.connect("FaceBase.db")
	cmd="SELECT * FROM Wideodomofon WHERE Id="+str(Id)
	cursor = conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close()
	return profile

with picamera.PiCamera() as camera:
            camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)

            
            while (True):
                with picamera.array.PiRGBArray(camera) as stream:
                    camera.capture(stream, format='bgr', use_video_port=True)

                    image = stream.array

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.filter2D(gray, -1, kernel_3x3)
                
                faces = face_cascade.detectMultiScale(image, 
                                scaleFactor=HAAR_SCALE_FACTOR, 
                                minNeighbors=HAAR_MIN_NEIGHBORS, 
                                minSize=HAAR_MIN_SIZE, 
                                flags=cv2.CASCADE_SCALE_IMAGE)
		
		for(x,y,w,h) in faces:
       			cv2.rectangle(gray,(x,y),(x+w,y+h),(225,0,0),2)
        		cv2.imshow('gray',cv2.resize(gray[y:y+h,x:x+w],(200,200)))
        		Id, conf = recognizer.predict(cv2.resize(gray[y:y+h,x:x+w],(200,200)))
        		profile = getProfile(Id)
			wyjscie = Id
			if(conf<73):
				cv2.putText(gray,str(Id), (x,y+h), font, 2, (0,255,255),2,cv2.LINE_AA)
            			
				if(profile!=None):
					cv2.putText(gray,profile[1], (x,y+h),font, 2,(0,255,255),2,cv2.LINE_AA)
					cv2.putText(gray,profile[2], (x,y+h+60),font, 2,(0,255,255),2,cv2.LINE_AA)
        		else:
            			Id="Unknown"
				cv2.putText(gray,"Unknown", (x,y+h),font, 2,(0,255,255),2,cv2.LINE_AA)
			conf = conf - 40
			conf = 100 - ((conf/140)*100)
	        	cv2.putText(gray,str(round(conf,2)), (x,y+h+120),font, 2,(0,255,255),2,cv2.LINE_AA)
		                
           	cv2.imshow('im',gray)     
		if (cv2.waitKey(10)==ord('q')):
			break
