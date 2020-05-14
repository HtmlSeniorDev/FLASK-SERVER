from flask import Blueprint,request
from flask_socketio import emit
from api.Service.ServiceWeddingView import ServiceWeddingView

WeddingList_blueprint = Blueprint('WeddingList_blueprint', __name__, )
Run_line_blueprint = Blueprint('Run_line_blueprint', __name__)


@WeddingList_blueprint.route("/get/WeddingList", methods=['GET'])  # user nick search
def get_weddings_list():
    try:
        api_wedding_list = ServiceWeddingView()
        return api_wedding_list.get_weddings_list()

    except Exception as e:

        return str(e)


@Run_line_blueprint.route("/run/line", methods=['POST'], strict_slashes=False)
def run_line():
    res = request.get_json()
    message = res['message']
    emit('run_text', message, broadcast=True, namespace='/chat')
    return 'line start'
