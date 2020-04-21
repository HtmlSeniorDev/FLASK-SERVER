from flask import jsonify
from api.Repository.NoticeDao import NoticeDao
from api.Repository.UsersDao import UsersDao


class ServiceNotice:
    User = UsersDao()
    Notice = NoticeDao()

    def show_notice(self, id_user):  # доделать список кто снимает
        try:

            search_kwargs = {

                "userId": id_user,

            }
            response_notice_text = self.Notice.get_notice(search_kwargs)
            text = response_notice_text['message']

            if response_notice_text['readed']:

                return {'notice': text, 'readed': True}

            else:

                update_kwargs = {

                    "readed": True

                }

            response_notice_text = self.Notice.update_notice(search_kwargs, update_kwargs)
            text = response_notice_text['message']

            return {'notice': text, 'readed': False}

        except Exception as e:
            print('ServiceNotice.show_notice', e)

            return False
