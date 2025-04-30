from dataclasses import dataclass
from typing import Dict, Any
from uuid import uuid4, UUID

# Base component type
class Component:
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)