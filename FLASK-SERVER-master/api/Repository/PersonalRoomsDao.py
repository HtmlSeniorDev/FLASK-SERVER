from .base_repo import get_conn


class PersonalRoomsDao:

    @staticmethod
    def get_user_array(kwargs):  # поиск по id комнаты

        try:

            response = get_conn().db.personalrooms.find_one(kwargs)

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def create_pm_rooms(kwargs):  # создание комнаты с кем-то(сервером обычно)

        try:

            response = get_conn().db.personalrooms.insert(kwargs)

            return response

        except Exception as e:
            print(e)

    @staticmethod
    def find_array_user_to_id_room(kwargs):  # создание комнаты с кем-то(сервером обычно)

        try:

            response = get_conn().db.personalrooms.find_one(kwargs)

            return response

        except Exception as e:

           print(e)

    @staticmethod
    def find_personalrooms_user_id(kwargs):  # создание комнаты с кем-то(сервером обычно)

        try:

            response = get_conn().db.personalrooms.find(kwargs)

            return response

        except Exception as e:
            print(e)