#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:30:27 2019

@author: tvpc00014
"""
import os
import re
import cv2
import imutils
import tempfile
import urllib
import pytesseract
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.preprocessing.image import img_to_array, load_img


WORKING_DIR = os.getcwd()
#def show_image(dis_image, file_name):
#    cv2.imshow(file_name, dis_image)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()




def get_detection_df(firebase_path):
    interpreter = tf.lite.Interpreter(model_path=os.path.join(WORKING_DIR,'common/Modeling_Code/aadhar_27_9_2019__model_tflite.tflite'))
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    '''takes firebase http url and returns
       the detection in form of a dataframe'''
    image = imutils.url_to_image(firebase_path)


    #req = urllib.urlopen(firebase_path)
    #arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    #img = cv2.imdecode(arr, -1) # 'Load it as it is'

    if image is not None:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        cv2.imwrite(temp_file.name, image)


        x_img = load_img(temp_file.name, target_size=(300, 300))
        x_img = img_to_array(x_img) / 255
        img = np.expand_dims(x_img, axis=0)
        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        (height, width, _) = image.shape

        result_data = pd.DataFrame(output_data[0], columns=['y1', 'x1', 'y2', 'x2'])
        output_data = interpreter.get_tensor(output_details[1]['index'])
        result_data['class'] = list(output_data[0])
        output_data = interpreter.get_tensor(output_details[2]['index'])
        result_data['score'] = list(output_data[0])
        result_data['x1'] = (result_data['x1']*width).astype(int)
        result_data['y1'] = (result_data['y1']*height).astype(int)
        result_data['x2'] = (result_data['x2']*width).astype(int)
        result_data['y2'] = (result_data['y2']*height).astype(int)

    return result_data, image

def get_detection_pan(firebase_path):
    interpreter = tf.lite.Interpreter(model_path=os.path.join(WORKING_DIR,'common/Modeling_Code/pan_data_extraction_28_10_2019__model_tflite.tflite'))
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    '''takes firebase http url and returns
       the detection in form of a dataframe'''
    image = imutils.url_to_image(firebase_path)


    #req = urllib.urlopen(firebase_path)
    #arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    #img = cv2.imdecode(arr, -1) # 'Load it as it is'

    if image is not None:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        cv2.imwrite(temp_file.name, image)


        x_img = load_img(temp_file.name, target_size=(300, 300))
        x_img = img_to_array(x_img) / 255
        img = np.expand_dims(x_img, axis=0)
        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        (height, width, _) = image.shape

        result_data = pd.DataFrame(output_data[0], columns=['y1', 'x1', 'y2', 'x2'])
        output_data = interpreter.get_tensor(output_details[1]['index'])
        result_data['class'] = list(output_data[0])
        output_data = interpreter.get_tensor(output_details[2]['index'])
        result_data['score'] = list(output_data[0])
        result_data['x1'] = (result_data['x1']*width).astype(int)
        result_data['y1'] = (result_data['y1']*height).astype(int)
        result_data['x2'] = (result_data['x2']*width).astype(int)
        result_data['y2'] = (result_data['y2']*height).astype(int)

    return result_data, image


def detect_text_adhar_front(firebase_path):

    '''takes a firebase http url and returns the details of aadhar (front)'''

    Result_Data, image = get_detection_df(firebase_path)
    name    = "Name couldn't be extracted. Please try again."
    dob     = "Date of Birth couldn't be extracted. Please try again."
    gender  = "Gender couldn't be extracted. Please try again."
    number  = "Aadhar number couldn't be extracted. Please try again."

    for _index, detection in Result_Data.iterrows():
        confidence = detection['score']*100
        idx = int(detection['class'])

        if (confidence > 10 and idx == 0):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            name_img = image[start_y:end_y, start_x:end_x]
#                show_image(name_img, "Name")
            # gray = cv2.cvtColor(name_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            name_raw = pytesseract.image_to_string(name_img, config = custom_oem_psm_config)
            # name = re.search("(^[A-Za-z ,.'-]+$)", name_raw)
#             if name:
#                 name = name.group()
#             else:
#                 name = 'Data extraction failed. Please try again.'

# #                print("Name: ", name)
            name = name_raw
            if name == "":
                name = "The data could not be extracted."
        if (confidence > 10 and idx == 1):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            dob_img = image[start_y:end_y, start_x:end_x]
#                show_image(dob_img, "DoB")
            # gray = cv2.cvtColor(dob_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            dob_raw = pytesseract.image_to_string(dob_img, config = custom_oem_psm_config)
            dob = dob_raw.replace(' ', '')
#                dob = re.search('^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$', dob_raw)
#                if dob:
#                    dob = dob.group()
#                else:
#                    dob = ''

#                print("\n\nDoB: ", dob)
            if dob == "":
                dob = "The data could not be extracted."
        if (confidence > 10 and idx == 2):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            gender_img = image[start_y:end_y, start_x:end_x]
#                show_image(gender_img, "Gender")
            # gray = cv2.cvtColor(gender_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            gender_raw = pytesseract.image_to_string(gender_img, config = custom_oem_psm_config)
            if "female" in gender_raw.lower():
                gender = 'Female'
            else:
                gender = 'Male'

#                print("\n\nGender: ", gender)
            if gender == "":
                gender = "The data could not be extracted."
        if (confidence > 10 and idx == 3):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            no_img = image[start_y:end_y, start_x:end_x]
#                show_image(no_img, "Number")
            # gray = cv2.cvtColor(no_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            no_raw = pytesseract.image_to_string(no_img, config = custom_oem_psm_config)
            number = re.search(r'(\d{4}\s?\d{4}\s?\d{4})', no_raw)
            if number:
                number = number.group()
            else:
                number = 'Data extraction failed. Please try again.'
            if number == "":
                number = "The data could not be extracted."
#                print("\n\nNumber: ", number)
    return {"name": name, "dob": dob, "gender": gender, "number": number}


def detect_text_adhar_back(firebase_path):

    '''takes a firebase http url and returns the details of aadhar (back)'''

    Result_Data, image = get_detection_df(firebase_path)
    address = "Address couldn't be extracted. Please try again."

    for _index, detection in Result_Data.iterrows():
        confidence = detection['score']*100
        idx = int(detection['class'])

        if (confidence > 10 and idx == 5):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            address_img = image[start_y:end_y, start_x:end_x]
#                show_image(address_img, "Address")
            #gray = cv2.cvtColor(address_img, cv2.COLOR_RGB2GRAY)
            address = pytesseract.image_to_string(address_img)
#                print("\n\nAddress: ", address)
    return {"address": address}


def detect_text_pan_card(firebase_path):
    '''takes a firebase http url and returns the details of pancard'''
    Result_Data, image = get_detection_pan(firebase_path)
    
    pan_no    = "Pan Number couldn't be extracted. Please try again."
    pan_name     = "Name couldn't be extracted. Please try again."
    pan_dob  = "Date of birth couldn't be extracted. Please try again."
    

    for _index, detection in Result_Data.iterrows():
        confidence = detection['score']*100
        idx = int(detection['class'])
        if (confidence > 10 and idx == 1):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            no_img = image[start_y:end_y, start_x:end_x]
#                show_image(no_img, "Number")
            #gray = cv2.cvtColor(no_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            no_raw = pytesseract.image_to_string(no_img, config = custom_oem_psm_config)
            pan_no = no_raw
            if pan_no == "":
                pan_no = "The data could not be extracted."
            
        if (confidence > 10 and idx == 2):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            name_img = image[start_y:end_y, start_x:end_x]
#                show_image(name_img, "Name")
            #gray = cv2.cvtColor(name_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            name_raw = pytesseract.image_to_string(name_img, config = custom_oem_psm_config)
            # name = re.search("(^[A-Za-z ,.'-]+$)", name_raw)
            # if name:
            #     pan_name = name.group()
            # else:
            #     pan_name = 'Cropping is not exact. Please try again.'

#                print("Name: ", name)
            pan_name = name_raw
            if pan_name == "":
                pan_name = "The data could not be extracted."

        if (confidence > 10 and idx == 3):
            start_x, start_y = int(detection['x1']), int(detection['y1'])
            end_x, end_y = int(detection['x2']), int(detection['y2'])
            dob_img = image[start_y:end_y, start_x:end_x]
#                show_image(dob_img, "DoB")
            #gray = cv2.cvtColor(dob_img, cv2.COLOR_RGB2GRAY)
            custom_oem_psm_config = '--psm 6'
            dob_raw = pytesseract.image_to_string(dob_img, config = custom_oem_psm_config)
            pan_dob = dob_raw
            if pan_dob == "":
                pan_dob = "The data could not be extracted."
#                dob = re.search('^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$', dob_raw)
#                if dob:
#                    dob = dob.group()
#                else:
#                    dob = ''

#                print("\n\nDoB: ", dob)
    return {"name": pan_name, "dob": pan_dob, "number": pan_no}


# JSON = detect_text_adhar_front('https://firebasestorage.googleapis.com/v0/b/kyc-scanner.appspot.com/o/sample%2Ftest2_aadhar_front.jpg?alt=media&token=70506199-6367-4f7d-b6c4-cc35ab1ae853')
