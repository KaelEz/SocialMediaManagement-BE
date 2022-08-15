from flask import Blueprint, jsonify, request
from flask_cors import CORS

instagramApp = Blueprint('instagramApp', __name__)
CORS(instagramApp) # enable CORS on the instagramApp

@instagramApp.route('/ig')
def index():
    return "Hai ig"