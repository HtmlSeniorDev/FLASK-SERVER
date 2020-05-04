from bson import ObjectId
from flask import Blueprint, send_file, redirect, request
from ..Models.DbModel.AvatarModel import Avatar
from ..Models.DbModel.GiftModel import Gift
from ..Objects.Server_id import SERVER_ADDRESS, SERVER_ID
import io
from bson.json_util import dumps
import json
from gridfs import GridFS
from limiter import limiter
import time
from db import mongo

get_attachments_gift_blueprint = Blueprint('get_attachments_gift_blueprint', __name__, )
get_attachments_avatar_blueprint = Blueprint('get_attachments_avatar_blueprint', __name__, )
uploads_attachments_blueprint = Blueprint('uploads_attachments_blueprint', __name__, )
"""Получаем изображения по url (аватарки,подарки)"""


# @get_attachments_blueprint.route("/photos/<filename>", methods=['GET'])
# def get_photo(filename):
#     try:
#         file = GridFile.objects(filename=filename).first()
#         file = file.photo.content_type
#         return send_file(io.BytesIO(file),
#                          attachment_filename='logo.jpeg',
#                          mimetype='image/jpeg')
#     except Exception as e:
#         print('get_attachments_error', e)
#
#         return redirect(SERVER_ADDRESS + '/static/avatar_exist.png/', code=302)
#
#

@get_attachments_gift_blueprint.route("/attachments/gift/<file_id>", methods=['POST', 'GET'])
def get_attachments_gift(file_id):
    try:
        return send_file(io.BytesIO(Gift.objects.get(id=ObjectId(file_id)).photo.read()),
                         attachment_filename='logo.jpeg',
                         mimetype='image/png')

    except Exception as e:
        print(e)


@get_attachments_avatar_blueprint.route("/attachments/avatar/<file_id>", methods=['POST', 'GET'])
def get_attachments_avatar(file_id):
    try:
        return send_file(io.BytesIO(Avatar.objects.get(id=ObjectId(file_id)).photo.read()),
                         attachment_filename='logo.jpeg',
                         mimetype='image/png')

    except Exception as e:
        print(e)
# return redirect(SERVER_ADDRESS + '/static/avatar_exist.png/', code=302)
