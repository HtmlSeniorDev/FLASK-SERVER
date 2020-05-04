from bson.objectid import ObjectId
from bson.json_util import dumps
import json
from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao
from .ServiceColor import ServiceColor
from .ServiceFindPersonalRoom import ServiceFindPersonalRooms
from .ServiceSendMsg import ServiceSendMsg
from api.Objects.Server_id import TYPE_INVISIBLE
from .ServiceValidation import ServiceValidation
from ..Models.DataModel.GetUserTypeModel import GetUserTypeModel
from ..Models.DbModel.UserModel import User


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

    # todo эта хуйня ломается из-за поля type,доделать отправку в лс сообщения о том,что он невидимка.
    def add_invisible(self, user_id, admin_id):
        try:
            """ Checked admin_id permission (must TYPE_ADMIN,TYPE_MODERATOR)"""
            validation_admin = self.Validator.checked_admin(admin_id)
            validation_moderator = self.Validator.checked_moderator(admin_id)
            if not validation_admin and not validation_moderator:
                return False
            """ Checked user_id permission (must TYPE_USER)"""
            validation_user_admin = self.Validator.checked_moderator(user_id)
            validation_user_moderator = self.Validator.checked_admin(user_id)
            if not validation_user_admin and not validation_user_moderator:
                User.objects(id=ObjectId(user_id)).update_one(
                    set__type=TYPE_INVISIBLE,
                )

                return True

            return False
        except Exception as e:
            print('add_invisible', e)
