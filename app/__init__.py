# Copyright (c) 2021 Veera Lupunen

from flask_socketio import SocketIO
from flask import Flask
from os import getenv
import logging

socketio = SocketIO()

app = Flask(__name__)
app.debug = True #vaihda myöhemmin: luetaan ympäristömuuttujasta
app.secret_key = getenv("SECRET_KEY")
    
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    
socketio.init_app(app)

from . import routes, chat