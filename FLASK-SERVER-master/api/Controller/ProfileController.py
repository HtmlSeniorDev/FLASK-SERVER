import json
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import request, Blueprint, jsonify
from ..Repository.UsersDao import UsersDao
from api.View.ServiceProfile import ServiceProfile
from ..Repository.base_repo import get_conn

update_password_blueprint = Blueprint('update_password_blueprint', __name__)
edit_profile_blueprint = Blueprint('edit_profile_blueprint', __name__, )
add_profile_photo_blueprint = Blueprint('add_profile_photo_blueprint', __name__, )
upload_photo_to_profile_blueprint = Blueprint('upload_photo_to_profile_blueprint', __name__, )
delete_photo_to_profile_blueprint = Blueprint('delete_photo_to_profile_blueprint', __name__, )
update_nickname_blueprint = Blueprint("update_nickname_blueprint", __name__)
set_avatar_photo_to_profile_blueprint = Blueprint('set_avatar_photo_to_profile_blueprint', __name__, )
Get_profile_photos_blueprint = Blueprint('Get_profile_photos_blueprint', __name__, )
profile_blueprint = Blueprint('profile_blueprint', __name__, )
UserInfo = UsersDao()


@profile_blueprint.route("/users/profile/<user_id>", methods=['GET'])  # user nick search
def found_user_profile(user_id):
    try:
        response = ServiceProfile.get_profile_information(user_id)
        return jsonify(response)
    except Exception as e:
        print("profile_blueprint", e)


@Get_profile_photos_blueprint.route("/users/photos/<id_user>", methods=['GET'])  # user nick search
def get_profile_photos(id_user):
    try:
        dict_api = {'data': []}
        array_dict_user = []
        dict_user = {}

        online_users = get_conn().db.photos
        photos_object = dumps(online_users.find({'user': ObjectId(str(id_user))}))

        for photo in json.loads(photos_object):
            photos_id = photo['_id']['$oid']
            private = photo['privated']
            description = photo['description']
            create = photo['createdAt']
            dict_user['url'] = 'http://185.231.154.198:5000/photos/' + str(photos_id)
            dict_user['privated'] = private
            dict_user['description'] = description
            dict_user['key'] = photos_id
            dict_user['createdAt'] = create

            array_dict_user.append(dict(dict_user))

        dict_api['data'] = array_dict_user

        complete = dumps(dict_api)

        return complete
    except Exception as e:
        print(e, 'photo exept profile')


# todo доделать отправку в сокет об изменениях цвета и  авиков и ника тд на клиент
@edit_profile_blueprint.route("/edit/profile/", methods=['POST'])  # user nick search
def edit_profile():
    try:
        """Перенаправляем запрос в сервис нужному методу"""
        res = request.get_json()
        serv = ServiceProfile()
        serv.update_profile_information(res)
        return {"status": True}

    except Exception as e:

        print('EDIT_PROFILE', e)

        return {"status": False}


@update_password_blueprint.route("/update/password/", methods=['POST'])  # user nick search
def update_password():
    try:
        """Перенаправляем запрос в сервис нужному методу"""
        res = request.get_json()
        return {"status": ServiceProfile.set_new_password(res)}

    except Exception as e:
        print(e, "update_password-blueprint")
        return {"status": False}


@update_nickname_blueprint.route("/update/nickname/", methods=['POST'])  # user nick search
def update_nickname():
    try:
        """Перенаправляем запрос в сервис нужному методу"""
        res = request.get_json()
        return {"status": ServiceProfile.set_new_nickname(res)}

    except Exception as e:
        print(e, "update_nickname-blueprint")
        return {"status": False}


@add_profile_photo_blueprint.route("/add/photo/", methods=['POST'], strict_slashes=False)  # user nick search
def add_photo_profile():
    try:
        profile = ServiceProfile()
        id_nick = request.form.get('id_nick')
        privated = request.form.get('privated')
        description = request.form.get('description')
        photo = request.files['photo']
        return dumps({"status": profile.add_photo(id_nick, privated, description, photo)})

    except Exception as e:

        print(e)

        return {"status": False}


# todo не удаляется из аватара профиля
@delete_photo_to_profile_blueprint.route("/delete/photo/profile/", methods=['POST'])  # user nick search
def delete_photo_profile():
    try:
        Profile = ServiceProfile()
        res = request.get_json()
        photo_id = res['photo_id']
        Profile.del_photo(photo_id)
        return {"status": True}

    except Exception as e:
        print('delete_photo_profile', e)

        return {"status": False}


@set_avatar_photo_to_profile_blueprint.route("/set/photo/profile/", methods=['POST'])  # user nick search
def set_photo_profile():
    try:
        Profile = ServiceProfile()
        res = request.get_json()
        photo_id = res['photo_id']
        user_id = res['user_id']
        Profile.set_avatar_photo(user_id, photo_id)

        return {"status": True}

    except Exception as e:

        print('set_avatar_profile', e)

        return {"status": False}
