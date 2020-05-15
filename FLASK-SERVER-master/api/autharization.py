from flask import Blueprint, jsonify
from api.View.ServicePushNotification import ServicePushNotification
from api.View.ServiceCheckBanned import ServiceCheckBanned
from db import mongo

autharization_blueprint = Blueprint('autharization_blueprint', __name__, )


@autharization_blueprint.route("/authChatApp/<login>/<password>/<imei>/<FcmToken>",
                               methods=['GET'])  # user search objectid
def autharization(login, password, imei, FcmToken):
    try:
        failed_auth = jsonify({'auth': False})
        Push = ServicePushNotification()
        Check = ServiceCheckBanned()
        if len(login) > 16 or len(password) > 16:
            a = {'reg': 'No'}
            return jsonify({'auth': False})
        else:
            try:
                online_users = mongo.db.users
                log = (online_users.find_one({'login': login}))
                Push.add_push_token(str(FcmToken), log['_id'])
                if (log['login'] == login) and (log['password'] == password):
                    Check.check_banned(log['_id'],
                                       imei)  # Проверяем есть ли такой же емэй со статусом забаненного,если да ,вешаем бан на текущий ник
                    validatorTrue = {'auth': True, 'nic': str(log['_id'])}
                    return jsonify(validatorTrue)
                else:
                    return failed_auth
            except Exception as e:
                print(e)
                return failed_auth
    except Exception as e:

        return print("error", e)
