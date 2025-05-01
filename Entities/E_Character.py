import uuid
from Entities.E_Base_Entity import Entity

class Character(Entity):
    def __init__(self):
        self.id = uuid.uuid4()
        

