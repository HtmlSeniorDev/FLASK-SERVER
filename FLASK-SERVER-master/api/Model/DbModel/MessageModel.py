from mongoengine import Document
from mongoengine import IntField, StringField, DateTimeField, BooleanField, ListField


class Message(Document):
    user = StringField(max_length=25)
    message = StringField(max_length=180)
    system = BooleanField()
    hideNic = BooleanField()
    readed = BooleanField()
    attachments = ListField(max_length=1)
    nic = StringField(max_length=16)
    color = IntField()
    avatar = StringField()
    createdAt = DateTimeField("Время сообщений")
    key = StringField(unique=True)
    place = StringField()

    meta = {'collection': 'messages'}

    def __str__(self) -> str:
        return 'New Message: ' + str(self.message)
