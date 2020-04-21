from .base_repo import get_conn


class PhotosDao:

    @staticmethod
    def insert_photo(kwargs):
        try:

            _id = get_conn().db.photos.insert(kwargs)

            return _id

        except Exception as e:
            print('insert_photo', e)

            return False

    @staticmethod
    def delete_photo(kwargs):
        try:

            get_conn().db.photos.delete_one(kwargs)

            return True

        except Exception as e:
            print('delete', e)

            return False
