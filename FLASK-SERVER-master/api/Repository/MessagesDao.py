from .base_repo import get_conn
from bson.json_util import dumps


class MessagesDao:
    @staticmethod
    def send_message(kwargs):

        try:

            get_conn().db.messages.insert(kwargs)

            return True

        except Exception as e:
            print('MessagesDao_send_message', e)

            return False

    @staticmethod
    def read_message(kwargs):

        try:

            return get_conn().db.messages.find(kwargs)

        except Exception as e:
            print('MessagesDao_read_message', e)

            return False

    @staticmethod
    def read_message_pm_last(kwargs):

        try:
            return get_conn().db.messages.find(kwargs).limit(1).sort('_id', -1)

        except Exception as e:
            print('read_message_pm_last', e)

            return False
