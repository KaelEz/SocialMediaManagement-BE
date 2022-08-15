import os

from flask import Flask
from app.routes.instagram import instagramApp
from app.routes.twitter import twitterApp
from app.routes.user import userApp

from app.utils import database

def create_app():
	app = Flask(__name__)

	# setup all our dependencies
	database.init_app(app)

	# register blueprint
	app.register_blueprint(instagramApp)
	app.register_blueprint(twitterApp)
	app.register_blueprint(userApp)
	
	return app

if __name__ == '__main__':
	create_app().run(debug = True)