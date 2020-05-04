class ListAvatarsModel:
    def __init__(self, avatar_id, url, price, name):
        self.avatar_id = avatar_id
        self.url = url
        self.price = price
        self.name = name

    def serialize(self):
        return {
            'id': self.avatar_id,
            'url': self.url,
            'price': self.price,
            'name': self.name
        }
