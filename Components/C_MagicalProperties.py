from dataclasses import dataclass
from Components.C_Base_Type import Component

@dataclass
class MagicalProperties(Component):
    """"""
    # Tags for conditional effects
    is_magical: bool = False
    is_enchanted: bool = False
    is_cursed: bool = False
    is_haunted: bool = False
    is_divine: bool = False
    is_undead: bool = False

    has_mana: bool = False
    mana_capacity: float = 0.0
    mana_regeneration_rate: float = 0.0
    mana_efficiency: float = 0.0
    mana_resistance: float = 0.0
    mana_conductivity: float = 0.0
    mana_absorption: float = 0.0
    mana_reflection: float = 0.0
    mana_drain: float = 0.0

    is_mana_conductive: bool = False
    magic_conductivity: float = 0.0
    magic_resistance: float = 0.0

    # Add more properties as needed