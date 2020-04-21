from datetime import datetime
import uuid

last_time = datetime.now()

key = uuid.uuid1()
MODEL_MESSAGE = {"room": None,
                 "user": None,
                 "message": None,
                 "system": False,
                 "hideNic": True,
                 "attachments": [],
                 "readed": False,
                 "nic": None,
                 "color": "#010101",
                 "avatar": False,
                 "createdAt": last_time,
                 "key": str(key)}
