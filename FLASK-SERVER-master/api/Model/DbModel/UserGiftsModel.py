from mongoengine import Document, ReferenceField, CASCADE
from mongoengine import StringField, DateTimeField
from .UserModel import User


class UserGiftsModel(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    gift = StringField()
    date = DateTimeField()
    user_from = StringField()
    meta = {'collection': 'usergifts'}

    def __str__(self) -> str:
        return 'New user_gifts: ' + self.user
