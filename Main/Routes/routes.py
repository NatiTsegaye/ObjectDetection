from api.image_detection_api import ImageApi


def initialize_routes(api):
    #Get: check to see if APi is running 
    #POST: send image for prediction 
    api.add_resource(ImageApi,'/api/image')
