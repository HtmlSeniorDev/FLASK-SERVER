from .base_repo import get_conn


class PushDao:
    Information_user = None

    def get_token(self, kwargs):

        try:
            print(kwargs)
            response = get_conn().db.pushNotifications.find_one(kwargs)
            self.Information_user = response
            print(kwargs)
            print(response)
            return response

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def write_token(kwargs):

        user = kwargs['user']
        set_token = kwargs['token']
        print(user, set_token)

        update_token = get_conn().db.pushNotifications.find_one_and_update({'user': user},

                                                                           {"$set": {"token": set_token}},

                                                                           )

        if not update_token:
            get_conn().db.pushNotifications.insert(kwargs)
