from mongoengine import Document, FileField, ReferenceField, CASCADE
from mongoengine import IntField, StringField, DateTimeField

from api.Models.DbModel.UserModel import User
from api.utils.Server_id import SERVER_ADDRESS


class Avatar(Document):
    creator = ReferenceField(User, reverse_delete_rule=CASCADE)
    price = IntField()
    createdAt = DateTimeField()
    name = StringField(max_length=16)
    photo = FileField()
    meta = {'collection': 'dBAvatar'}

    def __str__(self) -> str:
        return 'New dBAvatar: ' + self.name

    def serialize_avatar_information(self):
        data = dict({
            'image': SERVER_ADDRESS + "/attachments/avatar/" + str(self.id),
            'name': self.name,
            "id":str(self.id),

        })

        return data

