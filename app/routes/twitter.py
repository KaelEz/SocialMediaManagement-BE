from flask import Blueprint, jsonify, request
from flask_cors import CORS

twitterApp = Blueprint('twitterApp', __name__)
CORS(twitterApp) # enable CORS on the instagramApp

@twitterApp.route('/twt')
def index():
    return "Hai twt"