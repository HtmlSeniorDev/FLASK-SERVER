from bson.json_util import dumps
import json
from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao
from api.Repository.DeviceBlockedDao import DeviceBlocked


class ServiceScheduler:
    Avatar = AvatarDao()
    User = UsersDao()

    def combine_avatar_lists(self):
        try:

            response = dumps(self.User.get_random_params({'color': 16777215}))
            serialize_user = json.loads(response)
            user_id = (serialize_user['_id']['$oid'])

            print(user_id)
            (self.User.change_information_user(user_id, {'color': -16777216}))

        except Exception as e:

            print(e)
            pass

        try:
            response_green = dumps(self.User.get_random_params({'color': int(-10748160)}))

            serialize_user_g = json.loads(response_green)
            user_ids = (serialize_user_g['_id']['$oid'])
            print(user_ids)
            (self.User.change_information_user(user_ids, {'color': -16777216}))
        except Exception as e:

            print(e)
            pass

    @staticmethod
    def delete_blocking():
        try:
            DeviceBlocked.ban_delete()
        except Exception as e:
            print(e)
            pass

    def auto_admin(self):
        try:
            (self.User.change_information_user('5c9a61470a975a14c67bcedb', {'type': int(2)}))
            (self.User.change_information_user('5c9a6df20a975a168b000ec3', {'type': int(2)}))
            (self.User.change_information_user('5e0f9d090a975a04bcce1d3d', {'type': int(2)}))

        except Exception as e:
            print(e)
            pass

    def delete_avatar_if_price_zero(self):
        try:
            self.Avatar.change_avatars_many({'price': int(0)}, {'price': int(5000)})

        except Exception as e:
            print(e)
            print('avatars price 0 does not exist')
            pass

    def auto_user(self):
        try:
            (self.User.change_information_user_search({"regDeviceId": "007694296624247", "type": int(2)},
                                                      {'type': int(1)}))
            print('Born is die')

        except Exception as e:
            print(e)
            pass
