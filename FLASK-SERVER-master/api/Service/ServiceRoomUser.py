
from api.Repository.UserInRoomDao import UserInRoomDao


class ServiceRoomUser:
    ROOM = UserInRoomDao()

    def insert_user_in_room(self, user, room):

        try:
            self.ROOM.insert_user_to_userinroom({"user": user, "room": room})

        except Exception as e:

            print(e, 'ServiceRoomUser.insert_user_in_room')
            pass

    def delete_user_in_room(self,user,room):
        try:
            self.ROOM.delete_user_to_userinroom({"user": user, "room": room})

        except Exception as e:

            print(e, 'delete_user_in_room.insert_user_in_room')
            pass