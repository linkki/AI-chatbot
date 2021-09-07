# Copyright (c) 2021 Veera Lupunen

from flask import session
from flask_socketio import emit, join_room, leave_room
from . import socketio
from .ai_chat import ai_answer
import sys

@socketio.on('joined', namespace='/chat')
def join(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'message': "joku liittyi keskusteluun"}, room=room)

@socketio.on('text', namespace='/chat')
def message(message):
    #New message is written by the chatter.
    #sys.stderr.write("messagea kutsuttu\n")
    room = session.get('room')
    name = session.get('name')
    emit('message', {'name': name, 'message': message}, room=room)
    
    if session.get('ai'):
        #Kutsutaan ai_chat-moduulin funktiota
        emit('message', {'name': "salainen ystävä", 'message': ai_answer()}, room=room)
    
@socketio.on('leave', namespace='/chat')
def leave(message):
    #A chatter leaves the room.
    room = session.get('room')
    name = session.get('name')
    emit('status', {'name': name + 'poistui keskustelusta'}, room=room)
  
#TO-DO New chatter has joined the room
    