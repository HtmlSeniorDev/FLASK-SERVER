from mongoengine import Document
from mongoengine import IntField, StringField, DateTimeField


class Gift(Document):
    creator = StringField("Cоздатель подарка")
    price = IntField("Цена")
    createdAt = DateTimeField("Дата создания")
    name = StringField("Название подарка", max_length=16)
    description = StringField("Описание подарка", max_length=30)
    meta = {'collection': 'gifts'}

    def __str__(self) -> str:
        return 'New Gifts: ' + str(self.name)
