class ListAvatarsModel:
    def __init__(self, avatar_id: str, url: str, price:int, name: str):
        self.avatar_id: str = avatar_id
        self.url: str = url
        self.price: int = price
        self.name: str = name

    def serialize(self):
        return {
            'id': self.avatar_id,
            'url': self.url,
            'price': self.price,
            'name': self.name
        }
