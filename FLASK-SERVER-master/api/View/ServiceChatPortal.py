from bson import ObjectId
from bson.json_util import dumps
import json

from flask import jsonify

from api.Models.DbModel.UserModel import User
from api.Repository.UsersDao import UsersDao
from api.Repository.WeddingDao import WeddingDao
from api.utils.Server_id import SERVER_ADDRESS


class ServiceChatPortal:
    request_friends = []
    friends_list = []
    User = UsersDao()
    Wedding = WeddingDao()

    """Отправляем заявку в друзья"""

    def invite_friends(self, data):
        try:
            user = User.objects.get(id=ObjectId(data["user"]))  # user which accepted or no
            friend = User.objects.get(id=ObjectId(data["friend"]))  # self id(sender)
            self.request_friends = user.friendsRequest
            self.request_friends.append(friend.id)
            user.friendsRequest = self.request_friends
            list(set(user.friendsRequest))  # удаляем повторяющиеся элементы
            user.save()
            return True
        except Exception as e:
            print("invite_friends", e)
            return False

    @staticmethod
    def friend_request_list(user_id):
        request_list = []
        user = User.objects.get(id=ObjectId(user_id))  # self id
        for user in user.friendsRequest:
            request_list.append(User.objects.get(id=user).serialize_user_in_room())
        return request_list

    """Согласие/Отказ от дружбы"""

    def access_friends(self, data):
        user = User.objects.get(id=ObjectId(data["user"]))
        friend = User.objects.get(id=ObjectId(data["friend"]))# ищем список заявок
        """Если пользователь дал согласие на дружбу"""
        try:
            if data["consent"]:  # true/false
                user.friendsRequest.remove(
                    ObjectId(
                        data['friend']))  # если пользователь согласен дружить удаляем его из списка запросов на дружбу
                self.friends_list = user.friends
                self.friends_list.append(ObjectId(data['friend']))  # добавляем его в список друзей
                user.friends = self.friends_list
                friend.friends.append(ObjectId(data["user"]))
                user.save()
                friend.save()
                return True
            else:
                user.friendsRequest.remove(
                    ObjectId(data['friend']))
                user.save()
                return True
        except Exception as e:
            print(e, "access friend")
            return False

    @staticmethod
    def get_friends_list(user_id):
        friends_list = []
        user = User.objects.get(id=ObjectId(user_id))  # self id
        for user in user.friends:
            friends_list.append(User.objects.get(id=user).serialize_user_in_room())
        return friends_list

    @staticmethod
    def delete_friend(data):
        user = User.objects.get(id=ObjectId(data["user"]))
        friend = User.objects.get(id=ObjectId(data["friend"]))# ищем список заявок
        """delete_friend"""
        try:
            user.friends.remove(ObjectId(data['friend']))
            friend.friends.remove(ObjectId(data['user']))
            user.save()
            friend.save()

            # если пользователь согласен дружить удаляем его из списка запросов на дружбу
            return True

        except Exception as e:
            print(e, "delete_friend")
            return False

    def get_weddings_list(self):
        try:
            weddings_data = dumps(self.Wedding.get_information_weddings())
            return self.make_view_weddings_list(weddings_data)
        except Exception as e:
            print(e)
            pass

    def make_view_weddings_list(self, data):
        try:

            count = 0
            array_weddings = []
            for _ in json.loads(data):
                one_wedding = json.loads(data)[count]
                count += 1

                user0 = dumps(self.User.get_information_user(one_wedding['users'][0]))
                user1 = dumps(self.User.get_information_user(one_wedding['users'][1]))

                username0_data = json.loads(user0)
                username1_data = json.loads(user1)

                nickname0 = username0_data['nic']
                nickname1 = username1_data['nic']
                try:

                    photo0 = username0_data['photo']
                    one_wedding['photo0'] = SERVER_ADDRESS + '/photos/' + str(photo0)
                except Exception as e:
                    one_wedding['photo0'] = 'image_exist'
                    print(e)

                try:
                    photo1 = username1_data['photo']
                    one_wedding['photo1'] = SERVER_ADDRESS + '/photos/' + str(photo1)
                except Exception as e:
                    one_wedding['photo1'] = 'image_exist'
                    print(e)

                one_wedding['username0'] = str(nickname0)
                one_wedding['username1'] = str(nickname1)

                array_weddings.insert(count, one_wedding)
            return jsonify(array_weddings[::-1])
        except Exception as e:

            print('make_view_weddings_list', e)
            pass
