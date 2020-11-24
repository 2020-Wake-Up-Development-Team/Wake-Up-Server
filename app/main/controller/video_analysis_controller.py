from flask import Blueprint, request, jsonify, Response
import wget
import urllib.request
import cv2
from focus import GazeTracking
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import pymysql
import date
api = Blueprint("video_analysis", __name__, url_prefix="/video_analysis")
gaze = GazeTracking()
is_watching={-1:'not looking',0:"blinking",1:"focusing"}

print('model loading...')
detector = hub.load("https://tfhub.dev/tensorflow/centernet/hourglass_512x512/1")
print('model is loaded')

conn = pymysql.connect(host='localhost', user='root', password='woungsub',
                       db='wakeupdb', charset='utf8')

'''idx = Column(Integer, autoincrement=True, primary_key=True)
    id = Column(String(30), ForeignKey("USERS_TB.id"), nullable=False)
    phone = Column(Integer, nullable=False)
    sleep = Column(Integer, nullable=False)
    eating = Column(Integer, nullable=False)
    concentration = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)'''

@api.route("/<id>", methods=["POST"])
def get_videofile(id):
    curs = conn.cursor()
    data = request.get_json() 
    try:
        if not urllib.request.urlopen(data["url"]).status == 200:
            return jsonify({"message": "invalid url", "status": 400})
        
        video_file = wget.download(data["url"])
        cap = cv2.VideoCapture('video_file')
        time_tracker = 0
        sleeping_cnt = 0
        is_sleep = 0
        focus_count = 0
        frame_count = 0
        phone_count = 0

        try:
            while cap.isOpened():
                _,frame = cap.read()
                tensor = tf.image.convert_image_dtype(frame,tf.uint8)
                tensor = tf.expand_dims(tensor,axis= 0)
                detector_output = detector(tensor)
                class_ids = detector_output["detection_classes"]
                class_ids = list(np.int64(class_ids.numpy().squeeze()))
                scores = detector_output["detection_scores"]
                class_scores = list(np.float64(scores.numpy().squeeze()))

                try:
                    id = class_ids.index(77)
                except:
                    if class_scores[id]>0.85:
                        phone_count+=1 
                    
                gaze.refresh(frame)
                frame_count+=1

                if sleeping_cnt >20:
                    is_sleep+=1 
                if gaze.is_center():
                    text = "focusing"
                    focus_count+=1
                    sleeping_cnt = 0
                else:
                    if gaze.is_blinking():
                        sleeping_cnt+=1
                    else:  
                        pass
        except:
            pass 
        sql = """insert into CONCENTRATION_TB(id,phone,sleep,concentration,all_frame,created_at)
         values (%s, %s, %s, %s, %s, %s)"""       
        curs.execute(id,phone_count,is_sleep,focus_count,frame_count,date.today())
        #focus_persentage = fo1cus_count/length
        #sleep_persentage = is_sleep/length
            
        '''return
            frame_count,
            focus_count,
            is_sleep
            phone_count'''

        # video_file 처리
        return jsonify({"status": 200})

    except Exception as err:
        return jsonify({"status": 400, "message": "Fail"})
