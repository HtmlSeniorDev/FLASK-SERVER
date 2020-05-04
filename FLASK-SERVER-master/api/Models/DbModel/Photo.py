from mongoengine import Document
from mongoengine import StringField, DateTimeField, BooleanField, ReferenceField, CASCADE, FileField
from .UserModel import User


class Photo(Document):
    privated = BooleanField()
    createdAt = DateTimeField()
    description = StringField()
    photo = FileField()
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    meta = {'collection': 'photos'}

    def __str__(self) -> str:
        return 'New_USER_PHOTO: ' + self.user
