#!/Users/smcho/virtualenv/riki/bin/python

# -*- coding: utf-8 -*-
import os

from wiki import create_app
from flask_socketio import SocketIO, emit, join_room

directory = os.getcwd()
app = create_app(directory)
io = SocketIO(app)

@io.on('join')
def on_join(client,room):
    join_room(room=room)
    emit('client_joined')

@io.on('disconnect')
def disconnect ():
    print 'user disconnected'

@io.on('exit')
def exit (room):
    disconnect()

@io.on('editor_title')
def handle(msg, room):
    emit('client_title', msg, room=room, broadcast=True)

@io.on('editor_body')
def handle(msg, room):
    emit('client_body', msg, room=room)

@io.on('editor_tags')
def handle(msg, room):
    emit('client_tags', msg, room=room, broadcast=True)

if __name__ == '__main__':
    io.run(app, host='0.0.0.0', debug=True)