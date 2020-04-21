from flask import Flask
from SERVER_CONFIG import MONGO_ADDRESS, MONGO_PORT
from flask_cors import CORS
from flask_socketio import SocketIO
from mongoengine import connect, disconnect

socketio = SocketIO()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def create_app():
    app.config["MONGO_URI"] = "mongodb://" + MONGO_ADDRESS + ":" + str(MONGO_PORT) + "/chat"
    app.config['SECRET_KEY'] = 'secret!'
    app.config["MONGODB_DB"] = 'chat'
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config["MONGODB_SETTINGS"] = {"DB": "chat"}

    from db import mongo, mongoEngine
    from limiter import limiter
    limiter.init_app(app)
    mongo.init_app(app)
    mongoEngine.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*", async_mode='threading', logger=True, ping_timeout=30,
                      engineio_logger=True)
    disconnect()
    connect(
        'chat',
        host="mongodb://" + MONGO_ADDRESS + ":" + str(MONGO_PORT) + "/chat",
        port=27017
    )

    return app
