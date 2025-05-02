from dataclasses import dataclass
from Enums.equipment_slots import EquipmentSlot

@dataclass
class Equipable:
    slot_type: EquipmentSlot  # The slot this item is meant to go in
    requires_both_hands: bool = False
    weight_penalty: float = 0.0
