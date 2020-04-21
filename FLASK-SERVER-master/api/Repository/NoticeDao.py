from .base_repo import get_conn


class NoticeDao:

    @staticmethod
    def update_notice(search_kwargs, kwargs):

        try:

            return get_conn().db.notices.find_one_and_update(search_kwargs,
                                                             {"$set": kwargs})

        except Exception as e:
            print('NoticeDao.update_notice', e)

    @staticmethod
    def get_notice(search_kwargs):

        try:

            return get_conn().db.notices.find_one(search_kwargs)

        except Exception as e:
            print('NoticeDao.get_notice', e)
