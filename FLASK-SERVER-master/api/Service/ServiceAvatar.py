import json
from datetime import datetime
from datetime import timedelta

from bson.json_util import dumps
from bson.objectid import ObjectId

from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao
from ..Model.DataModel.ListAvatarsModel import ListAvatarsModel
from ..Model.DbModel.AvatarModel import Avatar
from ..Model.DbModel.UserModel import User
from ..Objects.Server_id import SERVER_ADDRESS
from ..Service.ServiceValidation import ServiceValidation


class ServiceAvatar:
    Avatar = AvatarDao()
    User = UsersDao()
    Validator = ServiceValidation()
    avatar_url = SERVER_ADDRESS + "/attachments/avatars-"

    def combine_avatar_list(self):
        try:
            return list(map(lambda avatar: ListAvatarsModel(avatar['_id']['$oid'],
                                                            self.avatar_url + avatar['_id'][
                                                                '$oid'], int(avatar['price']), avatar['name']),
                            json.loads(dumps(self.Avatar.get_avatar_list()))))
        except Exception as e:
            print(e)
            pass

    def buy_avatars(self, avatar_price, user_id, avatar_id):
        try:
            validation = self.Validator.checked_balance(user_id, avatar_price)
            if not validation:
                return False
            else:
                avatar_end_at = datetime.now() + timedelta(days=30),
                balance_user = validation - avatar_price
                User.objects(id=ObjectId(user_id)).update_one(
                    set__avatarLink=avatar_id,
                    set__avatarEndAt=avatar_end_at[0],
                    set__balace=balance_user,
                )

                return True

        except Exception as e:
            print('ServiceAvatar_buy_avatar', e)
            pass

    def add_avatar(self, avatar_price, creator, name):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                Avatar(
                    creator=creator,
                    price=int(avatar_price) * 100,
                    createdAt=datetime.now(),
                    name=name).save()
                return True
        except Exception as e:
            print('ServiceAvatar_add_avatar', e)
            pass

    def update_avatar(self, avatar_price, name, creator, avatar_id):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                Avatar.objects(id=ObjectId(avatar_id)).update_one(
                    set__creator=creator,
                    set__price=int(avatar_price) * 100,
                    set__createdAt=datetime.now(),
                    set__name=name
                )
        except Exception as e:
            print('ServiceAvatar_update_avatar', e)
            pass

    def delete_avatar(self, creator, avatar_id):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                return Avatar.objects(id=ObjectId(avatar_id)).delete()

        except Exception as e:
            print('ServiceAvatar_delete_avatar', e)
            pass
