from bson import ObjectId
from api.Models.DbModel.RoomModel import Room
from api.Models.DbModel.UserInRoom import UserInRoom
from api.Models.DbModel.UserModel import User

"""Cервис удаления и добавления юзера в комнату"""


# todo  check in client
class ServiceRoomUser:
    """Добавляем пользователя в комнату"""

    @staticmethod
    def insert_user_in_room(user, room):
        try:
            try:
                UserInRoom.objects.get(user=User(id=user))
            except Exception as e:
                UserInRoom(user=User(id=user), room=Room(id=room)).save()
                user_db = User.objects.get(id=ObjectId(user))
                user_db.online = True
                user_db.save()
        except Exception as e:
            print(e, 'ServiceRoomUser.insert_user_in_room')

    """Удаляем пользователя из комнаты"""

    @staticmethod
    def delete_user_in_room(user, room):
        try:
            if UserInRoom.objects.get(user=User(id=user)) is not None:
                UserInRoom.objects(user=ObjectId(user)).delete()
                user_db = User.objects.get(id=ObjectId(user))
                user_db.online = False
                user_db.save()
        except Exception as e:
            print(e, 'delete_user_in_room.insert_user_in_room')
