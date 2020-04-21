from mongoengine import Document
from mongoengine import StringField


class PushNotification(Document):
    user = StringField()
    token = StringField()
    meta = {'collection': 'PushNotification'}

    def __str__(self) -> str:
        return 'PushNotification: ' + self.user
