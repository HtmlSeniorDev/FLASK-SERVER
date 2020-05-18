from flask_socketio import emit
from dateutil.parser import parse
from datetime import datetime
from bson.objectid import ObjectId
from api.Models.DbModel.Photo import Photo
from api.Models.DbModel.UserModel import User


class ServiceProfile:
    @staticmethod
    def add_photo(id_user, privated, description, photo):
        try:
            photo_profile = Photo(user=id_user, description=description, privated=privated, createdAt=datetime.now())
            photo_profile.photo.put(photo, content_type='image/jpeg', filename="user_" + str(id_user))
            photo_profile.save()
            return True
        except Exception as e:
            print('ServiceProfile.add_photo', e)
            return False

    @staticmethod
    def del_photo(id_photo):
        try:
            Photo.objects(id=ObjectId(id_photo)).delete()
            return True
        except Exception as e:
            print('ServiceProfile.del_photo', e)
            return False

    @staticmethod
    def set_avatar_photo(id_user, id_photo):
        try:
            User.objects(id=ObjectId(id_user)).update_one(
                set__photo=id_photo,
            )
            return True
        except Exception as e:
            print('ServiceProfile.set_avatar_photo', e)
            return False

    # todo upd profile
    @staticmethod
    def get_profile_information(user_id):
        information = User.objects.get(id=ObjectId(user_id))
        if information.zags is not None:
            zags = User.objects.get(id=ObjectId(information.zags)).serialize_user_in_room()
            information.zags = [zags]
        return information.serialize_profile_information()

    @staticmethod
    def update_profile_information(kwargs):
        try:
            User.objects(id=ObjectId(kwargs['user_id'])).update_one(
                set__bday=parse(str(kwargs['bday'])),
                set__firstName=kwargs['firstName'],
                set__lastName=kwargs['lastName'],
                set__city=kwargs['city'],
                set__email=kwargs['email'],
                set__sex=int(kwargs['sex']),
                set__color=kwargs['color'],
                set__about=kwargs['about']
            )
            """Ищем юзера в списке подключенных и посылаем изменения в сокет"""

            # todo меняет у всех цвет
            emit('update_nic', {'color': int(kwargs['color']), "user": kwargs['user_id']}, user=kwargs['user_id'],
                 broadcast=True,
                 namespace='/chat')
            return True
        except Exception as e:
            print('ServiceProfile.update_profile_information', e)
            return False

    @staticmethod
    def set_new_password(kwargs):
        try:
            user = User.objects.get(id=ObjectId(kwargs['user_id']))
            if kwargs['old_password'] == user.password:

                User.objects(id=ObjectId(kwargs['user_id'])).update_one(
                    set__password=kwargs['password'],
                )
                return True

            return False

        except Exception as e:
            print('ServiceProfile.set_new_password', e)
            return False

    @staticmethod
    def set_new_nickname(kwargs):
        try:
            User.objects(id=ObjectId(kwargs['user_id'])).update_one(
                set__nic=kwargs['nic'],
            )
            """Посылаем изменения в сокет"""
            # todo посылает всем
            emit('update_nickname', {'nic': kwargs['nic'], "user": kwargs['user_id']}, broadcast=True,
                 namespace='/chat')
            return True
        except Exception as e:
            print('ServiceProfile.set_new_nickname', e)
            return False
