import json
from db import mongo
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from flask import Blueprint, request, jsonify
from api.View.ServiceAdmin import ServiceAdmin
from api.View.ServiceUnban import ServiceUnban
from api.View.ServiceAvatar import ServiceAvatar
from api.View.ServiceGifts import ServiceGifts

AdminList_blueprint = Blueprint('AdminList_blueprint', __name__, )
moderator_list_blueprint = Blueprint('moderator_list_blueprint', __name__, )
invisible_list_blueprint = Blueprint('invisible_list_blueprint', __name__, )
Unban_Actions_blueprint = Blueprint('Unban_Actions_blueprint', __name__, )
add_avatar_admin_blueprint = Blueprint('add_avatar_admin_blueprint', __name__)
upload_avatar_admin_blueprint = Blueprint('upload_avatar_admin_blueprint', __name__)
update_avatar_admin_blueprint = Blueprint('update_avatar_admin_blueprint', __name__)
delete_avatar_admin_blueprint = Blueprint('delete_avatar_admin_blueprint', __name__)
add_gift_admin_blueprint = Blueprint('add_gift_admin_blueprint', __name__)
upload_gift_admin_blueprint = Blueprint('upload_gift_admin_blueprint', __name__)
update_gift_admin_blueprint = Blueprint('update_gift_admin_blueprint', __name__)
delete_gift_admin_blueprint = Blueprint('delete_gift_admin_blueprint', __name__)
found_user_banned_blueprint = Blueprint('found_user_banned_blueprint', __name__)

useri = []


