class ListGiftsModel:
    def __init__(self, gift_id, url, price, name, description):
        self.avatar_id = gift_id
        self.url = url
        self.price = price
        self.name = name
        self.description = description

    def serialize(self):
        return {
            'id': self.avatar_id,
            'url': self.url,
            'price': self.price,
            'name': self.name,
            'description': self.description
        }
