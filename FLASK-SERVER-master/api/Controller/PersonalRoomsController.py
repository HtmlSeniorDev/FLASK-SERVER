from flask import Blueprint, jsonify
from api.View.ServiceFindPersonalRoom import ServiceFindPersonalRooms

find_personalrooms_blueprint = Blueprint('find_personalrooms_blueprint', __name__, )


@find_personalrooms_blueprint.route("/personalrooms/<my_id>", methods=['GET'])  # user nick search
def get_personalrooms_list(my_id):
    try:
        api_personal_rooms_list = ServiceFindPersonalRooms()
        data = api_personal_rooms_list.find_personal_rooms(my_id)
        return jsonify(data)

    except Exception as e:

        return str(e)
