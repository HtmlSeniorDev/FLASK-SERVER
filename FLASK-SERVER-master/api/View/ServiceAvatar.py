import json
from datetime import datetime, timedelta
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_socketio import emit
from api.Repository.AvatarDao import AvatarDao
from api.Repository.UsersDao import UsersDao
from api.Models.DataModel.ListAvatarsModel import ListAvatarsModel
from api.Models.DbModel.AvatarModel import Avatar
from api.Models.DbModel.UserModel import User
from api.utils.Server_id import SERVER_ADDRESS
from ..Models.DbModel.SendAvatar import SendAvatar
from ..View.ServiceValidation import ServiceValidation


class ServiceAvatar:
    Avatar = AvatarDao()
    User = UsersDao()
    Validator = ServiceValidation()
    avatar_url = SERVER_ADDRESS + "/attachments/avatar/"

    def combine_avatar_list(self):
        try:
            """Парсим список аватаров"""
            return list(map(lambda avatar: ListAvatarsModel(
                avatar['_id']['$oid'],
                self.avatar_url + avatar['_id']['$oid'],
                int(avatar['price']),
                avatar['name']),
                            json.loads(dumps(self.Avatar.get_avatar_list()))))
        except Exception as e:
            print('combine_avatar_list', e)
            pass

    def buy_avatars(self, avatar_price, user_id, avatar_id):
        try:
            """Проверка баланса """

            validation = self.Validator.checked_balance(user_id, avatar_price)
            if not validation:
                """Если у отправителя не хватает баланса """
                return False
            else:

                avatar_end_at = datetime.now() + timedelta(days=30),
                balance_user = validation - avatar_price
                User.objects(id=ObjectId(user_id)).update_one(
                    set__avatarLink=avatar_id,
                    set__avatarEndAt=avatar_end_at[0],
                    set__balace=balance_user,
                )
                emit('update_avatar',
                     {'avatarLink': SERVER_ADDRESS + "/attachments/avatar/" + str(avatar_id), "user": user_id},
                     broadcast=True,
                     namespace='/chat')
                return True

        except Exception as e:
            print('ServiceAvatar_buy_avatar', e)
            pass

    def add_avatar(self, avatar_price, creator, name, photo):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                time = datetime.now()
                avatar = Avatar(
                    creator=creator,
                    price=int(avatar_price),
                    createdAt=time,
                    name=name)
                avatar.photo.put(photo, content_type='image/png', filename="avatar_" + str(time))
                avatar.save()
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
                    set__creator=User(id=creator),
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

    @staticmethod
    def send_user_avatar(kwargs):
        try:
            avatar = Avatar.objects.get(id=ObjectId(kwargs['avatar']))
            user = User.objects.get(id=ObjectId(kwargs['sender']))
            if avatar.price < user.balace:
                user.balace = user.balace - avatar.price
                user.save()
                SendAvatar(sender=user, user=kwargs['user'], avatar=kwargs['avatar']).save()
                return True
            return False

        except Exception as e:
            print('send_user_avatar', e)
            pass

    @staticmethod
    def check_avatar_send(user_id):
        avatar_information = SendAvatar.objects(user=ObjectId(user_id)).first()
        return avatar_information.serialize_sendlist()

    @staticmethod
    def accept_user_avatar(kwargs):
        try:
            if kwargs['accept']:
                User.objects(id=ObjectId(kwargs['user'])).update_one(
                    set__avatarLink=(kwargs['avatar']),
                    set__avatarEndAt=datetime.now())
                return True
            return False

        except Exception as e:
            print('accept_user_avatar', e)
