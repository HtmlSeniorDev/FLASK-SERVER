from flask import Blueprint, request, jsonify
from api.Service.ServiceAudio import ServiceAudio
import time
from db import mongo
from bson.json_util import dumps
import json
add_audio_blueprint = Blueprint('add_audio_blueprint', __name__, )
get_audio_blueprint = Blueprint('get_audio_blueprint', __name__, )


@add_audio_blueprint.route("/add/audio/", methods=['POST'], strict_slashes=False)  # user nick search
def audio_add():
    try:
        timestamp = int(time.time() * 1000)
        name = 'sound' + str(timestamp) + '.aac'

        add = ServiceAudio()
        movies = request.files["audio"]
        add.add_audio(name, movies)
        save_attach = mongo.db.attachments
        save_attach.insert(
            {'name': str(name), 'user': '5c9a61470a975a14c67bcedb',
             '_class': 'ru.readme.server.object.db.DBAttachment'})
        find = dumps(save_attach.find_one({'name': str(name)}))
        get_id_attachments = json.loads(find)
        get_id = get_id_attachments['_id']['$oid']

        a = jsonify({'attach': get_id, 'name': name})

        return a

    except Exception as e:

        print('audio_add', e)


@get_audio_blueprint.route("/get/audio", methods=['POST'])  # user nick search
def audio_get():
    try:
        add = ServiceAudio()
        res = request.get_json()
        audio_file = (res['audio'])
        user_id = (res['user_id'])

        return add.add_audio(user_id, audio_file)

    except Exception as e:

        return str(e)
