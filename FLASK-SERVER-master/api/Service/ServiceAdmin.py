from bson.json_util import dumps
import json
from datetime import datetime
from datetime import timedelta
from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao
from .ServiceColor import ServiceColor
from .ServiceFindPersonalRoom import ServiceFindPersonalRooms
from .ServiceSendMsg import ServiceSendMsg
from api.Objects.Server_id import TYPE_INVISIBLE, TYPE_ADMIN, TYPE_MODERATOR
from ..Objects.Server_id import TYPE_PM, SERVER_ID
from ..Model.DataModel.GetUserTypeModel import GetUserTypeModel


class ServiceAdmin:
    Avatar = AvatarDao()
    User = UsersDao()

    Color = ServiceColor()
    Send = ServiceSendMsg()
    Text_Invisible = 'Теперь вы не можете писать в общий чат!'
    Private_room = ServiceFindPersonalRooms()

    def get_user_type_list(self, user_type):
        try:
            return list(map(lambda x: GetUserTypeModel(x['_id']['$oid'], x['nic'], x['color']),
                            json.loads(dumps(self.User.find_user({'type': int(user_type)})))))
        except Exception as e:
            print(e, 'AdminService.get_user_type_list')
            pass

    def get_block_list(self, avatar_price, user_id, avatar_id):
        try:
            response_user = dumps(self.User.get_information_user(user_id))
            serialize_user = json.loads(response_user)
            balance_user = int(serialize_user['balace'])
            if balance_user < avatar_price:
                return False
            else:
                avatarEndAt = datetime.now() + timedelta(days=30),
                balance_user = balance_user - avatar_price
                object_change = {
                    "avatarLink": str(avatar_id),
                    "avatarEndAt": avatarEndAt[0],  # объект времени 0
                    "balace": int(balance_user),
                }
                dumps(self.User.change_information_user(user_id, object_change))
                return True
        except Exception as e:
            print('get_block_list', e)
            pass

    def send_avatars(self, avatar_price, user_id_sender, avatar_id, user_id_accepter):
        try:
            response_user = dumps(self.User.get_information_user(user_id_sender))
            serialize_user = json.loads(response_user)
            balance_user = int(serialize_user['balace'])
            if balance_user < avatar_price:
                return False
            else:
                balance_user = balance_user - avatar_price
                object_change = {
                    "balace": int(balance_user),
                }
                object_accepter = {
                    "avatarRequest": avatar_id
                }
                dumps(self.User.change_information_user(user_id_accepter, object_accepter))
                dumps(self.User.change_information_user(user_id_sender, object_change))
                return True
        except Exception as e:
            print('send_avatars', e)
            pass

    def accept_avatar_send(self, user_id_accepter):
        try:
            response_user = dumps(self.User.get_information_user(user_id_accepter))
            serialize_user = json.loads(response_user)
            avatar_request = (serialize_user['avatarRequest'])
            avatarEndAt = datetime.now() + timedelta(days=30),
            object_change = {
                "avatarLink": str(avatar_request),
                "avatarEndAt": avatarEndAt[0],  # объект времени 0
            }
            dumps(self.User.change_information_user(user_id_accepter, object_change))
            return True
        except Exception as e:
            print('accept_avatar_send', e)
            pass

    def add_invisible(self, user_id, admin_id):
        try:
            response_user = dumps(self.User.get_information_user(admin_id))
            serialize_user = json.loads(response_user)
            type_user = int(serialize_user['type'])
            if type_user == TYPE_ADMIN or type_user == TYPE_MODERATOR:
                object_change = {
                    'type': TYPE_INVISIBLE
                }
                self.User.change_information_user(user_id, object_change)
                room = self.Private_room.find_personal_server(user_id)
                print('admin_room', room)
                self.Send.send_message(SERVER_ID, self.Text_Invisible, TYPE_PM, room, [])
                return True
            return False
        except Exception as e:
            print('add_invisible', e)
            pass
