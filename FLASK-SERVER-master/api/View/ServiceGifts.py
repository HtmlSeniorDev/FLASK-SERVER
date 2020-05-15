from bson.json_util import dumps
import json
from datetime import datetime
from api.Repository.GiftsDao import GiftsDao
from api.Repository.UsersDao import UsersDao
from .ServiceMessages import ServiceMessages
from api.Models.DbModel.GiftModel import Gift
from api.Models.DbModel.UserGiftsModel import UserGiftsModel
from api.Models.DbModel.UserModel import User
from api.utils.Server_id import SERVER_ADDRESS
from bson.objectid import ObjectId
from api.Models.DataModel.ListGiftsModel import ListGiftsModel
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
            """Парсим список подарков"""
            return list(map(lambda gift: ListGiftsModel(gift['_id']['$oid'],
                                                        self.Gift_url + gift['_id']['$oid']
                                                        , int(gift['price']), gift['name'],
                                                        gift['description']),
                            json.loads(dumps(self.Gifts.get_gifts_list()))))
        except Exception as e:
            print("get_gifts_list_service", e)

    # todo исправить
    """Отправка подарка пользователю"""

    def send_gifts(self, gift_price, user_id, gift_id, from_id):
        try:
            if user_id == from_id:
                raise Exception('Enough send self')

            """Проверка баланса """
            validation = self.Validator.checked_balance(user_id, gift_price)
            if not validation:

                """Если у отправителя не хватает баланса """
                return False
            else:

                """Отнимаем стоимость подарка"""
                balance_user = validation - gift_price

                """Создаем объект подарок пользователя"""
                UserGiftsModel(user=User(id=user_id), gift=Gift(id=gift_id), date=datetime.now(),
                               from_=User(id=from_id)).save()

                """Снимаем баланс отправителя"""
                User.objects(id=ObjectId(from_id)).update_one(
                    set__balace=balance_user,
                )
                return True

        except Exception as e:
            print("send_gifts", e)

    """Добавление подарка админом"""

    def add_gift(self, gift_price, creator, name, description, photo):
        try:
            """Проверяем права доступа"""
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                time = datetime.now()
                """Создамем подарок """
                gift = Gift(
                    creator=creator,
                    price=int(gift_price),
                    createdAt=time,
                    description=description,
                    name=name
                )
                gift.photo.put(photo, content_type='image/png', filename="gift_" + str(time))
                gift.save()
                return True
        except Exception as e:
            print('ServiceGift_add_gift', e)

    """Обновление подарка админом"""

    def update_gift(self, gift_price, name, creator, gift_id, description):
        try:
            """Проверяем права доступа"""
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                """Обновляем подарок"""
                Gift.objects(id=ObjectId(gift_id)).update_one(
                    set__creator=User(id=creator),
                    set__description=description,
                    set__price=int(gift_price),
                    set__createdAt=datetime.now(),
                    set__name=name
                )
        except Exception as e:
            print('ServiceGift_update_gift', e)

    def delete_gift(self, creator, gift_id):
        try:
            """Проверяем права доступа"""
            validation = self.Validator.checked_admin(creator)
            if not validation:
                return False
            else:
                """Удаляем подарок"""
                return Gift.objects(id=ObjectId(gift_id)).delete()
        except Exception as e:
            print('ServiceGift_delete_gift', e)
