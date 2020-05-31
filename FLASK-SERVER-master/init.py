from flask import Flask
from SERVER_CONFIG import MONGO_ADDRESS, MONGO_PORT, MONGO_USER, MONGO_PASS
from flask_cors import CORS
from flask_socketio import SocketIO
from mongoengine import connect, disconnect
from db import mongoEngine
from limiter import limiter
from api.Repository.base_repo import get_conn

socketio = SocketIO()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def create_app():
    app.config["MONGO_URI"] = "mongodb://" + MONGO_USER + ':' + MONGO_PASS + '@' + MONGO_ADDRESS + ":" + str(
        MONGO_PORT) + "/chat"
    app.config['SECRET_KEY'] = 'secret!'
    app.config["MONGODB_DB"] = 'chat'
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['MONGO_AUTH_SOURCE'] = 'admin'
    app.config["MONGODB_SETTINGS"] = {"DB": "chat"}

    limiter.init_app(app)
    get_conn().init_app(app)
    mongoEngine.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*", async_mode='threading', logger=True, ping_timeout=300,
                      engineio_logger=True)
    disconnect()
    connect(
        'chat',
        host="mongodb://" + MONGO_ADDRESS + ":" + str(MONGO_PORT) + "/chat",
        port=27017,
        username=MONGO_USER,
        password=MONGO_PASS,
    )

    return app
