from bson.json_util import dumps

from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao


class ServiceScheduler:
    Avatar = AvatarDao()
    User = UsersDao()

    def combine_avatar_lists(self):
        try:

            response = dumps(self.Avatar.get_avatar_list())
            print(response)

        except Exception as e:

            print('have some error', e)
            pass
