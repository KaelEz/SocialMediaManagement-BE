from flask import Blueprint, jsonify, request
from flask_cors import CORS

userApp = Blueprint('userApp', __name__)
CORS(userApp) # enable CORS on the userApp

@userApp.route('/user')
def index():
    return "Hai user"