from mongoengine import Document, ReferenceField, CASCADE

from .RoomModel import Room
from .UserModel import User


class UserInRoom(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    room = ReferenceField(Room, reverse_delete_rule=CASCADE)
    meta = {'collection': 'userInRoom'}

    def __str__(self) -> str:
        return 'New user_connected_to_room:'
