from mongoengine import Document, ReferenceField, CASCADE
from mongoengine import StringField
from .UserModel import User


class PushNotification(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    token = StringField()
    meta = {'collection': 'PushNotification'}

    def __str__(self) -> str:
        return 'PushNotification: ' + self.user
