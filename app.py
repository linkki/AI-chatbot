# Copyright (c) 2021 Veera Lupunen

from app import app, socketio

if __name__ == '__main__':
    socketio.run(app)