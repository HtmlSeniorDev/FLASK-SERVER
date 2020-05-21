from mongoengine import DateTimeField, Document, ReferenceField, CASCADE
from api.Models.DbModel.UserModel import User


class BannedUser(Document):
    userId = ReferenceField(User, reverse_delete_rule=CASCADE)
    bannerId = ReferenceField(User, reverse_delete_rule=CASCADE)
    createdAt = DateTimeField()
    endAt = DateTimeField()
    meta = {'collection': 'dBBannedUser'}

    def __str__(self) -> str:
        return 'New ban: ' + str(self.createdAt)

