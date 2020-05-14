from bson.json_util import dumps
import json
from api.Repository.UsersDao import UsersDao
from api.Repository.SettingsDao import SettingsDao
from api.Repository.WeddingDao import WeddingDao
from datetime import datetime
from .ServiceMessages import ServiceMessages
from .ServicePushNotification import ServicePushNotification
from api.Objects.Server_id import SERVER_ID


class ServiceZags:
    User = UsersDao()
    Msg = ServiceMessages()
    Wedding = WeddingDao()
    Push = ServicePushNotification()

    Settings = SettingsDao()
    Text_Sending = '\tотправил вам заявку на вступление в брак.' \
                   'Посмотреть заявки можно в Чат портале, раздел "Виртуальный загс" '

    Text_Requester_User_Accepted = '\tсогласился на брак с вами.'
    Text_Decline_Request = '\t  отклонил вашу заявку на брак'
    Text_Delete_Request = '\t расторгнул брак с вами'

    def check_exist_zags(self, user_request):

        check_exist = dumps(self.User.get_information_user(user_request))
        serialize_exist_zags = json.loads(check_exist)
        try:
            zags_lenght = serialize_exist_zags['zags']

            return False



        except Exception as e:

            print('Check_zags_exist', e)

            return True

    def update_zags_request(self, user_request, user_from_request):
        try:

            if self.check_exist_zags(user_request):
                if user_request == user_from_request:
                    return False

                response_user = dumps(self.User.get_information_user(user_from_request))
                serialize_user = json.loads(response_user)
                balance_user = int(serialize_user['balace'])
                nick = 'Пользователь\t' + str(serialize_user['nic'])
                price_zags = self.Settings.get_zags_price()
                if balance_user < price_zags:
                    print('not enough money')
                    return False
                else:
                    balance_user = balance_user - price_zags
                    object_change = {
                        "balace": int(balance_user),
                    }

                    object_change_zags = {"zagsRequest": [str(user_from_request)]}
                    self.Msg.create_rooms(SERVER_ID, str(user_request), nick + self.Text_Sending)
                    dumps(
                        self.User.change_information_user(user_from_request, object_change))  # user_update_from_balance
                    dumps(
                        self.User.change_information_user(user_request, object_change_zags))  # user_update_zags_request
                    self.Push.send_wedding_push(str(user_request), nick + self.Text_Sending, nick)

                    return True

            return False

        except Exception as e:

            print(e, 'UPDATE_ZAGS_REQUEST________________METHOD')
            pass

    def accept_zags_request(self, user_id, from_accept_id):

        try:

            print(user_id)
            print(from_accept_id)
            object_change_accepter = {
                "zags": user_id,
                "zagsRequest": []
            }
            object_change_requester = {
                "zags": from_accept_id,

            }

            response_user = dumps(self.User.get_information_user(from_accept_id))
            serialize_user = json.loads(response_user)
            nick = 'Пользователь\t' + str(serialize_user['nic'])
            self.Msg.create_rooms(SERVER_ID, user_id, nick + self.Text_Requester_User_Accepted)
            dumps(self.User.change_information_user(from_accept_id, object_change_accepter))
            dumps(self.User.change_unset_field_one(from_accept_id, {"zagsRequest": 1}))
            dumps(self.User.change_information_user(user_id, object_change_requester))  # accept
            weddingstartAt = datetime.now()

            insert_wedding = {"users": [
                from_accept_id,
                user_id
            ],
                "date": weddingstartAt,
                "deleted": False}

            self.Wedding.send_information_weddings(insert_wedding)
            self.Push.send_wedding_push(user_id, nick + self.Text_Requester_User_Accepted, nick)




        except Exception as e:
            print('accept zags request _______________error')
            print(e)

    def delete_zags(self, user_id, from_accept_id):

        try:
            print(user_id)
            print(from_accept_id)

            response_user = dumps(self.User.get_information_user(from_accept_id))
            serialize_user = json.loads(response_user)
            nick = 'Пользователь\t' + str(serialize_user['nic'])
            self.Msg.create_rooms(SERVER_ID, user_id, nick + self.Text_Delete_Request)
            dumps(self.User.change_unset_field_one(user_id, {"zags": 1}))
            dumps(self.User.change_unset_field_one(from_accept_id, {"zags": 1}))
            self.Push.send_wedding_push(user_id, nick + self.Text_Delete_Request, nick)

        except Exception as e:

            print('delete_zags-------------', e)

    def decline_zags_request(self, user_id, from_request):

        response_user = dumps(self.User.get_information_user(user_id))
        serialize_user = json.loads(response_user)

        self.Msg.create_rooms(SERVER_ID, from_request,
                              serialize_user['nic'] + self.Text_Decline_Request)
        dumps(self.User.change_unset_field_one(user_id, {"zagsRequest": 1}))
        self.Push.send_wedding_push(from_request, serialize_user['nic'] + self.Text_Decline_Request,
                                    serialize_user['nic'])
        # accept
