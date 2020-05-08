import json
from bson.objectid import ObjectId
from bson.json_util import dumps
from db import mongo
from flask import request, Blueprint
from ..Repository.UsersDao import UsersDao
from ..Service.ServiceProfile import ServiceProfile
from ..Objects.Server_id import SERVER_ADDRESS

edit_profile_blueprint = Blueprint('edit_profile_blueprint', __name__, )
add_profile_photo_blueprint = Blueprint('add_profile_photo_blueprint', __name__, )
upload_photo_to_profile_blueprint = Blueprint('upload_photo_to_profile_blueprint', __name__, )
delete_photo_to_profile_blueprint = Blueprint('delete_photo_to_profile_blueprint', __name__, )
set_avatar_photo_to_profile_blueprint = Blueprint('set_avatar_photo_to_profile_blueprint', __name__, )
Get_profile_photos_blueprint = Blueprint('Get_profile_photos_blueprint', __name__, )
profile_blueprint = Blueprint('profile_blueprint', __name__, )
UserInfo = UsersDao()


@profile_blueprint.route("/users/profile/<nic>", methods=['GET'])  # user nick search
def found_user(nic):
    try:
        global data
        global data_dict
        global nick
        data = []
        data_dict = {}
        online_users = mongo.db.users
        nick = (online_users.find_one({'_id': ObjectId(str(nic))}))
        photo = str(nick['photo'])
        if len(photo) >= 1:
            url_att = SERVER_ADDRESS + '/photos/' + photo
    except Exception as e:
        url_att = 'image_exist'

    nick.update({'photo': url_att})
    nick.update({'avatarEndAt': '1'})
    nick.update({'balace': int(nick['balace']) / 100})
    nick.update({'login': '1'})
    nick.update({'password': '1'})
    if 'zags' in nick:
        pass
    else:
        nick.update({'zags': ''})
    if 'zagsRequest' in nick:
        pass
    else:
        nick.update({'zagsRequest': []})
    if 'bday' in nick:
        global time
        time = (nick['bday'])
        try:
            global time_bday
            time_bday = time.strftime("%m/%d/%Y")
            time_bday = time_bday.replace('/', '.')
            nick.update({'bday': time_bday})
        except Exception:
            nick.update({'bday': time})
            pass
    color = nick['color']
    nick.update({'bday': '2019'})
    if 'city' in nick:
        nick.update({'city': nick['city']})
    else:
        nick.update({'city': ''})
    if 'about' in nick:
        nick.update({'about': nick['about']})
    else:
        nick.update({'about': ''})
    if ('firstName') in nick:
        nick.update({'firstName': nick['firstName']})
    else:
        nick.update({'firstName': ''})
    if 'lastName' in nick:
        nick.update({'lastName': nick['lastName']})
    else:
        nick.update({'lastName': ''})
    if nick['sex'] == 3:
        nick.update({'sex': 'Не определен'})
    elif nick['sex'] == 1:
        nick.update({'sex': 'Мужской'})
    elif nick['sex'] == 2:
        nick.update({'sex': 'Женский'})
    nick.update({'color': color})
    data.append(nick)
    data_dict['data'] = data
    return dumps(data_dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


@Get_profile_photos_blueprint.route("/users/photos/<id_user>", methods=['GET'])  # user nick search
def get_profile_photos(id_user):
    try:
        dict_api = {'data': []}
        array_dict_user = []
        dict_user = {}

        online_users = mongo.db.photos
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


@edit_profile_blueprint.route("/edit/profile/", methods=['POST'])  # user nick search
def edit_profile():
    try:
        user = UsersDao()
        res = request.get_json()
        user.change_information_user(res['user_id'], {

            "bday": res['bday'],
            "firstName": res['firstName'],
            "lastName": res['lastName'],
            "city": res['city'],
            "email": res['email'],
            "sex": res['sex'],
            "color": res['color'],
            "about": res['about']

        })

        return {"status": True}

    except Exception as e:

        print('EDIT_PROFILE', e)

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
