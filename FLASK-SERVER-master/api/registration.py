from flask import Blueprint, jsonify
from datetime import datetime
from .Models.DbModel.UserModel import User

registration_blueprint = Blueprint('registration_blueprint', __name__, )


@registration_blueprint.route("/registration/<login>/<password>/<nick>/<colornick>", methods=['GET'])
def registration(login: str, password: str, nick: str, colornick: int) -> jsonify:
    try:
        timereg = datetime.now()
        User(login=login, password=password, nic=nick, sex=int(0),
             color=int(colornick), type=int(1), registrationDate=timereg, bday=timereg, balace=int(50), vic=int(0),
             regDeviceId=str("0"), lastVisit=datetime.now()).save()
        return jsonify({'reg': True})
    except Exception as e:
        print(e)
        return jsonify({'reg': False})
