from bson import ObjectId
from api.Models.DbModel.RoomModel import Room
from api.Models.DbModel.UserInRoom import UserInRoom
from api.Models.DbModel.UserModel import User

"""Cервис удаления и добавления юзера в комнату"""

#todo  check in client
class ServiceRoomUser:
    """Добавляем пользователя в комнату"""

    @staticmethod
    def insert_user_in_room(user, room):
        try:
            UserInRoom(user=User(id=user), room=Room(id=room))
        except Exception as e:
            print(e, 'ServiceRoomUser.insert_user_in_room')

    """Удаляем пользователя из комнаты"""

    @staticmethod
    def delete_user_in_room(user, room):
        try:
            UserInRoom.objects(user=ObjectId(user), room=ObjectId(room)).delete()
        except Exception as e:
            print(e, 'delete_user_in_room.insert_user_in_room')
