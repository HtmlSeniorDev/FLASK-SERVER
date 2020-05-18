from flask import session, request
from flask_socketio import emit, join_room
from api.Repository.UsersDao import UsersDao
from api.View.ServiceRoomUser import ServiceRoomUser
from init import socketio
from limiter import limiter
from .Model_Message import MODEL_MESSAGE
from .Strings import ENTRY_TEXT, LEAVE_TEXT
import uuid
from bson.objectid import ObjectId
from bson.json_util import dumps
import json
from datetime import datetime
from api.Repository.AttachmentsDao import AttachmentsDao
from api.Repository.MessagesDao import MessagesDao

User = UsersDao()
Attachments = AttachmentsDao()
MESSAGES_DAO = MessagesDao()
UserConnected = []


def get_user_room_from_sid(sid) -> dict:  # ищем пользователя по sid для удаления из комнаты в бд
    count = -1  # Потому что массив начинается с нулевого элемента
    for con_client in UserConnected:
        count += 1
        if sid == con_client['sid']:
            user = con_client['user']
            room = con_client['room']
            nic = con_client['nic']
            remove_que = {"user": user, "room": room, "nic": nic}

            del UserConnected[count]  # Удаление юзера из списка подключенных
            return remove_que


def write_socket_con(sid, user, room, nic):  # Записываем подключенных в комнате юзеров
    user_con = {'sid': sid, 'user': user, 'room': room, "nic": nic}
    UserConnected.append(user_con)
    print('NEW_USER:', user)


def write_last_message(message):  # Записываем последние сообщения во всех комнатах чатах
    write_last_message_pm_mongo(message)
    ServiceRoomUser.insert_user_in_room(message["user"],message["room"])


def get_last_message() -> list:  # Получаем список последних сообщений для конкретной комнаты
    msg_room = []
    mongo_msg = dumps(MESSAGES_DAO.read_message({'place': session['room'], "hideNic": False}))
    for msg in json.loads(mongo_msg):
        msg_room.append(msg)

    return msg_room


def insert_or_delete_user_room_to_db(selector, user, room):  # В зависимости от выбора del/add юзера в комнату
    if selector == 'connected':
        ServiceRoomUser.insert_user_in_room(user, room)
    elif selector == 'disconnected':
        ServiceRoomUser.delete_user_in_room(user, room)


def update_leave_msg(user, room, nic):  # Обновляем модель сообщения для выхода из комнаты
    MODEL_MESSAGE['user'] = user
    MODEL_MESSAGE['room'] = room
    MODEL_MESSAGE['nic'] = nic
    MODEL_MESSAGE['message'] = LEAVE_TEXT


def find_attachments_name(attachments_id) -> str:
    attachments = dumps(Attachments.find_name({'_id': ObjectId(attachments_id)}))
    attach = json.loads(attachments)
    return attach['name']


'''_________________PM ACTION FUNCTIONS___________________'''


def write_last_message_pm_mongo(message):  # Записываем приватные сообщения из монги для конкретной комнаты(query=room)

    return MESSAGES_DAO.send_message(message)


'''_________________socket_routes___________________'''


@socketio.on('connect', namespace='/chat')
@limiter.limit("10/10minutes")
def connect():
    print('Client_connected_now', request.sid)


# todo сделать сообщения прочитанными или нет в зависимости от айди пользователя
@socketio.on('joined', namespace='/chat')
@limiter.limit("1/3second")
def joined(msg):
    session['user'] = msg['user']
    session['room'] = msg['room']

    room = (session['room'])
    msg.update({'hideNic': True})
    key = uuid.uuid1()
    msg.update({'key': str(key)})
    del msg['avatar']
    msg['message'] = ENTRY_TEXT
    join_room(room)
    emit('status', msg, room=room)
    emit('last_message', get_last_message()[-25:-1], broadcast=False, user=session['user'])
    insert_or_delete_user_room_to_db('connected', session['user'], room)
    write_socket_con(request.sid, session['user'], room, msg['nic'])


@socketio.on('text', namespace='/chat')
def text(message):
    room = session['room']
    key = uuid.uuid1()
    message.update({'key': str(key)})
    if len(message['attachments']) > 0:
        attachments = find_attachments_name(message['attachments'])
        message.update({'attachments': [attachments]})
    emit('message', message, room=room)
    message['createdAt'] = datetime.now()
    message['place'] = message['room']
    del message['room']
    write_last_message(message)


@socketio.on('disconnect', namespace='/chat')
def disconnect():
    print('Client_disconnected_now', request.sid)
    remove_user = get_user_room_from_sid(request.sid)
    user = remove_user['user']
    room = remove_user['room']
    nic = remove_user['nic']
    update_leave_msg(user, room, nic)
    msg_leave = dumps(MODEL_MESSAGE)
    emit('status', json.loads(msg_leave), room=room)
    insert_or_delete_user_room_to_db('disconnected', user, room)
