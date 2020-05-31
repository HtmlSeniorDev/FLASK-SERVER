from api.Repository.base_repo import get_conn


def down():
    get_conn().db.users.update_many({}, {'$unset': {'some_field': ''}})


def up():
    get_conn().db.users.update_many({}, {'$set': {'friends': []}})

if __name__ == '__main__':
    up()