from flask import request
from app import app

@app.route('/')
def index():
    return "Hai Sonovabic"