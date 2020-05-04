from mongoengine import Document, ReferenceField, CASCADE
from mongoengine import StringField
from .UserModel import User


class UserInRoom(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    room = StringField()
    meta = {'collection': 'UserInRoom'}

    def __str__(self) -> str:
        return 'New user_connected_to_room: ' + self.user
