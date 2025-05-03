from dataclasses import dataclass
from typing import Dict
from uuid import UUID
from Enums.equipment_slots import EquipmentSlot

@dataclass
class EquipmentSlots:
    # The list of equipment slots for the entity (uuid)
    slots: Dict[EquipmentSlot, UUID]