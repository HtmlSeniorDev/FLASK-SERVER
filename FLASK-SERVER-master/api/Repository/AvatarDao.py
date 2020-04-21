from bson.objectid import ObjectId
from .base_repo import get_conn


class AvatarDao:
    @staticmethod
    def get_avatar_list():
        try:
            response = get_conn().db.dBAvatar.find({})

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def find_avatar(avatar_id):
        try:
            response = get_conn().db.dBAvatar.find({'_id': ObjectId(avatar_id)})

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def delete_avatars_many(kwargs):
        try:

            get_conn().db.dBAvatar.delete_many(kwargs)

            return True

        except Exception as e:
            print(e)

    @staticmethod
    def change_avatars_many(search_kwargs, kwargs):

        try:
            print(kwargs)

            get_conn().db.dBAvatar.update_many(search_kwargs,
                                               {"$set": kwargs})

            return True
        except Exception as e:
            print(e)

    @staticmethod
    def insert_avatar(kwargs):
        try:
            _id = get_conn().db.dBAvatar.insert(kwargs)

            return _id

        except Exception as e:
            print('insert_avatar', e)
            return False

    @staticmethod
    def update_avatar(search_kwargs, kwargs):
        try:
            get_conn().db.dBAvatar.update_one(search_kwargs,
                                              {"$set": kwargs})

            return True

        except Exception as e:
            print('update_avatar', e)
            return False

    @staticmethod
    def delete_avatar(search_kwargs):
        try:
            get_conn().db.dBAvatar.delete_one(search_kwargs)
            print('delete_avatar_admin succsess')
            return True

        except Exception as e:
            print('delete_avatar', e)
            return False
