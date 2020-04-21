from bson.json_util import dumps
import json
from api.Service.ServiceMessages import ServiceMessages
from api.Repository.BannedUserDao import BannedUser
from api.Repository.UsersDao import UsersDao
from api.Objects.Server_id import TYPE_BANNED, TYPE_ADMIN, TYPE_MODERATOR


class ServiceCheckBanned:
    User = UsersDao()
    Unban = BannedUser()
    Log_Message = ServiceMessages()

    def check_banned(self, id_user, imei):  # доделать список кто снимает
        try:
            self.User.change_information_user(id_user, {'regDeviceId': str(imei)})
            data = self.User.get_information_user(id_user)
            type_user = int(data['type'])
            print('type', type_user)
            if type_user == TYPE_ADMIN or type_user == TYPE_MODERATOR:
                return False
            else:
                response_imei_banned = dumps(self.User.find_user({'regDeviceId': str(imei)}))
                count = 0
                for user in json.loads(response_imei_banned):
                    count += 1
                    user_type = user['type']
                    if user_type == TYPE_BANNED:
                        self.User.change_information_user(id_user, {'type': TYPE_BANNED})

                        return False

                return True

        except Exception as e:
            print('ServiceCheckBanned', e)
