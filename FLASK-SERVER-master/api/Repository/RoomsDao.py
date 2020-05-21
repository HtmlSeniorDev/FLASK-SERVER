from .base_repo import get_conn
from bson.objectid import ObjectId


class RoomsDao:
    @staticmethod
    def get_rooms(kwargs):
        try:
            response = get_conn().db.chatrooms.find(kwargs)

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def get_category(kwargs):
        try:
            response = get_conn().db.categories.find(kwargs)

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def get_user_room(kwargs):
        try:
            response = get_conn().db.userInRoom.find(kwargs)

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def update_category(kwargs, category_id):
        try:
            get_conn().db.categories.find_one_and_update({'_id': ObjectId(category_id)},
                                                         {"$set": kwargs})

            return True

        except Exception as e:
            print(e, 'RoomsDao.update_category')
            return False

    @staticmethod
    def update_room(kwargs, category_id):
        try:
            get_conn().db.chatrooms.find_one_and_update({'_id': ObjectId(category_id)},
                                                        {"$set": kwargs})

            return True

        except Exception as e:
            print(e, 'RoomsDao.update_category')
            return False

    @staticmethod
    def create_category(kwargs):
        try:
            get_conn().db.categories.insert(kwargs)

            return True

        except Exception as e:
            print(e, 'RoomsDao.update_category')

            return False

    @staticmethod
    def create_room(kwargs):
        try:
            get_conn().db.chatrooms.insert(kwargs)

            return True

        except Exception as e:
            print(e, 'RoomsDao.create_room')

            return False
