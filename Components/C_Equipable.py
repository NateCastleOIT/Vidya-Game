from dataclasses import dataclass
from Components.C_Base_Type import Component
from Enums.equipment_slots import EquipmentSlot

@dataclass
class Equipable(Component):
    slot_type: EquipmentSlot  # The slot this item is meant to go in
    requires_both_hands: bool = False
    weight_penalty: float = 0.0
