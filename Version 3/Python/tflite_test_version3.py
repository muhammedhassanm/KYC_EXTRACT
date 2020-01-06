# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:49:42 2019
@author: Vivekanandan | Techvantage
"""
import cv2
import time
import imutils
import warnings
import pytesseract 
import numpy as np
import pandas as pd
from imutils.video import FPS
import PIL.ImageDraw as ImageDraw 
import PIL.ImageFont as ImageFont
import PIL.ImageColor as ImageColor
from matplotlib import pyplot as plt
from imutils.video import VideoStream
from keras.preprocessing.image import  array_to_img, img_to_array, load_img
with warnings.catch_warnings():  
    warnings.filterwarnings("ignore",category=FutureWarning)
    import tensorflow as tf

size = (300, 300)
def transform_image(size):
    # function for transforming images into a format supported by CNN
    x = load_img('aa.jpg', target_size=(size[0], size[1]) )
    x = img_to_array(x) / 255
    x = np.expand_dims(x, axis=0)
    return (x)

def show_image(IMAGE):
    plt.figure(figsize=(10,10))
    plt.imshow(IMAGE, aspect = 'auto')
    plt.show()

interpreter = tf.lite.Interpreter(model_path='C:/Users/100119/Desktop/model_tflite_21_11_2019 _kyc_latest.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']
CLASSES = ["cow", "cow_face", "unblurred_muzzle", "cow_eye", "cow_eye",
     "cow_ear", "cow_ear", "cow_eartag", "laptop", "mobile", "cup", "chair",
     "pen", "mouse", "monitor", "book", "bottle", "key_board",
     "tablet", "person", "eye_glass","cpu","blurred_muzzle", "adhar_front", "adhar_back", "pan", "license","atm","business_card","office_id","paper"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

image ='C:/Users/100119/Pictures/Saved Pictures/pdf_img_2/yildiz_iicai05_13.jpg'
frame = cv2.imread(image)
(h, w) = frame.shape[:2]
cv2.imwrite('aa.jpg',frame)
img = transform_image(size)
interpreter.set_tensor(input_details[0]['index'], img)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
Result_Data = pd.DataFrame(output_data[0],columns=['y1','x1','y2','x2'])
output_data = interpreter.get_tensor(output_details[1]['index'])
Result_Data['class'] = list(output_data[0])
output_data = interpreter.get_tensor(output_details[2]['index'])
Result_Data['score'] = list(output_data[0])
Result_Data['score'] = Result_Data['score'] * 100
Result_Data['x1'] = (Result_Data['x1']*w).astype(int)
Result_Data['y1'] = (Result_Data['y1']*h).astype(int)
Result_Data['x2'] = (Result_Data['x2']*w).astype(int)
Result_Data['y2'] = (Result_Data['y2']*h).astype(int)

count =1
for index,detection  in Result_Data.iterrows():
    confidence = int(detection['score']) 
    if confidence >10:
            idx = int(detection['class'])
            (startX, startY, endX, endY) = detection['x1'].astype("int"),detection['y1'].astype("int"),detection['x2'].astype("int"),detection['y2'].astype("int")
            crop=frame[startY:endY,startX:endX]
            crop = cv2.resize(crop,None,fx=2.5,fy =2.5)
            cv2.imwrite('E:/Desktop/KYC_EXTRACT/Version1/test-images/' +str(count)+'.jpg',crop)
            count+=1
#                gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
#                retval, thresh_gray = cv2.threshold(g, thresh=75, maxval=255,type=cv2.THRESH_BINARY_INV)
            cv2.imshow('crop',crop)
            cv2.waitKey(0)
#            if int(detection['class']) != 4 and int(detection['class']) != 6 :
#                print(int(detection['class']))
#                custom_oem_psm_config = '--psm 6'
#                text= pytesseract.image_to_string(crop,config = custom_oem_psm_config)
            if int(detection['class']) != 0:
               
                print(int(detection['class']))
               
                text= pytesseract.image_to_string(crop,config = '--psm 3')
                
                print(text)
            #cv2.imshow('crop',crop)
            #cv2.waitKey(0)
            # draw the prediction on the frame
            label = "{}: {:.2f}%".format(CLASSES[idx],confidence)
            cv2.rectangle(frame, (startX, startY), (endX, endY),COLORS[idx], 3)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 4)

cv2.imshow("Frame", cv2.resize(frame,(400,400)))
cv2.waitKey(0)

cv2.destroyAllWindows()
