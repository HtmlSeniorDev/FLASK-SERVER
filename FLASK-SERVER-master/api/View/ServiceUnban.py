from bson.json_util import dumps
import json
from api.View.ServiceMessages import ServiceMessages
from api.Repository.BannedUserDao import BannedUser
from api.Repository.UsersDao import UsersDao


class ServiceUnban:
    User = UsersDao()
    Unban = BannedUser()
    Log_Message = ServiceMessages()

    def unban_user(self, id_user, id_banner, id_document, name_admin):  # доделать список кто снимает
        try:
            response_admin = dumps(self.User.get_information_user(id_banner))
            serialize_user = json.loads(response_admin)
            user_type = serialize_user['type']
            if user_type == 4 or user_type == 2:
                object_change = {
                    "type": int(1)
                }
                self.User.change_information_user(id_user, object_change)
                self.Unban.ban_delete(str(id_document))
                self.Log_Message.logging_sender(id_user, id_banner, name_admin)

                return True

            else:

                return False

        except Exception as e:
            print('ServiceUnban.unban_user', e)

            return False

   


