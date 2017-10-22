import os
from flask import Flask
def create_app(config=None):
    app = Flask('flaskr')
    app.config['SECRET_KEY'] = 'I have a dream'
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+"/images"
    app.config.update(config or {})
    return app