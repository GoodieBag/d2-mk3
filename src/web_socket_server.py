import eventlet
import socketio
from lib.bot import Bot

sio = socketio.Server(cors_allowed_origins='https://diggibot.surge.sh')
app = socketio.WSGIApp(sio)

bot = Bot()

def handle_movements(command):
    if command == 'forward':
        bot.move_forwards()
    if command == 'backward':
        bot.move_backwards()
    if command == 'left':
        bot.turn_left()
    if command == 'right':
        bot.turn_right()

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def message(sid, data):
    print('message ', data)
    handle_movements(data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 3000)), app)