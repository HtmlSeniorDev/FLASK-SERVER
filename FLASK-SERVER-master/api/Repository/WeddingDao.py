from .base_repo import get_conn


class WeddingDao:

    @staticmethod
    def get_information_weddings():

        try:

            response = get_conn().db.wedding.find({'deleted': False})

            return response

        except Exception as e:
            print('WeddingDao.get_information_weddings', e)

    @staticmethod
    def send_information_weddings(kwargs):

        try:

            response = get_conn().db.wedding.insert(kwargs)

            return response

        except Exception as e:
            print('WeddingDao.get_information_weddings', e)


