from init import app
from init import mongo_connect


def get_conn():
    with app.app_context():
        return mongo_connect
