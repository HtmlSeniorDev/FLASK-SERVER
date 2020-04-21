from bson.objectid import ObjectId
from .base_repo import get_conn


class BannedUser:

    @staticmethod
    def ban_delete(id_document):

        try:

            get_conn().db.dBBannedUser.delete_one({'_id': ObjectId(id_document)})

            return True

        except Exception as e:
            print('BannedUserDao', e)


