"""This is init module."""
from flask import Flask
from flask_restful import Api
import os
from Main.Routes.routes import initialize_routes
from flask_cors import CORS

# Place where app is defined
app = Flask(__name__)

api = Api(app)
CORS(app, resources={r'/*':{"origins": "*"}},allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Methods"])
#CORS(app)


initialize_routes(api)

