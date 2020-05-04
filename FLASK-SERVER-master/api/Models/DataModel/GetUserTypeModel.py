class GetUserTypeModel:
    def __init__(self, user_id, nic, color):
        self.user_id = user_id
        self.nic = nic
        self.color = color

    def serialize(self):
        return {
            'user_id': self.user_id,
            'nic': self.nic,
            'color': self.color,
        }
