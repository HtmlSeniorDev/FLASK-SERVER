from bson import ObjectId
from flask import Blueprint, send_file
from ..Models.DbModel.AvatarModel import Avatar
from ..Models.DbModel.GiftModel import Gift
from ..Models.DbModel.Photo import Photo
import io

get_attachments_photos_profile_blueprint = Blueprint('get_attachments_photos_profile_blueprint', __name__, )
get_attachments_gift_blueprint = Blueprint('get_attachments_gift_blueprint', __name__, )
get_attachments_avatar_blueprint = Blueprint('get_attachments_avatar_blueprint', __name__, )
uploads_attachments_blueprint = Blueprint('uploads_attachments_blueprint', __name__, )

"""Получаем изображения по url (аватарки,подарки,фото,вложения)"""


@get_attachments_photos_profile_blueprint.route("/photos/<file_id>", methods=['POST', 'GET'])
def get_attachments_photos(file_id):
    try:
        return send_file(io.BytesIO(Photo.objects.get(id=ObjectId(file_id)).photo.read()),
                         mimetype='image/png')

    except Exception as e:
        print(e)


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
