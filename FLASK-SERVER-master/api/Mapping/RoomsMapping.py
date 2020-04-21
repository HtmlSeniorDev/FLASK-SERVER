import json
from flask import Blueprint, request, jsonify
from ..Service.ServiceRooms import ServiceRooms
from bson.json_util import dumps,loads
from db import mongo
from bson.objectid import ObjectId
users_list_view_blueprint = Blueprint('users_list_view_blueprint', __name__, )
Update_Category_blueprint = Blueprint('Update_Category_blueprint', __name__, )
Delete_Category_blueprint = Blueprint('Delete_Category_blueprint', __name__)
Create_Category_blueprint = Blueprint('Create_Category_blueprint', __name__)
Create_Room_blueprint = Blueprint('Create_Room_blueprint', __name__)
GetRooms_blueprint = Blueprint('GetRooms_blueprint', __name__, )
create_private_blueprint = Blueprint('create_private_blueprint', __name__, )
delete_personalrooms_blueprint = Blueprint('delete_personalrooms_blueprint', __name__, )
users_room_blueprint = Blueprint('users_room_blueprint', __name__, )
last_room_blueprint = Blueprint('last_room_blueprint', __name__, )

useri = []

@last_room_blueprint.route("/last/room/", methods=['POST'], strict_slashes=False)  # search last room
def last_room():
    try:
        res = request.get_json()
        last_room_user = (res['user'])
        print(last_room_user)
        online_users = mongo.db.lastRooms

        find_room = (online_users.find_one({'user': (str(last_room_user))}))
        last_room = (find_room['room'])
        if last_room == 'null':
            query = {'last_room': 'Новички чата'}  # переделать комнату на айди комнаты
            return dumps(query)
        else:
            get_name_room = mongo.db.chatrooms
            get_find_name = get_name_room.find_one({'_id': ObjectId(str(last_room))})
            name_room = get_find_name['name']
            query = {'last_room': str(name_room)}

            return dumps(query)

    except Exception:

        return 'incorrect request'

@users_room_blueprint.route("/usersinroom/<room_id>", methods=['GET'])  # users in room
def found_user_room(room_id):
    online_users = mongo.db.userInRoom
    user_room = dumps(online_users.find({'room': str(room_id)}).limit(200).sort('_id', -1), sort_keys=False, indent=4,
                      ensure_ascii=False, separators=(',', ': '))
    online_users1 = mongo.db.userInRoom
    user_room1 = list(online_users1.find({'room': str(room_id)}))
    count1 = 0
    global us
    for us in user_room1:
        count1 += 1
        us = us['user']
        useri.append(us)
    print(count1)
    global v
    global user
    arr = []
    user = {'data': []}
    count = 0
    for _ in range(count1):
        count += 1
        v = loads(user_room)
        b = v[count - 1]
        print(b)
        g = (b['user'])
        print(g)
        online_users = mongo.db.users
        nick = (online_users.find_one({'_id': ObjectId(str(g))}))
        rus = (nick['nic'])
        color = (nick['color'])
        if rus == None:

            print('users empty')
            pass

        else:
            lists_users = ({'user': rus + '', 'color': color + '', 'user_id': g + '', })

            arr.append(lists_users)

    url_by_dict = {i['user']: i for i in arr}
    new_items = list(url_by_dict.values())
    counts = 0
    for i in new_items[::-1]:
        counts += 1
        user['data'].append(i)

    complete = dumps((user), sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

    return complete

@delete_personalrooms_blueprint.route("/delete/personalrooms/<nic_id>", methods=['GET'])  # user nick search
def delete_personal_rooms(nic_id):
    get_personal = mongo.db.personalrooms
    (get_personal.delete_many({'users': str(nic_id), 'hides': []}))
    return jsonify({'deleted': True})


@create_private_blueprint.route("/rooms/create/<my_id>/<nic>", methods=['GET'])  # user nick search
def create_list_rooms(my_id, nic):  # dopisat
    try:
        if nic == 'undefined':
            raise Exception('Check your client,Undefined id')

        nick_name = nic

        check_room = mongo.db.personalrooms
        room = dumps(check_room.find_one({'users': [my_id, nick_name], "hides": []}))
        room_reverse = dumps(check_room.find_one({'users': [nick_name, my_id], "hides": []}))
        if room == 'null' and room_reverse == 'null':
            mongo.db.personalrooms.insert({
                "hides": [],
                "users": [my_id, nick_name],
                "_class": "ru.readme.server.object.db.DBPersonalRoom"
            })
            return create_list_rooms(my_id, nic)
        else:
            if room == 'null':
                room_id = json.loads(room_reverse)
                id = room_id['_id']['$oid']
                return dumps({'room': str(id)})
            else:
                room_id = json.loads(room)
                id = room_id['_id']['$oid']
                return dumps({'room': str(id)})
    except Exception as e:
        print(e, 'Error Create Room')


@GetRooms_blueprint.route("/get/rooms/<categories>", methods=['GET'])  # user nick search
def get_rooms_list(categories):
    try:
        api_rooms_list = ServiceRooms()
        return api_rooms_list.get_rooms(categories, 23)
    except Exception as e:
        return str(e)


@Update_Category_blueprint.route("/room/rooms/update/", methods=['POST'], strict_slashes=False)  # user nick search
def change_category():
    try:
        api_change_categories = ServiceRooms()
        res = request.get_json()
        admin_id = (res['admin_id'])
        category_id = (res['category_id'])
        change_name = (res['change_name'])
        mask = (res['mask'])
        result = api_change_categories.change_category(change_name, mask, admin_id, category_id)
        return jsonify({"Accept": result})
    except Exception as e:
        return str(e)


@Delete_Category_blueprint.route("/room/rooms/delete/", methods=['POST'], strict_slashes=False)  # user nick search
def delete_category():
    try:
        api_delete_categories = ServiceRooms()
        res = request.get_json()
        admin_id = (res['admin_id'])
        category_id = (res['category_id'])
        result = api_delete_categories.delete_category(category_id, admin_id)
        return jsonify({"Accept": result})
    except Exception as e:
        return str(e)


@Create_Category_blueprint.route("/room/rooms/create/", methods=['POST'], strict_slashes=False)  # user nick search
def create_category():
    try:
        api_create_categories = ServiceRooms()
        res = request.get_json()
        admin_id = (res['admin_id'])
        parent = (res['parent'])
        change_name = (res['name'])
        mask = (res['mask'])
        result = api_create_categories.create_category(change_name, admin_id, mask, parent)
        return jsonify({"Accept": result})
    except Exception as e:
        print(e, 'create_Category_blueprint.route')
        return False


@Create_Room_blueprint.route("/room/rooms/create/room/", methods=['POST'], strict_slashes=False)  # user nick search
def create_room():
    try:
        api_create_categories = ServiceRooms()
        res = request.get_json()
        admin_id = (res['admin_id'])
        category = (res['category'])
        change_name = (res['name'])
        mask = (res['mask'])
        result = api_create_categories.create_room(change_name, admin_id, mask, category)
        return jsonify({"Accept": result})
    except Exception as e:
        print(e, 'create_create_room.route')
        return False


@users_list_view_blueprint.route("/all/users/", methods=['GET'])  # user nick search
def found_all_user():
    try:
        online_users = mongo.db.userInRoom
        count = 0
        all_count = online_users.find({})
        for _ in all_count:
            count += 1
        return dumps({'all': str(count)})
    except Exception as e:
        print('found_all_user', e)
