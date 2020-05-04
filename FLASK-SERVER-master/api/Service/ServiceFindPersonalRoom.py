from ..Objects.Server_id import SERVER_ID
from bson.json_util import dumps
from bson.objectid import ObjectId
from ..Repository.PersonalRoomsDao import PersonalRoomsDao
from ..Repository.UsersDao import UsersDao
from ..Repository.MessagesDao import MessagesDao

import json


# todo переделать через модель
class ServiceFindPersonalRooms:
    Private = PersonalRoomsDao()
    USERS = UsersDao()
    MESSAGES = MessagesDao()
    last_msg = None

    def find_personal_server(self, my_id) -> str:
        try:

            USER_ARRAY = [SERVER_ID, my_id]

            room = dumps(self.Private.find_array_user_to_id_room({'users': USER_ARRAY, 'hides': []}))

            if room == 'null':
                create_room = ({
                    "hides": [],
                    "users": USER_ARRAY,
                    "_class": "ru.readme.server.object.db.DBPersonalRoom"

                })
                print('room create')
                self.Private.create_pm_rooms(create_room)

                return self.find_personal_server(my_id)

            serialize_room = json.loads(room)
            room = serialize_room['_id']['$oid']
            return room

        except Exception as e:

            print('find_personal_server', e)
            pass

    def find_personal_rooms(self, my_id) -> list:
        try:
            list_private = []

            rooms = dumps(self.Private.find_personalrooms_user_id({'users': my_id, 'hides': []}))
            for room in json.loads(rooms):  # Идем по списку персональных комнат
                serialize_room = room
                room = serialize_room['_id']['$oid']
                serialize_room['room_id'] = str(room)
                message_last = (self.MESSAGES.read_message_pm_last({'place': room}))

                for message in message_last:  # формируем последнее сообщение ,его время,и статус прочитано или нет.
                    serialize_room['last_msg'] = message['message']
                    serialize_room['last_time'] = message['createdAt']
                    serialize_room['readed'] = message['readed']
                    self.last_msg = message['message']

                # Заполняем поле от кого
                if serialize_room['users'][0] == my_id:

                    # Если ник == моему нику не
                    # показывать в списке личных сообщений а сменить на второго пользователя массива

                    user_id = serialize_room['users'][1]
                    information_user = self.USERS.get_information_user(user_id)
                    serialize_room['private_nick'] = information_user['nic']

                else:

                    user_id = serialize_room['users'][0]
                    information_user = self.USERS.get_information_user(user_id)
                    serialize_room['private_nick'] = information_user['nic']

                del serialize_room['_class']
                del serialize_room['_id']
                del serialize_room['hides']
                del serialize_room['users']
                list_private.append(serialize_room)

            return list_private

        except Exception as e:

            print('find_personal_rooms', e)
            pass
