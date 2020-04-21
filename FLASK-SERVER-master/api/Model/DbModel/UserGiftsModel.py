from mongoengine import Document
from mongoengine import StringField, DateTimeField


class UserGiftsModel(Document):
    user = StringField()
    gift = StringField()
    date = DateTimeField()
    user_from = StringField()
    meta = {'collection': 'usergifts'}

    def __str__(self) -> str:
        return 'New user_gifts: ' + self.user
