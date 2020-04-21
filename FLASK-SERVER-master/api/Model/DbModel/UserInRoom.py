from mongoengine import Document
from mongoengine import StringField


class UserInRoom(Document):
    user = StringField()
    room = StringField()
    meta = {'collection': 'UserInRoom'}

    def __str__(self) -> str:
        return 'New user_connected_to_room: ' + self.user
