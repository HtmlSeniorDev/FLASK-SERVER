from flask import Blueprint
from bson.json_util import dumps
from bson.objectid import ObjectId
from db import mongo
from .Objects.Server_id import SERVER_ADDRESS

other_function_blueprint = Blueprint('other_function_blueprint', __name__, )


@other_function_blueprint.route("/check/login/<iduser>", methods=['GET'])  # user nick search
def found_user_login(iduser):
    online_users = mongo.db.users
    nick = (online_users.find_one({'_id': ObjectId(str(iduser))}))
    color = nick['color']
    if 'avatarLink' in nick:
        avatar = SERVER_ADDRESS + '/attachments/avatar/' + nick['avatarLink']
    else:
        avatar = False
    nickname = {'Nickname': (nick['nic']), 'type': (nick['type']), 'color': color, 'avatar': avatar}

    return dumps(nickname)


@other_function_blueprint.route("/banned/room/<name>", methods=['GET'])  # check banned user
def banned_action(name):
    online_users = mongo.db.users
    nick = (online_users.find_one({'_id': ObjectId(str(name))}))

    banned = {'user': 'banned'}
    unbanned = {'user': 'unbanned'}

    if nick['type'] == int(8):

        return dumps(banned)

    else:

        return dumps(unbanned)
