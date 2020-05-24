from datetime import datetime
from bson import ObjectId
from api.Models.DbModel.BannedUser import BannedUser
from api.Models.DbModel.UserModel import User
from api.utils.Server_id import TYPE_USER

"""Шедулер для тюрьмы"""

class BannedScheduler:
    time = datetime.now()

    def check_banned_scheduler(self):
        try:
            users = BannedUser.objects.all()
            for banneduser in users:
                if banneduser.endAt < self.time:
                    User.objects(id=ObjectId(banneduser.userId.id)).update_one(
                        set__type__=TYPE_USER,
                    )
                    banneduser.delete()
        except Exception as e:
            print('check_banned_scheduler', e)
