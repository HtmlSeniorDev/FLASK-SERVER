from bson.json_util import dumps
import json

from flask import jsonify

from api.Repository.UsersDao import UsersDao
from api.Repository.WeddingDao import WeddingDao
from api.Objects.Server_id import SERVER_ADDRESS


class ServiceWeddingView:
    User = UsersDao()
    Wedding = WeddingDao()

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
