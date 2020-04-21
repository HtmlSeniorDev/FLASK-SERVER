from .base_repo import get_conn


class GridFsDao:
    @staticmethod
    def save_audio(kwargs, name):
        try:
            get_conn().save_file(name, kwargs, metadata={
                "_contentType": "audio/aac",
                "_class": "com.mongodb.BasicDBObject"
            }, content_type='')

        except Exception as e:
              print(e)

    @staticmethod
    def save_photo(kwargs, name):
        try:
            get_conn().save_file(name, kwargs, metadata={
                "_contentType": "image/png",
                "_class": "com.mongodb.BasicDBObject"
            }, content_type='')

        except Exception as e:
            print(e)