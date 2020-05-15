from api.registration import registration_blueprint
from api.autharization import autharization_blueprint

from api.Controller.GiftsMapping import delete_gifts_blueprint, GiftsListBuy_blueprint, GiftRequestClient_blueprint, \
    gifts_blueprint

from api.Controller.ProfileMapping import edit_profile_blueprint, profile_blueprint, add_profile_photo_blueprint, \
    upload_photo_to_profile_blueprint, delete_photo_to_profile_blueprint, set_avatar_photo_to_profile_blueprint, \
    Get_profile_photos_blueprint, update_password_blueprint, update_nickname_blueprint

from api.other_function import other_function_blueprint
from init import create_app
from sys import getdefaultencoding

from api.Controller.AvatarMapping import AvatarRequestClient_blueprint, AvatarSend_blueprint, AvatarAccept_blueprint, \
    AvatarList_blueprint, Avatar_Checked_blueprint
from api.Controller.ZagsMapping import Zags_Request_Decline_blueprint, Zags_Request_blueprint, Zags_Accept_blueprint, \
    Zags_Delete_blueprint

from api.Controller.PersonalRoomsMapping import find_personalrooms_blueprint

from api.Controller.AttachmentsMapping import get_attachments_gift_blueprint, get_attachments_avatar_blueprint, \
    get_attachments_photos_profile_blueprint

from api.Controller.PortalMapping import WeddingList_blueprint, Run_line_blueprint, Friends_invite_blueprint, \
    Friends_list_blueprint, Friends_accsess_blueprint, Friends_request_list_blueprint

from api.Controller.AdminMapping import AdminList_blueprint, moderator_list_blueprint, \
    invisible_list_blueprint, \
    Unban_Actions_blueprint, add_avatar_admin_blueprint, update_avatar_admin_blueprint, \
    delete_avatar_admin_blueprint, add_gift_admin_blueprint, upload_gift_admin_blueprint, update_gift_admin_blueprint, \
    delete_gift_admin_blueprint

from api.Controller.RoomsMapping import GetRooms_blueprint, users_room_blueprint, last_room_blueprint, \
    delete_personalrooms_blueprint, create_private_blueprint, Update_Category_blueprint, Delete_Category_blueprint, \
    Create_Room_blueprint, Create_Category_blueprint, users_list_view_blueprint

from api.Controller.NoticeMapping import ShowNotice_blueprint

from api.Controller.AudioMapping import add_audio_blueprint

from SERVER_CONFIG import SERVER_ADDRESS, SERVER_PORT
from apscheduler.schedulers.background import BackgroundScheduler
from Scheduler_color import ServiceScheduler
from main import main
from init import socketio

getdefaultencoding()

app = create_app()
app.register_blueprint(Friends_request_list_blueprint)
app.register_blueprint(Friends_list_blueprint)
app.register_blueprint(Friends_accsess_blueprint)
app.register_blueprint(Friends_list_blueprint)
app.register_blueprint(Friends_invite_blueprint)
app.register_blueprint(Avatar_Checked_blueprint)
app.register_blueprint(update_nickname_blueprint)
app.register_blueprint(update_password_blueprint)
app.register_blueprint(Run_line_blueprint)
app.register_blueprint(update_gift_admin_blueprint)
app.register_blueprint(delete_gift_admin_blueprint)
app.register_blueprint(add_gift_admin_blueprint)
app.register_blueprint(upload_gift_admin_blueprint)
app.register_blueprint(update_avatar_admin_blueprint)
app.register_blueprint(delete_avatar_admin_blueprint)
app.register_blueprint(add_avatar_admin_blueprint)
app.register_blueprint(delete_photo_to_profile_blueprint)
app.register_blueprint(set_avatar_photo_to_profile_blueprint)
app.register_blueprint(upload_photo_to_profile_blueprint)
app.register_blueprint(add_profile_photo_blueprint)
app.register_blueprint(main)
app.register_blueprint(add_audio_blueprint)
app.register_blueprint(Create_Room_blueprint)
app.register_blueprint(Create_Category_blueprint)
app.register_blueprint(Delete_Category_blueprint)
app.register_blueprint(Update_Category_blueprint)
app.register_blueprint(ShowNotice_blueprint)
app.register_blueprint(AdminList_blueprint)
app.register_blueprint(GetRooms_blueprint)
app.register_blueprint(WeddingList_blueprint)
app.register_blueprint(AvatarSend_blueprint)
app.register_blueprint(AvatarAccept_blueprint)
app.register_blueprint(Zags_Delete_blueprint)
app.register_blueprint(Zags_Request_Decline_blueprint)
app.register_blueprint(Zags_Accept_blueprint)
app.register_blueprint(Zags_Request_blueprint)
app.register_blueprint(GiftRequestClient_blueprint)
app.register_blueprint(Unban_Actions_blueprint)
app.register_blueprint(GiftsListBuy_blueprint)
app.register_blueprint(AvatarRequestClient_blueprint)
app.register_blueprint(AvatarList_blueprint)
app.register_blueprint(Get_profile_photos_blueprint)
app.register_blueprint(invisible_list_blueprint)
app.register_blueprint(moderator_list_blueprint)
app.register_blueprint(last_room_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(autharization_blueprint)
app.register_blueprint(get_attachments_gift_blueprint)
app.register_blueprint(delete_gifts_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(get_attachments_avatar_blueprint)
app.register_blueprint(find_personalrooms_blueprint)
app.register_blueprint(gifts_blueprint)
app.register_blueprint(users_room_blueprint)
app.register_blueprint(edit_profile_blueprint)
app.register_blueprint(create_private_blueprint)
app.register_blueprint(users_list_view_blueprint)
app.register_blueprint(other_function_blueprint)
app.register_blueprint(delete_personalrooms_blueprint)
app.register_blueprint(get_attachments_photos_profile_blueprint)

# JOB = ServiceScheduler()
# scheduler = BackgroundScheduler()
# scheduler.add_job(JOB.combine_avatar_lists, trigger='interval', seconds=40)
# scheduler.add_job(JOB.delete_blocking, trigger='interval', minutes=15)
# scheduler.add_job(JOB.auto_admin, trigger='interval', seconds=3)
# scheduler.add_job(JOB.auto_user, trigger='interval', seconds=3)
# scheduler.add_job(JOB.delete_avatar_if_price_zero, trigger='interval', seconds=5)
# scheduler.start()


if __name__ == '__main__':
    socketio.run(app, port=SERVER_PORT, host=SERVER_ADDRESS, debug=True)  # 79.174.12.77
