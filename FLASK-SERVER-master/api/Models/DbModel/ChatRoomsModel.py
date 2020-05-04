from mongoengine import Document
from mongoengine import IntField, StringField, BooleanField


class ChatRooms(Document):
    deleted = BooleanField()
    name = StringField()
    mask = IntField()
    category = IntField()  # не уточнено
    meta = {'collection': 'chatrooms'}

    def __str__(self) -> str:
        return 'Create_New_Room: ' + self.name
