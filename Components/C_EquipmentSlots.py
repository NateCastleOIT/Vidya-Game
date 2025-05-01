from dataclasses import dataclass
from typing import Dict
from uuid import UUID
from Components.C_Base_Type import Component
from Enums.equipment_slots import EquipmentSlot

@dataclass
class EquipmentSlots(Component):
    """
    This class represents the equipment slots of an entity.
    It is a component that can be added to an entity to define its equipment slots.
    """

    # The list of equipment slots for the entity (uuid)
    slots: Dict[EquipmentSlot, UUID]