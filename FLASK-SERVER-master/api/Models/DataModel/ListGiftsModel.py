class ListGiftsModel:
    def __init__(self, gift_id: str, url: str, price: int, name: str, description: str):
        self.avatar_id: str = gift_id
        self.url: str = url
        self.price: int = price
        self.name: str = name
        self.description: str = description

    def serialize(self):
        return {
            'id': self.avatar_id,
            'url': self.url,
            'price': self.price,
            'name': self.name,
            'description': self.description
        }
