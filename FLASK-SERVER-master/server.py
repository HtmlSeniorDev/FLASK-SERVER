from sys import getdefaultencoding
from SERVER_CONFIG import SERVER_ADDRESS, SERVER_PORT
from background import scheduler
from blueprints import app
from init import socketio

getdefaultencoding()
scheduler.start()
if __name__ == '__main__':
    socketio.run(app, port=SERVER_PORT, host=SERVER_ADDRESS, debug=True)  # 79.174.12.77
