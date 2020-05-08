from api.Repository.UsersDao import UsersDao
from api.Repository.PhotosDao import PhotosDao
from datetime import datetime
from bson.objectid import ObjectId
from ..Models.DbModel.Photo import Photo
from ..Models.DbModel.UserModel import User


class ServiceProfile:
    User = UsersDao()
    Photos = PhotosDao()

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
