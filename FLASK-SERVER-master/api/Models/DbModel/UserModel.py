from mongoengine import Document, BooleanField
from mongoengine import IntField, StringField, DateTimeField, ListField

from api.utils.Server_id import SERVER_ADDRESS


class User(Document):
    GENDER_CHOICE = {0: 'не определен', 1: 'мужской', 2: 'женский'}
    login = StringField(max_length=16, unique=True)
    password = StringField(max_length=16)
    nic = StringField(max_length=16, unique=True)
    firstName = StringField(max_length=16)
    lastName = StringField(max_length=16)
    email = StringField(max_length=20)
    about = StringField(max_length=40)
    sex = IntField(max_length=1, default=0, max_value=2, choices=GENDER_CHOICE, required=True)
    color = IntField()
    photo = StringField(max_length=50)
    type = IntField()
    city = StringField(max_length=20)
    bday = DateTimeField()
    registrationDate = DateTimeField()
    balace = IntField(min_value=0)
    vic = IntField()
    regDeviceId = StringField(max_length=20)
    lastVisit = DateTimeField()
    avatarLink = StringField()
    avatarEndAt = DateTimeField()
    zags = StringField()
    zagsRequest = ListField()
    friends = ListField()
    online = BooleanField()
    friendsRequest = ListField()
    meta = {'collection': 'users'}

    def __str__(self) -> str:
        return 'New User: ' + str(self.nic)

    def serialize_user_in_room(self):
        return {
            'id': str(self.id),
            'color': self.color,
            "photo": self.photo,
            'nic': self.nic,
            "online": self.online
        }

    def serialize_profile_information(self):
        return [dict({
            'id': str(self.id),
            'color': self.color,
            'nic': self.nic,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "sex": self.GENDER_CHOICE[self.sex],
            # "type": self.type,
            # "registrationDate": self.sex,
            "balace": self.balace,
            # "vic": self.vic,
            # "regDeviceId": self.regDeviceId,
            "photo": self.photo,
            "zags": self.zags,
            "zagsRequest": self.zagsRequest,
            "bday": str(self.bday)[:10],
            "city": self.city,
            "about": self.about
        })]
