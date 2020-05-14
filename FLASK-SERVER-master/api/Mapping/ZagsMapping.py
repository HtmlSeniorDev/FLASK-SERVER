from flask import Blueprint, request, jsonify
from api.Service.ServicePushNotification import ServicePushNotification
from api.Service.ServiceZags import ServiceZags

Zags_Request_blueprint = Blueprint('Zags_Request_blueprint', __name__, )
Zags_Request_Decline_blueprint = Blueprint('Zags_Request_Decline_blueprint', __name__, )
Zags_Accept_blueprint = Blueprint('Zags_Accept_blueprint', __name__, )
Zags_Delete_blueprint = Blueprint('Zags_Delete_blueprint', __name__, )

Push = ServicePushNotification()
Zags = ServiceZags()


@Zags_Accept_blueprint.route("/sending/zags/accept/", methods=['POST'], strict_slashes=False)
def get_request():
    try:

        global res
        res = request.get_json()
        user_request = (res['user_request'])
        user_from_request = (res['user_from'])
        print('ID USER REQUEST TO WEDDING:', user_request)
        print('ID USER REQUEST TO from:', user_from_request)
        result = Zags.accept_zags_request(user_request, user_from_request)
        return jsonify({"Accept": result})

    except Exception as e:

        return str(e)


@Zags_Delete_blueprint.route("/sending/zags/delete/", methods=['POST'], strict_slashes=False)
def get_request_delete():
    try:

        global res
        res = request.get_json()
        user_request = (res['user_request'])
        user_from_request = (res['user_from'])
        result = Zags.delete_zags(user_request, str(user_from_request))
        return jsonify({"Accept": result})

    except Exception as e:

        return str(e)


@Zags_Request_blueprint.route("/sending/zags/request/", methods=['POST'], strict_slashes=False)
def get_request():
    try:

        global res
        res = request.get_json()
        user_request = (res['user_request'])
        user_from_request = (res['user_from'])
        result = Zags.update_zags_request(str(user_request), str(user_from_request))
        return jsonify({"Accept": result})

    except Exception as e:

        return str(e)


@Zags_Request_Decline_blueprint.route("/sending/zags/request/decline/", methods=['POST'], strict_slashes=False)
def decline_request():
    try:

        global res
        res = request.get_json()
        user_request = (res['user_request'])
        user_from_request = (res['user_from'])
        Zags.decline_zags_request(user_request[0], user_from_request)
        return jsonify({"Accept": True})

    except Exception as e:

        return str(e)
