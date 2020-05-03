from mongoengine import Document
from mongoengine import IntField, StringField, DateTimeField

GENDER_CHOICE = {0: 'не известно', 1: 'мужской', 2: 'женский'}


class User(Document):
    login = StringField(max_length=16, unique=True)
    password = StringField(max_length=16)
    nic = StringField(max_length=16, unique=True)
    firstName = StringField(max_length=16)
    lastName = StringField(max_length=16)
    email = StringField(max_length=20)
    sex = IntField(default=0, max_length=1, choices=GENDER_CHOICE.keys(),
                   required=True)
    color = IntField()
    type = IntField(
        default=1)  # Тип пользователя(1-пользователь,2-админ,4-модератор,8-забаненный,16-невидимка,32-супербан
    registrationDate = DateTimeField()
    balace = IntField(min_value=0)
    vic = IntField()
    regDeviceId = StringField(max_length=20)  # Имеи устройства
    lastVisit = DateTimeField()  # Последнее посещение
    avatarLink = StringField()
    avatarEndAt = DateTimeField()

    meta = {'collection': 'users'}

    def __str__(self) -> str:
        return 'New User: ' + str(self.nic)
