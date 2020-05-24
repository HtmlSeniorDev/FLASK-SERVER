from datetime import datetime, timedelta

from bson.objectid import ObjectId
from bson.json_util import dumps
import json
from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao
from .ServiceColor import ServiceColor
from .ServiceFindPersonalRoom import ServiceFindPersonalRooms
from .ServiceSendMsg import ServiceSendMsg
from api.utils.Server_id import TYPE_INVISIBLE, TYPE_BANNED, TYPE_USER
from .ServiceValidation import ServiceValidation
from api.Models.DataModel.GetUserTypeModel import GetUserTypeModel
from api.Models.DbModel.UserModel import User
from ..Models.DbModel.BannedUser import BannedUser


class ServiceAdmin:
    Avatar = AvatarDao()
    User = UsersDao()
    Validator = ServiceValidation()
    Color = ServiceColor()
    Send = ServiceSendMsg()
    Text_Invisible = 'Теперь вы не можете писать в общий чат!'
    Private_room = ServiceFindPersonalRooms()

    def get_user_type_list(self, user_type):
        try:
            """Получает список пользователей по их типу прав"""
            return list(map(lambda x: GetUserTypeModel(x['_id']['$oid'], x['nic'], x['color']),
                            json.loads(dumps(self.User.find_user({'type': int(user_type)})))))
        except Exception as e:
            print(e, 'AdminService.get_user_type_list')
            pass

    """Снять бан/Добавить бан"""
    def add_type(self, user_id, admin_id, type_, time_ban):
        try:

            """ Checked admin_id permission (must TYPE_ADMIN,TYPE_MODERATOR)"""
            validation_admin = self.Validator.check_admin(admin_id)
            validation_moderator = self.Validator.check_moderator(admin_id)
            if not validation_admin and not validation_moderator:
                return False
            """ Checked user_id permission (must TYPE_USER)"""
            validation_user_admin = self.Validator.check_moderator(user_id)
            validation_user_moderator = self.Validator.check_admin(user_id)
            if not validation_user_admin and not validation_user_moderator:
                User.objects(id=ObjectId(user_id)).update_one(
                    set__type__=type_,
                )
                if type_ == TYPE_BANNED:
                    created = datetime.now()
                    end = created + timedelta(minutes=time_ban)
                    BannedUser(bannerId=admin_id, userId=user_id, createdAt=created, endAt=end).save()
                elif type_ == TYPE_USER:
                    try:
                        BannedUser.objects(userId=ObjectId(user_id)).delete()
                    except Exception as e:
                        print(e)
                        return True

                return True
            return False
        except Exception as e:
            print('add_invisible', e)
