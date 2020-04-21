from .base_repo import get_conn


class DeviceBlocked:

    @staticmethod
    def ban_delete():

        try:

            get_conn().db.deviceBan.delete_many({})
            print('disban')
            return True

        except Exception as e:
            print('BannedUserDao', e)