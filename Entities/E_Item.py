import uuid

class Item(Entity):
    def __init__(self):
        self.id = uuid.uuid4()