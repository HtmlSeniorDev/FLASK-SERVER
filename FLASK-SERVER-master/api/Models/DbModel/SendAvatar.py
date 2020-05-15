from mongoengine import Document, ReferenceField, CASCADE

from api.Models.DbModel.AvatarModel import Avatar
from api.Models.DbModel.UserModel import User


class SendAvatar(Document):
    sender = ReferenceField(User, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    avatar = ReferenceField(Avatar, reverse_delete_rule=CASCADE)
    meta = {'collection': 'UserAvatarRequest'}

    def __str__(self) -> str:
        return 'New send Avatar: '

    def serialize_sendlist(self):
        data = ([dict({
            'sender': self.sender.serialize_user_in_room(),
            'user':  self.user.serialize_user_in_room(),
            'avatar': self.avatar.serialize_avatar_information(),

        })])

        return data
