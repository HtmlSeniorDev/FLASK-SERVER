from flask import Blueprint, request, jsonify
from flask_socketio import emit
from api.View.ServiceChatPortal import ServiceChatPortal

WeddingList_blueprint = Blueprint('WeddingList_blueprint', __name__, )
Run_line_blueprint = Blueprint('Run_line_blueprint', __name__)
Friends_invite_blueprint = Blueprint("Friends_invite_blueprint", __name__)
Friends_list_blueprint = Blueprint("Friends_list_blueprint", __name__)
Friends_request_list_blueprint = Blueprint("Friends_request_list_blueprint", __name__)
Friends_accsess_blueprint = Blueprint("Friends_accsess_blueprint", __name__)
Friends_delete_blueprint = Blueprint("Friends_delete_blueprint", __name__)


@WeddingList_blueprint.route("/get/WeddingList", methods=['GET'])  # user nick search
def get_weddings_list():
    try:
        api_wedding_list = ServiceChatPortal()
        return api_wedding_list.get_weddings_list()

    except Exception as e:

        return str(e)


@Run_line_blueprint.route("/run/line", methods=['POST'], strict_slashes=False)
def run_line():
    res = request.get_json()
    message = res['message']
    emit('run_text', message, broadcast=True, namespace='/chat')
    return 'line start'


@Friends_invite_blueprint.route("/friend", methods=['POST'], strict_slashes=False)
def invite_friend():
    res = request.get_json()
    a = ServiceChatPortal()
    return jsonify({"status": a.invite_friends(res)})


@Friends_request_list_blueprint.route("/friend/request/<user>", methods=["GET"])
def request_friends_list(user):
    try:
        return jsonify(ServiceChatPortal.friend_request_list(user))
    except Exception as e:
        return ("user not found", 400)


@Friends_accsess_blueprint.route("/friend", methods=["PUT"])
def request_accsess_friend():
    try:
        res = request.get_json()
        a = ServiceChatPortal()
        return jsonify({"status": a.access_friends(res)})

    except Exception as e:
        return (e, "user not found", 400)


@Friends_list_blueprint.route("/friend/<user_id>", methods=["GET"])
def get_friends_list(user_id):
    try:
        return jsonify(ServiceChatPortal.get_friends_list(user_id))
    except Exception as e:
        return ("user not found", 400)


@Friends_delete_blueprint.route("/friend", methods=["DELETE"])
def friend_delete(data):
    try:
        return jsonify(ServiceChatPortal.delete_friend(data))
    except Exception as e:
        return ("user not found", 400)
