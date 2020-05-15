from datetime import datetime
from datetime import timedelta
from api.Repository.MessagesDao import MessagesDao
from api.Repository.PersonalRoomsDao import PersonalRoomsDao
import json
from bson.json_util import dumps
from api.utils.Server_id import SERVER_ID


class ServiceMessages:
    Messages = MessagesDao()
    Pm_rooms = PersonalRoomsDao()

    def logging_sender(self, id_user, id_banner, name_admin):  # доделать список кто снимает
        try:

            object_document = {

                "user": str(id_banner),
                "place": "777f1f1f1f1f",
                "message": str(name_admin) + "разбанил пользователя" + str(id_user),
                "createdAt": datetime.now() + timedelta(hours=5),
                "type": 1,
                "attachments": [],
                "readed": False,
                "hideNic": False,
                "system": False,
                "_class": "ru.readme.server.object.db.DBMessage"
            }

            self.Messages.send_message(object_document)

            return True

        except Exception as e:
            print(e)

            return False

    def send_pm_with_server(self, id_user, id_banner, name_admin):  # доделать список кто снимает
        try:

            object_document = {

                "user": str(id_banner),
                "place": "777f1f1f1f1f",
                "message": str(name_admin) + "разбанил пользователя" + str(id_user),
                "createdAt": datetime.now() + timedelta(hours=5),
                "type": 1,
                "attachments": [],
                "readed": False,
                "hideNic": False,
                "system": False,
                "_class": "ru.readme.server.object.db.DBMessage"
            }

            self.Messages.send_message(object_document)

            return True

        except Exception as e:
            print(e)

            return False

    def create_rooms(self, user_id1, user_id2, message):  #
        print('create')

        room_object = {'users': [str(user_id1),
                                 str(user_id2)],
                       "hides": []}  # server_id user_id1

        check_rooms = dumps(self.Pm_rooms.get_user_array(room_object))
        print('hel')
        if check_rooms == 'null':
            add_room = {

                "hides": [],
                "users": [user_id1, user_id2],
                "_class": "ru.readme.server.object.db.DBPersonalRoom"

            }
            self.Pm_rooms.create_pm_rooms(add_room)

            return self.create_rooms(user_id1, user_id2, message)

        load_room_id = json.loads(check_rooms)
        id_room = load_room_id['_id']['$oid']

        return self.send_message_private_post(id_room, message)

    def send_message_private_post(self, place, message):

        try:
            send_msg = {

                "user": SERVER_ID,
                "place": str(place),
                "message": str(message),
                "createdAt": datetime.now() + timedelta(hours=5),
                "type": 2,
                "attachments": [],
                "readed": False,
                "hideNic": False,
                "system": False,
                "_class": "ru.readme.server.object.db.DBMessage"
            }

            self.Messages.send_message(send_msg)

            return True

        except Exception as e:
            print(e)
