from .base_repo import get_conn


class AttachmentsDao:
    @staticmethod
    def find_name(kwargs):
        try:
            data = get_conn().db.attachments.find_one(kwargs)
            print(data)
            return data

        except Exception as e:
            print(e)
