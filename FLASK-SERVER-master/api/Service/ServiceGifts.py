from bson.json_util import dumps
import json
from datetime import datetime
from datetime import timedelta
from api.Repository.GiftsDao import GiftsDao
from api.Repository.UsersDao import UsersDao
from .ServiceMessages import ServiceMessages
from ..Objects.Server_id import SERVER_ID, SERVER_ADDRESS, TYPE_ADMIN
from bson.objectid import ObjectId
from ..Model.DataModel.ListGiftsModel import ListGiftsModel

class ServiceGifts:
    Gifts = GiftsDao()
    User = UsersDao()
    Msg = ServiceMessages()
    Gift_url = SERVER_ADDRESS + '/attachments/gifts-'
    Text_Sending = "Пользователь отправил вам подарок,он будет виден у вас в профиле!"

    def get_gifts_list_service(self):
        try:

            return list(map(lambda gift: ListGiftsModel(gift['_id']['$oid'],
                                                            self.Gift_url + gift['_id'][
                                                                '$oid'], int(gift['price']), gift['name'],gift['description']),
                            json.loads(dumps(self.Gifts.get_gifts_list()))))
        except Exception as e:
            print(e)
            pass

    def send_gifts(self, gift_price, user_id, gift_id, from_id):
        try:

            if user_id == from_id:
                raise Exception('Enough send self')

            response_user = dumps(self.User.get_information_user(from_id))
            serialize_user = json.loads(response_user)
            balance_user = int(serialize_user['balace'])
            print('this balance:', int(balance_user) / 100)
            if balance_user < gift_price:
                return False
            else:

                date_gift = datetime.now() + timedelta(hours=5),
                balance_user = balance_user - gift_price
                object_change = {
                    "balace": int(balance_user),

                }

                object_user_gifts = {

                    "user": str(user_id),
                    "gift": str(gift_id),
                    "date": date_gift[0],
                    "from": str(from_id),

                }

                dumps(self.Gifts.insert_gift(object_user_gifts))
                self.Msg.create_rooms(SERVER_ID, str(user_id),
                                      self.Text_Sending)
                dumps(self.User.change_information_user(from_id, object_change))

                return True

        except Exception as e:
            print(e)
            pass

    def add_gift(self, gift_price, creator, name, description):
        try:

            response_user = dumps(self.User.get_information_user(creator))
            serialize_user = json.loads(response_user)
            type_user = int(serialize_user['type'])
            if type_user != TYPE_ADMIN:
                return False
            else:

                createdAt = datetime.now(),

                object_change = {

                    "creator": str(creator),
                    "createdAt": createdAt[0],  # объект времени 0
                    "name": str(name),
                    "description": str(description),
                    "price": int(gift_price) * 100

                }

                return self.Gifts.insert_gift_admin(object_change)

        except Exception as e:
            print('ServiceGifts_add_gif', e)
            pass

    def update_gift(self, gift_price, name, creator, gift_id, description):
        try:

            response_user = dumps(self.User.get_information_user(creator))
            serialize_user = json.loads(response_user)
            type_user = int(serialize_user['type'])
            if type_user != TYPE_ADMIN:
                return False
            else:

                createdAt = datetime.now(),

                search_kwargs = {"_id": ObjectId(gift_id)}

                object_change = {

                    "creator": str(creator),
                    "createdAt": createdAt[0],  # объект времени 0
                    "name": str(name),
                    "price": int(gift_price) * 100,
                    "description":str(description)

                }

                return self.Gifts.update_gift_admin(search_kwargs, object_change)

        except Exception as e:
            print('ServiceAvatar_update_avatar', e)
            pass

    def delete_gift(self, creator, avatar_id):
        try:

            response_user = dumps(self.User.get_information_user(creator))
            serialize_user = json.loads(response_user)
            type_user = int(serialize_user['type'])
            if type_user != TYPE_ADMIN:
                return False
            else:

                search_kwargs = {"_id": ObjectId(str(avatar_id))}
                self.Gifts.delete_users_gifts_permanent({'gift': avatar_id})
                return self.Gifts.delete_gift_admin(search_kwargs)

        except Exception as e:
            print('ServiceAvatar_delete_avatar', e)
            pass
