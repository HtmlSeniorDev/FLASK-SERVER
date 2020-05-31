from bson.objectid import ObjectId

from api.Models.DbModel.UserModel import User
from api.Repository.base_repo import get_conn
from limiter import limiter
from flask import Blueprint, request, jsonify
from api.View.ServiceGifts import ServiceGifts
from api.utils.Server_id import SERVER_ADDRESS
from bson.json_util import dumps
import json

GiftsListBuy_blueprint = Blueprint('GiftsListBuy_blueprint', __name__, )
delete_gifts_blueprint = Blueprint('avatars_blueprint', __name__, )
GiftRequestClient_blueprint = Blueprint('GiftRequestClient_blueprint', __name__, )
gifts_blueprint = Blueprint('gifts_blueprint', __name__, )


@GiftRequestClient_blueprint.route("/Gift/send/", methods=['POST'], strict_slashes=False)  # user search objectid
def gift_send():
    try:
        api_buy = ServiceGifts()
        res = request.get_json()
        gift_price = int((res['price']))
        user_id = str(res['user_id'])
        gift_id = str(res['gift_id'])
        from_id = str(res['from_id'])
        result = api_buy.send_gifts(int(gift_price), user_id, gift_id, from_id)
        return jsonify({"Accept": result})
    except Exception as e:
        print(e)

        return 'no'


@GiftsListBuy_blueprint.route("/get/GiftsList", methods=['GET'])  # user nick search
def get_gifts():
    try:
        api_gifts_list = ServiceGifts()
        return jsonify([e.serialize() for e in api_gifts_list.get_gifts_list_service()])

    except Exception as e:

        return str(e)


@delete_gifts_blueprint.route("/delete/gift/<id_gift>", methods=['GET'])  # user nick search
@limiter.limit("20/1minutes")
def delete_gifts(id_gift):
    try:
        coll_gift = get_conn().db.usergifts
        (coll_gift.delete_one({'_id': ObjectId(str(id_gift))}))
        return True
    except Exception as e:
        print(e)

        return False


@gifts_blueprint.route("/users/gift/<nic>", methods=['GET'])  # user nick search
def found_user_gift(nic):
    global data
    global data_dict
    data = {'data': []}
    data_dict = {}
    print('nic----', str(nic))
    gift_profile = get_conn().db.usergifts
    get_gift = dumps(gift_profile.find({'user': (ObjectId(str(nic)))}))
    count = 0
    arr_gifts_dict = {'url': []}
    arr_gifts = []
    arr_gifts_id = []
    for _ in json.loads(get_gift):
        count += 1

    count_list = -1
    for _ in range(count):
        count_list += 1
        complete_msg = json.loads(get_gift)[count_list]
        gifts = complete_msg['gift']["$oid"]
        gifts_id = complete_msg['_id']['$oid']
        search_description = get_conn().db.gifts.find_one({'_id': ObjectId(str(gifts))})
        get_description = search_description['description']
        get_name = search_description['name']
        arr_gifts_dict['description'] = str(get_description)
        arr_gifts_dict['name'] = str(get_name)
        user = User.objects.get(id=complete_msg["from_"]["$oid"])
        arr_gifts_dict['from'] = str(user.nic)
        arr_gifts_dict['url'] = SERVER_ADDRESS + "/attachments/gift/" + str(gifts)
        arr_gifts_dict['id'] = str(gifts_id)
        arr_gifts.append(dict(arr_gifts_dict))
        arr_gifts_id.append(str(gifts_id))
        data.update({'data': arr_gifts})
    return dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
