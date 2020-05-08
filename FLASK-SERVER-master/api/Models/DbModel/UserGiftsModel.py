from mongoengine import Document, ReferenceField, CASCADE
from mongoengine import DateTimeField

from .GiftModel import Gift
from .UserModel import User


class UserGiftsModel(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    gift = ReferenceField(Gift, reverse_delete_rule=CASCADE)
    date = DateTimeField()
    from_ = ReferenceField(User, default=None)
    meta = {'collection': 'usergifts'}

    def __str__(self) -> str:
        return 'New user_gifts: ' + self.user
