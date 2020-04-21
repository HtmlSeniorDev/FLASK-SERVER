from bson.objectid import ObjectId
from .base_repo import get_conn


class UsersDao:
    Information_user = None

    def get_information_user(self, user_id):

        try:

            response = get_conn().db.users.find_one({'_id': ObjectId(user_id)})
            self.Information_user = response
            print('response')

            return response

        except Exception as e:
            print('UsersDao.get_information_user', e)

    @staticmethod
    def change_information_user(user_id, kwargs):

        try:

            get_conn().db.users.find_one_and_update({'_id': ObjectId(user_id)},
                                                    {"$set": kwargs})

            return True

        except Exception as e:
            print('UsersDao.change_information_user', e)

            return False

    @staticmethod
    def change_information_user_search(search_kwargs, kwargs):

        try:
            print(kwargs)

            get_conn().db.users.update_many(search_kwargs,
                                            {"$set": kwargs})

            return True

        except Exception as e:
            print('UsersDao.change_information_user_search', e)

            return False

    @staticmethod
    def change_unset_field_many(search_kwargs):

        try:

            get_conn().db.users.update_many(search_kwargs,
                                            {"$unset": {"avatarLink": 1}})

            return True

        except Exception as e:
            print('UsersDao.change_unset_field_one', e)

            return False

    def get_random_params(self, kwargs):

        try:
            response = get_conn().db.users.find_one(kwargs)
            self.Information_user = response
            print('response')

            return response
        except Exception as e:
            print('UsersDao.get_random_params', e)

    @staticmethod
    def change_unset_field_one(user_id, kwargs):

        try:

            get_conn().db.users.update({'_id': ObjectId(user_id)},
                                       {"$unset": kwargs})

            return True

        except Exception as e:
            print('UsersDao.change_unset_field_one', e)

            return False

    @staticmethod
    def find_user(search_kwargs):

        try:

            return get_conn().db.users.find(search_kwargs)

        except Exception as e:
            print('UsersDao.find_user', e)

            return False
