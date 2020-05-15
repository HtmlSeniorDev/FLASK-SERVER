from pyfcm import FCMNotification
from .FirebaseConfig import firebase_api_key
from api.Repository.PushDao import PushDao
from api.Repository.PersonalRoomsDao import PersonalRoomsDao
from api.Repository.UsersDao import UsersDao
from bson.objectid import ObjectId


class ServicePushNotification:
    Push = PushDao()
    Pm = PersonalRoomsDao()
    User = UsersDao()

    def determinate_push_user(self, room_id, name_sender) -> str:

        object_query = {"_id": ObjectId(room_id)}

        users_array = (self.Pm.get_user_array(object_query))

        serialize_users = (users_array['users'])
        user1 = serialize_users[0]
        user2 = serialize_users[1]

        if user1 == name_sender:

            return user2
        else:

            return user1

    def send_client_push(self, name_sender, message, room_id) -> bool:  # отправка пуш уведомления клиенту
        try:

            name = self.determinate_push_user(room_id, name_sender)
            fcm_token1 = self.Push.get_token({'user': str(name),
                                              })

            nickname = self.User.get_information_user(name_sender)
            push_service = FCMNotification(
                api_key=firebase_api_key)

            registration_id = str(fcm_token1['token'])  # fcm token
            message_title = str(nickname['nic'])
            message_body = str(message)
            print('registration_id---------------------------------------------------------------------',
                  registration_id)
            push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                              message_body=message_body, sound='default',
                                              android_channel_id='fcm_default_channel')

            return True

        except Exception as e:
            print(e)

            return False

    def add_push_token(self, fcm_token, name_sender) -> bool:  # добавляем пуш в базу
        try:
            query = {
                'user': str(name_sender),
                'token': str(fcm_token)
            }

            self.Push.write_token(query)

            return True
        except Exception as e:
            print(e)

            return False

    def send_wedding_push(self, user_id, message, title):
        try:

            fcm_token1 = self.Push.get_token({'user': str(user_id),
                                              })

            push_service = FCMNotification(
                api_key=firebase_api_key)

            registration_id = str(fcm_token1['token'])  # fcm token
            message_title = str(title)
            message_body = str(message)
            print('registration_id---------------------------------------------------------------------',
                  registration_id)

            push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                              message_body=message_body, sound='default',
                                              android_channel_id='fcm_default_channel')
        except Exception as e:
            print(e, 'send_wedding_push error')