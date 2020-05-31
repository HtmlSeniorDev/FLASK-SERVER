from flask import Blueprint, jsonify
from datetime import datetime

from limiter import limiter
from .Models.DbModel.UserModel import User

registration_blueprint = Blueprint('registration_blueprint', __name__, )


@limiter.limit("10/day")
@registration_blueprint.route("/registration/<login>/<password>/<nick>/<colornick>", methods=['GET'])
def registration(login: str, password: str, nick: str, colornick: int) -> jsonify:
    try:
        time_reg = datetime.now()
        User(login=login, password=password, nic=nick, sex=int(0),
             color=int(colornick), type=int(1), registrationDate=time_reg, bday=time_reg, balace=int(50), vic=int(0),
             friends=[], zagsRequest=[], firstName="Чаттер", lastName="Чаттеров", city="Чатляндия",
             about="Познакомлюсь!",
             regDeviceId=str("0"), lastVisit=datetime.now()).save()

        return jsonify({'reg': True})
    except Exception as e:
        print(e)
        return jsonify({'reg': False})
