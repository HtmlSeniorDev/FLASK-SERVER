from mongoengine import IntField, StringField, DateTimeField,Document, ReferenceField, CASCADE, FileField
from api.Models.DbModel.UserModel import User


class Gift(Document):
    creator = ReferenceField(User, reverse_delete_rule=CASCADE)
    price = IntField()
    createdAt = DateTimeField()
    photo = FileField()
    name = StringField(max_length=16)
    description = StringField(max_length=30)
    meta = {'collection': 'gifts'}

    def __str__(self) -> str:
        return 'New Gifts: ' + str(self.name)
