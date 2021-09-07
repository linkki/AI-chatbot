# Copyright (c) 2021 Veera Lupunen

from flask import session
from flask_socketio import emit, join_room, leave_room
from . import socketio

@socketio.on('text', namespace='/chat')
def message(message):
    #New message is written by the chatter.
    room = session.get('room')
    name = session.get('name')
    emit('message', {'name': name, 'message': message}, room=room)
    
@socketio.on('leave', namespace='/chat')
def leave(message):
    #A chatter leaves the room.
    room = session.get('room')
    name = session.get('name')
    emit('status', {'name': name + 'poistui keskustelusta'}, room=room)
  
#New chatter has joined the room
    