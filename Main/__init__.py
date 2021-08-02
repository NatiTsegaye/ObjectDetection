"""This is init module."""
#from flask_restful import Api
from flask import Flask, Response, request
import os
import tensorflow as tf
import numpy as np
from PIL import Image 
#from Main.Routes.routes import initialize_routes
#from flask_cors import CORS
# Place where app is defined
app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'Main/api/uploads'
#api = Api(app)
#CORS(app, resources={r'/api/*':{"origins": "*"}},allow_headers=[
 #   "Content-Type", "Authorization", "Access-Control-Allow-Methods"])
#CORS(app)

#initialize_routes(api)


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
            
    @app.route('/api/image', methods=['POST']) 
    def post():
        image = request.files.get('image','')
        img = Image.open(image)
        #filename = image.filename
        #file_path = os.path.join('Main/api/uploads',filename)
        #image.save(file_path)
        result = prediction(img)
        #os.remove('Main/api/tr.jpg')
        return {'Response': result}
