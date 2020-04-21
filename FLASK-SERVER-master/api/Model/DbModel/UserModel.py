from mongoengine import Document
from mongoengine import IntField, StringField, DateTimeField


class User(Document):
    login = StringField(max_length=16, unique=True)
    password = StringField(max_length=16)
    nic = StringField(max_length=16, unique=True)
    firstName = StringField(max_length=16)
    lastName = StringField(max_length=16)
    email = StringField(max_length=20)
    sex = IntField("Пол(0-не определен,1-мужской,2-женский)", default=0)
    color = IntField()
    type = IntField("Тип пользователя(1-пользователь,2-админ,4-модератор,8-забаненный,16-невидимка,32-супербан",
                    default=1)
    registrationDate = DateTimeField()
    balace = IntField(min_value=0)
    vic = IntField("количетсво очков викторины")
    regDeviceId = StringField("Имеи устройства", max_length=20)
    lastVisit = DateTimeField("Последнее посещение")
    avatarLink = StringField()
    avatarEndAt = DateTimeField()

    meta = {'collection': 'users'}

    def __str__(self) -> str:
        return 'New User: ' + str(self.nic)
