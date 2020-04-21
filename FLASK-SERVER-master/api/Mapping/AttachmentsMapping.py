from flask import Blueprint, send_file, redirect,request
from pymongo import MongoClient
from ..Objects.Server_id import SERVER_ADDRESS,SERVER_ID
import io
from bson.json_util import dumps
import json
from gridfs import GridFS
from limiter import limiter
import time
from db import mongo

get_attachments_blueprint = Blueprint('get_attachments_blueprint', __name__, )
uploads_blueprint = Blueprint('uploads_blueprint', __name__, )

@uploads_blueprint.route("/uploads", methods=["POST"])
@limiter.limit("1/1minutes")
def save_upload():
  try:
    timestamp = int(time.time() * 1000)
    name = str(timestamp) + "_" + str(timestamp) + '23.jpeg'
    mongo.save_file(name, request.files["photo"], metadata={
        "_contentType": "image/png",
        "_class": "com.mongodb.BasicDBObject"
    }, content_type='')
    save_attach = mongo.db.attachments
    save_attach.insert(
        {'name': str(name), 'user': SERVER_ID, '_class': 'ru.readme.server.object.db.DBAttachment'})
    find = dumps(save_attach.find_one({'name': str(name)}))
    get_id_attachments = json.loads(find)
    get_id = get_id_attachments['_id']['$oid']
    a = {'attach': get_id, 'name': name}
    return dumps(a)
  except Exception:

      print ('uploads exception')

@get_attachments_blueprint.route("/photos/<filename>", methods=['GET'])
def get_photo(filename):
    try:
        mongo_client = MongoClient('mongodb://localhost:27017')
        db = mongo_client['chat']
        grid_fs = GridFS(db)

        grid_fs_file = grid_fs.find_one({'filename': 'avatars-' + filename})
        print(grid_fs_file)
        response = (grid_fs_file.read())

        return send_file(io.BytesIO(response), attachment_filename='logo.jpeg',
                         mimetype='image/jpeg')
    except Exception:
        print('get_attachments_error')

        return redirect(SERVER_ADDRESS + '/static/avatar_exist.png/', code=302)


@get_attachments_blueprint.route("/attachments/<filename>", methods=['POST', 'GET'])
def get_attachments(filename):
    try:
        mongo_client = MongoClient('mongodb://localhost:27017')
        db = mongo_client['chat']
        grid_fs = GridFS(db)

        if filename.startswith('sound'):
            meme = 'audio/aac'
            attch = filename

        else:
            meme = 'image/png'
            attch = filename
        grid_fs_file = grid_fs.find_one({'filename': filename})
        print(grid_fs_file)
        response = (grid_fs_file.read())

        return send_file(io.BytesIO(response), attachment_filename=attch,
                         mimetype=meme, as_attachment=True)

    except Exception as e:

        return redirect(SERVER_ADDRESS + '/static/user_exist.png/', code=302)
