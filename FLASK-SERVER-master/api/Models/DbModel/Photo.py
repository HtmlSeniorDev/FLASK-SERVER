from mongoengine import Document, CASCADE, ReferenceField
from mongoengine import StringField, DateTimeField, BooleanField, FileField


# todo при установки аватарки пользователя,она не работает связать поле photo в модели User
from api.Models.DbModel.UserModel import User


class Photo(Document):
    privated = BooleanField()
    createdAt = DateTimeField()
    description = StringField(max_length=20)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    photo = FileField()
    meta = {'collection': 'photos'}

