from uuid import uuid4, UUID

class Entity:
    def __init__(self, id: UUID = None):
        self.id = id or uuid4()

    def to_dict(self) -> dict:
        return {"id": str(self.id)}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=UUID(data["id"]))