from bson.json_util import dumps
import json
from datetime import datetime
from datetime import timedelta
from api.Repository.GiftsDao import GiftsDao
from api.Repository.UsersDao import UsersDao
from .ServiceMessages import ServiceMessages
from ..Models.DbModel.GiftModel import Gift
from ..Objects.Server_id import SERVER_ID, SERVER_ADDRESS
from bson.objectid import ObjectId
from ..Models.DataModel.ListGiftsModel import ListGiftsModel
from .ServiceValidation import ServiceValidation


class ServiceGifts:
    Gifts = GiftsDao()
    User = UsersDao()
    Validator = ServiceValidation()
    Msg = ServiceMessages()
    Gift_url = SERVER_ADDRESS + '/attachments/gift/'
    Text_Sending = "Пользователь отправил вам подарок,он будет виден у вас в профиле!"

    def get_gifts_list_service(self):
        try:

            return list(map(lambda gift: ListGiftsModel(gift['_id']['$oid'],
                                                        self.Gift_url + gift['_id']['$oid']
                                                        , int(gift['price']), gift['name'],
                                                        gift['description']),
                            json.loads(dumps(self.Gifts.get_gifts_list()))))
        except Exception as e:
            print(e)
            pass

    # todo исправить
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

    def add_gift(self, gift_price, creator, name, description, photo):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                time = datetime.now()
                avatar = Gift(
                    creator=creator,
                    price=int(gift_price) * 100,
                    createdAt=time,
                    description=description,
                    name=name)
                avatar.photo.put(photo, content_type='image/png', filename="gift_" + str(time))
                avatar.save()
                return True
        except Exception as e:
            print('ServiceGift_add_gift', e)
            pass

    def update_gift(self, gift_price, name, creator, gift_id, description):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                Gift.objects(id=ObjectId(gift_id)).update_one(
                    set__creator=creator,
                    set__description=description,
                    set__price=int(gift_price) * 100,
                    set__createdAt=datetime.now(),
                    set__name=name
                )
        except Exception as e:
            print('ServiceGift_update_gift', e)
            pass

    def delete_gift(self, creator, gift_id):
        try:
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                return Gift.objects(id=ObjectId(gift_id)).delete()
        except Exception as e:
            print('ServiceGift_delete_gift', e)
            pass
