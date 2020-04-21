from init import app
from db import mongo


def get_conn():
    with app.app_context():
        return mongo
