from mongoengine import IntField, StringField, Document, BooleanField


class Room(Document):
    deleted = BooleanField()
    mask = IntField()
    name = StringField(max_length=16)
    category = StringField(max_length=30)
    meta = {'collection': 'chatrooms'}

    def __str__(self) -> str:
        return 'New Room: ' + str(self.name)
