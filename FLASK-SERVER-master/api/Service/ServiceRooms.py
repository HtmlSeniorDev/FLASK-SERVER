from bson.json_util import dumps
import json
from api.Repository.RoomsDao import RoomsDao
from api.Objects.Server_id import TYPE_ADMIN
from api.Repository.UsersDao import UsersDao


class ServiceRooms:
    Rooms = RoomsDao()
    User = UsersDao()

    def get_rooms(self, category, mask):

        try:

            array_rooms = self.get_category(category)

            rooms_list = dumps(self.Rooms.get_rooms({'category': category, 'deleted': False}))

            count = -1

            for _ in json.loads(rooms_list):

                count += 1
                room = json.loads(rooms_list)[count]
                users_in_room = dumps(self.Rooms.get_user_room({'room': str(room['_id']['$oid'])}))
                users = 0
                for _ in json.loads(users_in_room):
                    users += 1

                room['count'] = users

                array_rooms.insert(count, room)
            self.get_category(category)

            return json.dumps(array_rooms[::-1], separators=(',', ':'))

        except Exception as e:

            print(e, 'ServiceRooms.get_rooms')
            pass

    def get_category(self, parent):
        try:
            array_rooms = []

            rooms_list = dumps(self.Rooms.get_category({'parent': parent, 'deleted': False}))

            count = -1

            for _ in json.loads(rooms_list):
                count += 1

                room = json.loads(rooms_list)[count]

                array_rooms.insert(-55, room)

            return array_rooms

        except Exception as e:

            print(e, 'ServiceRooms.get_categories')
            pass

    def change_category(self, change_name, mask, admin_id, category_id):
        try:
            mask = sum(mask)
            admin_checked = dumps(self.User.get_information_user(admin_id))

            serialize_admin = json.loads(admin_checked)

            if serialize_admin['type'] == TYPE_ADMIN:
                self.Rooms.update_category({'name': change_name, 'mask': mask}, category_id)

                return True

            else:
                return False

        except Exception as e:

            print(e, 'ServiceRooms.change_category')
            pass

    def delete_category(self, category_id, admin_id):
        try:

            admin_checked = dumps(self.User.get_information_user(admin_id))

            serialize_admin = json.loads(admin_checked)

            if serialize_admin['type'] == TYPE_ADMIN:
                self.Rooms.update_category({'deleted': True}, category_id)

                return True

            else:
                return False

        except Exception as e:

            print(e, 'ServiceRooms.delete_category')
            pass

    def create_category(self, name, admin_id, mask, parent):
        try:
            mask = sum(mask)
            admin_checked = dumps(self.User.get_information_user(admin_id))

            serialize_admin = json.loads(admin_checked)

            if serialize_admin['type'] == TYPE_ADMIN:
                self.Rooms.create_category({'deleted': False, 'name': name, 'mask': mask, 'parent': parent,
                                            "_class": "ru.readme.server.object.db.DBCategory"})

                return True

            else:
                return False
        except Exception as e:

            print(e, 'ServiceRooms.create_category')
            pass

    def create_room(self, name, admin_id, mask, category):
        try:
            mask = sum(mask)
            admin_checked = dumps(self.User.get_information_user(admin_id))

            serialize_admin = json.loads(admin_checked)

            if serialize_admin['type'] == TYPE_ADMIN:
                self.Rooms.create_room({'deleted': False, 'name': name, 'mask': mask, 'category': category,
                                            "_class" : "ru.readme.server.object.db.DBRoom"})

                return True

            else:
                return False

        except Exception as e:

            print(e, 'ServiceRooms.create_room')
            pass
