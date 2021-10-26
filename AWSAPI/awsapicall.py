from flask import Flask, json, request
import boto3
import json
import os
from PIL import Image
import mysql.connector
from cv2 import cv2
import time


def most_frequent(List): 
    return max(set(List), key = List.count) 

ListE = []
filepath = 'aa.mp4'

rekognition = boto3.client('rekognition', region_name='us-west-2')
api = Flask(__name__)


os.startfile(filepath)
        print(6)
        for i in range(10):
            print(7)
            return_value, image = camera.read()
            print(8)
            cv2.imwrite('image'+str(i)+'.jpg', image)
            print(3)
            with open('image'+str(i)+'.jpg', 'rb') as image_data: response_content = image_data.read()
            print(4)
            rekognition_response = rekognition.detect_faces(Image={'Bytes':response_content}, Attributes=['ALL'])
            print(5)
            jdump = json.dumps(rekognition_response)
            if os.path.exists('image'+str(i)+'.jpg'):
              os.remove('image'+str(i)+'.jpg')
            else:
              print("The file does not exist")
            jobject = json.loads(jdump)
            emotion_type = jobject["FaceDetails"][0]["Emotions"][0]["Type"]
            print(emotion_type)
            ListE.append(emotion_type)