@found_user_banned_blueprint.route("/banned/user", methods=['GET'])  # users in room
def found_user_banned():
    online_users = mongo.db.dBBannedUser
    user_room = dumps(online_users.find().limit(50).sort('_id', -1), sort_keys=False, indent=4,
                      ensure_ascii=False, separators=(',', ': '))
    count1 = 0
    global us
    for us in json.loads(user_room):
        count1 += 1
        us = us['userId']
        useri.append(us)
    global v
    global user
    arr = []
    user = {'data': []}
    count = 0
    for _ in range(count1):
        count += 1
        v = loads(user_room)
        b = v[count - 1]
        g = (b['userId'])
        admin = (b['bannerId'])
        id_document = (b['_id'])
        online_users = mongo.db.users
        nick = (online_users.find_one({'_id': ObjectId(str(g))}))
        online_users1 = mongo.db.users
        nick1 = (online_users1.find_one({'_id': ObjectId(str(admin))}))
        rus1 = (nick1['nic'])
        rus = (nick['nic'])
        color = int(nick['color'])

        if rus == None:
            pass
            print('users empty')
        else:
            lists_users = (
                {'user': rus + '', 'color': color, 'user_id': g + '', 'admin': rus1 + '',
                 "id_document": str(id_document), "id_banner": str(admin)})
            arr.append(lists_users)
    url_by_dict = {i['user']: i for i in arr}
    new_items = list(url_by_dict.values())
    counts = 0
    for i in new_items[::-1]:
        counts += 1
        user['data'].append(i)

    complete = dumps((user), sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

    return complete


@Unban_Actions_blueprint.route("/Unban/User", methods=['POST'], strict_slashes=False)  # user search objectid
def unban_user():
    api_unban = ServiceUnban()
    res = request.get_json()
    id_user = str(res['id_user'])
    id_banner = str(res['id_banner'])
    name_admin = str(res['name_admin'])
    id_document = str(res['id_document'])
    result = api_unban.unban_user(id_user, id_banner, id_document, name_admin)

    return jsonify({"Accept": result})


@AdminList_blueprint.route("/get/users/type/<types>", methods=['GET'])  # user nick search
def get_admin_list(types):
    try:
        api_admin_list = ServiceAdmin()
        return jsonify([e.serialize() for e in api_admin_list.get_user_type_list(types)])
    except Exception as e:
        return str(e)


@moderator_list_blueprint.route("/get/users/type/<types>", methods=['GET'])  # users in room
def found_list_moderators(types):
    try:
        api_admin_list = ServiceAdmin()

        return api_admin_list.get_user_type_list(types)

    except Exception as e:

        return str(e)


@invisible_list_blueprint.route("/get/users/type/<types>", methods=['GET'])  # users in room
def found_list_invisible(types):
    try:
        api_admin_list = ServiceAdmin()
        return api_admin_list.get_user_type_list(types)

    except Exception as e:

        return str(e)


@invisible_list_blueprint.route("/add/user/type", methods=['POST'], strict_slashes=False)  # users in room
def add_type():
    try:
        api_admin_list = ServiceAdmin()
        res = request.get_json()
        id_user = str(res['id_user'])
        id_admin = str(res['id_admin'])
        type_ = str(res["type_"])
        time = str(res["time"])
        return jsonify({'status': api_admin_list.add_type(id_user, id_admin, type_,time)})

    except Exception as e:

        return str(e)


@add_avatar_admin_blueprint.route("/add/avatar/admin", methods=['GET', 'POST'], strict_slashes=False)  # user nick search
def add_avatar_admin():
    try:
        Avatar = ServiceAvatar()
        creator = request.form.get('creator')
        name = request.form.get('name')
        price = request.form.get('price')
        photo = request.files['photo']
        return dumps({"status": Avatar.add_avatar(price, creator, name, photo)})

    except Exception as e:

        print('AdminMapping_add_avatar_admin', e)

        return {"status": False}


@update_avatar_admin_blueprint.route("/update/avatar/admin", methods=['POST'])  # user nick search
def update_avatar_admin():
    try:
        Avatar = ServiceAvatar()
        res = request.get_json()
        creator = res['creator']
        name = res['name']
        price = res['price']
        avatar_id = res['avatar_id']
        return {'status': Avatar.update_avatar(price, name, creator, avatar_id)}

    except Exception as e:

        print('AdminMapping_update_avatar_admin', e)

        return {"name_avatar": 'ok'}


@delete_avatar_admin_blueprint.route("/delete/avatar/admin", methods=['POST'])  # user nick search
def delete_avatar_admin():
    try:
        Avatar = ServiceAvatar()
        res = request.get_json()
        creator = res['creator']
        avatar_id = res['avatar_id']
        return {'status': Avatar.delete_avatar(creator, avatar_id)}
    except Exception as e:

        print('AdminMapping_delete_avatar_admin', e)

        return {"name_avatar": False}


@add_gift_admin_blueprint.route("/add/gift/admin", methods=['POST'], strict_slashes=False)  # user nick search
def add_gift_admin():
    try:
        Gift = ServiceGifts()
        creator = request.form.get('creator')
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        photo = request.files['photo']
        return dumps({"status": Gift.add_gift(price, creator, name, description, photo)})
    except Exception as e:

        print('AdminMapping_add_avatar_admin', e)

        return {"name_avatar": False}


@update_gift_admin_blueprint.route("/update/gift/admin", methods=['POST'])  # user nick search
def update_gift_admin():
    try:
        Gift = ServiceGifts()
        res = request.get_json()
        creator = res['creator']
        name = res['name']
        price = res['price']
        gift_id = res['gift_id']
        description = res['description']

        return {'status': Gift.update_gift(price, name, creator, gift_id, description)}

    except Exception as e:

        print('AdminMapping_update_gift_admin', e)

        return {"name_gift": 'ok'}


@delete_gift_admin_blueprint.route("/delete/gift/admin", methods=['POST'])  # user nick search
def delete_gift_admin():
    try:
        Gift = ServiceGifts()
        res = request.get_json()
        creator = res['creator']
        gift_id = res['gift_id']
        return {'status': Gift.delete_gift(creator, gift_id)}
    except Exception as e:

        print('AdminMapping_delete_gift_admin', e)

        return {"name_avatar": False}
