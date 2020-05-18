from flask import Blueprint, request, jsonify
from api.View.ServiceAvatar import ServiceAvatar

AvatarRequestClient_blueprint = Blueprint('AvatarRequestClient', __name__, )
AvatarSend_blueprint = Blueprint('AvatarSend_blueprint', __name__, )
AvatarAccept_blueprint = Blueprint('AvatarAccept_blueprint', __name__, )
AvatarList_blueprint = Blueprint('AvatarList_blueprint', __name__, )
Avatar_Checked_blueprint = Blueprint("Avatar_Checked_blueprint", __name__)


@AvatarList_blueprint.route("/get/AvatarList", methods=['GET'])  # user nick search
def get_avatar_list():
    try:
        api_avatar_list = ServiceAvatar()
        return jsonify([e.serialize() for e in api_avatar_list.combine_avatar_list()])
    except Exception as e:

        return str(e)


@AvatarRequestClient_blueprint.route("/Avatar/buy/", methods=['POST'], strict_slashes=False)  # user search objectid
def buy_avatar():
    try:
        api_buy = ServiceAvatar()
        res = request.get_json()
        avatar_price = int((res['price']))
        user_id = str(res['user_id'])
        avatar_id = str(res['avatar_id'])
        result = api_buy.buy_avatars(int(avatar_price), user_id, avatar_id)
        return jsonify({"Accept": result})
    except Exception as e:
        return jsonify({"Accept": False})


@AvatarSend_blueprint.route("/avatar/send/", methods=['POST'], strict_slashes=False)  # user search objectid
def send_avatar():
    try:
        req = request.get_json()
        return jsonify({"status": ServiceAvatar.send_user_avatar(req)})
    except Exception as e:
        print(e, 'AVATAR_SEND_ERROR')
        return jsonify({"status": False})


@AvatarAccept_blueprint.route("/avatar/accept/", methods=['POST'], strict_slashes=False)  # user search objectid
def accept_avatar():
    try:
        res = request.get_json()
        service = ServiceAvatar()
        return jsonify({"status": service.accept_user_avatar(res)})
    except Exception as e:
        print(e, 'AVATAR_SEND_ERROR')
        return jsonify({"status": False})


@Avatar_Checked_blueprint.route("/avatar/check/<user>", methods=["GET"])
def checking_avatar(user):
    try:
        response = ServiceAvatar.check_avatar_send(user)
        return jsonify(response)
    except Exception as e:
        pass
