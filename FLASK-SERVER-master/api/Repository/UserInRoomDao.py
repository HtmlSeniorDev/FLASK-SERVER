from .base_repo import get_conn


class UserInRoomDao:
    @staticmethod
    def insert_user_to_userinroom(kwargs):

        try:

            get_conn().db.userInRoom.insert(kwargs)

            return True

        except Exception as e:
            print('inser_user_to_userinroom', e)

            return False

    @staticmethod
    def delete_user_to_userinroom(kwargs):

        try:

            get_conn().db.userInRoom.delete_many(kwargs)

            return True

        except Exception as e:
            print('delete_user_to_userinroom', e)

            return False