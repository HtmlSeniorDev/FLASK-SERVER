from mongoengine import Document
from mongoengine import IntField, StringField, DateTimeField


class Avatar(Document):
    creator = StringField()
    price = IntField()
    createdAt = DateTimeField()
    name = StringField(max_length=16)
    meta = {'collection': 'dBAvatar'}

    def __str__(self) -> str:
        return 'New dBAvatar: ' + self.name
