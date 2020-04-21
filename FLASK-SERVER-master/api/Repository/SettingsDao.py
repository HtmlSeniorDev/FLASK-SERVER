from .base_repo import get_conn


class SettingsDao:

    @staticmethod
    def get_zags_price():

        try:

            response = get_conn().db.dBSettings.find_one({'name': 'ZAGS_PRICE'})
            price = int(response['ivalue'])

            return price

        except Exception as e:
            print('SettingsDao.get_zags_price', e)

    @staticmethod
    def set_zags_price(kwargs):

        try:

            get_conn().db.dBSettings.find_one_and_update({'name': 'ZAGS_PRICE'},   {"$set": kwargs})


            return True

        except Exception as e:
            print('SettingsDao.get_zags_price', e)
