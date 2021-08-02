from flask import Flask, request
from flask_restful import Resource
import tensorflow as tf
import numpy as np
from PIL import Image 
import os

label_map ={'Crab': 0,
 'Haddock': 1,
 'Hake': 2,
 'Ling': 3,
 'Octopus': 4,
 'Plaice, European': 5,
 'Ray': 6,
 'Sardine': 7}

model = tf.keras.models.load_model('Main/api/myModel')

def prediction(image):    

    #img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img = image.resize((224,224))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
    preds = model.predict(x)
    #print('Predictions', preds)
    
    for pred, value in label_map.items():    
        if value == np.argmax(preds):
            print('Predicted class is:', pred)
            print('With a confidence score of: ', np.max(preds))
            return {
                "Prediction" : pred, 
                "Confidence" : str(np.max(preds))
            }
            
        
class ImageApi(Resource):
    def post(self):
        image = request.files.get('image','')
        img = Image.open(image)
        result = prediction(img)
        return {'Response': result}

    def get(self):
        return {'Resource':'APi Running'}
