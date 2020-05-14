from flask import Blueprint, request, jsonify
from api.Service.ServiceAvatar import ServiceAvatar

AvatarRequestClient_blueprint = Blueprint('AvatarRequestClient', __name__, )
AvatarSend_blueprint = Blueprint('AvatarSend_blueprint', __name__, )
AvatarAccept_blueprint = Blueprint('AvatarAccept_blueprint', __name__, )
AvatarList_blueprint = Blueprint('AvatarList_blueprint', __name__, )


@AvatarList_blueprint.route("/get/AvatarList", methods=['GET'])  # user nick search
def get_avatar_list():
    try:
        api_avatar_list = ServiceAvatar()
        return jsonify([e.serialize() for e in api_avatar_list.combine_avatar_list()])
    except Exception as e:

        return str(e)


@AvatarRequestClient_blueprint.route("/Avatar/buy/", methods=['POST'], strict_slashes=False)  # user search objectid
def buy_avatar():
    api_buy = ServiceAvatar()
    res = request.get_json()
    avatar_price = int((res['price']))
    user_id = str(res['user_id'])
    avatar_id = str(res['avatar_id'])
    result = api_buy.buy_avatars(int(avatar_price), user_id, avatar_id)
    return jsonify({"Accept": result})


@AvatarSend_blueprint.route("/Avatar/send/", methods=['POST'], strict_slashes=False)  # user search objectid
def send_avatar():
    api_buy = ServiceAvatar()
    res = request.get_json()
    avatar_price = int((res['price']))
    user_id = str(res['user_id'])
    avatar_id = str(res['avatar_id'])
    accepter_user_id = str(res['accepter_user_id'])
    result = api_buy.send_avatars(int(avatar_price), user_id, avatar_id, accepter_user_id)
    return jsonify({"Accept": result})


@AvatarAccept_blueprint.route("/Avatar/accept/", methods=['POST'], strict_slashes=False)  # user search objectid
def accept_avatar():
    api_buy = ServiceAvatar()
    res = request.get_json()
    accepter_user_id = str(res['accepter_user_id'])
    result = api_buy.accept_avatar_send(accepter_user_id)
    return jsonify({"Accept": result})
