import json
from db import mongo
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from flask import Blueprint, request, jsonify
from ..Service.ServiceColor import ServiceColor
from ..Service.ServiceAdmin import ServiceAdmin
from ..Service.ServiceUnban import ServiceUnban
from ..Service.ServiceAvatar import ServiceAvatar
from ..Service.ServiceGifts import ServiceGifts

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


@AdminList_blueprint.route("/get/users/type/<types>", methods=['GET'])
def get_admin_list(types):
    try:
        api_admin_list = ServiceAdmin()
        return jsonify([e.serialize() for e in api_admin_list.get_user_type_list(types)])
    except Exception as e:
        return str(e)


@moderator_list_blueprint.route("/get/users/type/<types>", methods=['GET'])
def found_list_moderators(types):
    try:
        api_admin_list = ServiceAdmin()

        return api_admin_list.get_user_type_list(types)

    except Exception as e:

        return str(e)


@invisible_list_blueprint.route("/get/users/type/<types>", methods=['GET'])
def found_list_invisible(types):
    try:
        api_admin_list = ServiceAdmin()

        return api_admin_list.get_user_type_list(types)

    except Exception as e:

        return str(e)


@invisible_list_blueprint.route("/add/invisible", methods=['POST'], strict_slashes=False)  # users in room
def add_invisible():
    try:
        api_admin_list = ServiceAdmin()
        res = request.get_json()
        id_user = str(res['id_user'])
        id_admin = str(res['id_admin'])
        return jsonify({'status': api_admin_list.add_invisible(id_user, id_admin)})
    except Exception as e:
        return str(e)


@add_avatar_admin_blueprint.route("/add/avatar/admin", methods=['POST'], strict_slashes=False)  # user nick search
def add_avatar_admin():
    try:
        Avatar = ServiceAvatar()
        res = request.get_json()
        creator = res['creator']
        name = res['name']
        price = res['price']
        return dumps({"name_avatar": Avatar.add_avatar(price, creator, name)})
    except Exception as e:
        print('AdminMapping_add_avatar_admin', e)
        return {"name_avatar": False}


@upload_avatar_admin_blueprint.route("/upload/avatar/admin", methods=['POST'])  # user nick search
def upload_avatar_admin():
    try:
        mongo.save_file("avatars-" + request.files['photo'].filename, request.files["photo"], metadata={
            "_contentType": "image/png",
            "_class": "com.mongodb.BasicDBObject"
        }, content_type='')

        return {"status": True}

    except Exception as e:

        print('AdminMapping_upload_avatar_admin', e)

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
        res = request.get_json()
        creator = res['creator']
        name = res['name']
        price = res['price']
        description = res['description']
        return dumps({"name_gifts": Gift.add_gift(price, creator, name, description)})

    except Exception as e:

        print('AdminMapping_add_avatar_admin', e)

        return {"name_avatar": False}


@upload_gift_admin_blueprint.route("/upload/gift/admin", methods=['POST'])  # user nick search
def upload_gift_admin():
    try:
        mongo.save_file("gifts-" + request.files['photo'].filename, request.files["photo"], metadata={
            "_contentType": "image/png",
            "_class": "com.mongodb.BasicDBObject"
        }, content_type='')

        return {"status": True}

    except Exception as e:

        print('AdminMapping_upload_gift_admin', e)

        return {"status": False}


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
