from flask import Blueprint, jsonify, request
from api.View.ServiceNotice import ServiceNotice
from limiter import limiter

ShowNotice_blueprint = Blueprint('ShowNotice_blueprint', __name__, )


@ShowNotice_blueprint.route("/get/notice/", methods=['POST'], strict_slashes=False)  # user nick search
@limiter.limit("1/10seconds")
def get_notice():
    try:

        res = request.get_json()
        user = res['user']
        notice_status = ServiceNotice()

        return jsonify(notice_status.show_notice(user))

    except Exception as e:

        return str(e)
