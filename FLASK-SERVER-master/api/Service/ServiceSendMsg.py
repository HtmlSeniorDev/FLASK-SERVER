from datetime import datetime
from datetime import timedelta
from flask import jsonify
from bson.objectid import ObjectId
from db import mongo
from .ServicePushNotification import ServicePushNotification


class ServiceSendMsg:
    Push = ServicePushNotification()

    def send_message(self, nick, msg, type, place, attachments):

        if int(type) == 2:
            print(nick, place)
            self.Push.send_client_push(nick, msg, place)

        banned = mongo.db.users
        nick1 = (banned.find_one({'_id': ObjectId(str(nick))}))
        check_invisible = nick1['type']
        if check_invisible == 16 and type == 1:
            return jsonify({"send": False})

        if len(attachments) < 1:
            pass

        else:
            attachments = [str(attachments)]

        if len(msg) > 120 or msg == '':
            return jsonify({"send": False})

        mongo.db.messages.insert({

            "user": str(nick),
            "place": str(place),
            "message": str(msg),
            "createdAt": datetime.now() + timedelta(hours=5),
            "type": int(type),
            "attachments": attachments,
            "readed": True,
            "hideNic": False,
            "system": False,
            "_class": "ru.readme.server.object.db.DBMessage"
        })

        return jsonify({"send": True})
