from .base_repo import get_conn


class GiftsDao:
    @staticmethod
    def get_gifts_list():
        try:
            response = get_conn().db.gifts.find({})

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def insert_gift(kwargs):
        try:
            response = get_conn().db.usergifts.insert(kwargs)

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def insert_gift_admin(kwargs):
        try:
            _id = get_conn().db.gifts.insert(kwargs)

            return _id

        except Exception as e:
            print('insert_gift', e)
            return False

    @staticmethod
    def update_gift_admin(search_kwargs, kwargs):
        try:
            get_conn().db.gifts.update_one(search_kwargs,
                                              {"$set": kwargs})

            return True

        except Exception as e:
            print('update_gift', e)
            return False

    @staticmethod
    def delete_gift_admin(search_kwargs):
        try:
            get_conn().db.gifts.delete_one(search_kwargs)
            print('delete_gift_admin succsess')
            return True

        except Exception as e:
            print('delete_avatar', e)
            return False

    @staticmethod
    def delete_users_gifts_permanent(search_kwargs):
        try:
            get_conn().db.usergifts.delete_many(search_kwargs)
            print('delete_users_gifts_permanent')
            return True

        except Exception as e:
            print('delete_users_gifts_permanent', e)
            return False





