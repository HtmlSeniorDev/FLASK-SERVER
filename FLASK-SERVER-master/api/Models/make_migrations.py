from db import mongo


def down():
    mongo.db.users.update_many({}, {'$unset': {'some_field': ''}})


def up():
    mongo.db.users.update_many({}, {'$set': {'friends': []}})

if __name__ == '__main__':
    up()