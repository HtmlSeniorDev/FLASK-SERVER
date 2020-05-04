from flask import Blueprint, jsonify
from datetime import datetime
from .Models.DbModel.UserModel import User

registration_blueprint = Blueprint('registration_blueprint', __name__, )


@registration_blueprint.route("/registration/<login>/<password>/<nick>/<colornick>", methods=['GET'])
def registration(login: str, password: str, nick: str, colornick: int) -> jsonify:
    try:
        User(login=login, password=password, nic=nick, firstName="", lastName="", email="", sex=int(0),
             color=int(colornick), type=int(1), registrationDate=datetime.now(), balace=int(50000), vic=int(0),
             regDeviceId=str("0"), lastVisit=datetime.now()).save()
        return jsonify({'reg': True})
    except Exception as e:
        print(e)
        return jsonify({'reg': False})
