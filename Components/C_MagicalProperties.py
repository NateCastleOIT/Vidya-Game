from dataclasses import dataclass, field

@dataclass
class MagicalProperties:
    """"""
    # Tags for conditional effects
    conditional_effects: dict = field(default_factory=lambda: {
        "is_magical": False,
        "is_enchanted": False,
        "is_cursed": False,
        "is_haunted": False,
        "is_divine": False,
        "is_undead": False
    })

    # Magical properties
    magical_properties: dict = field(default_factory=lambda: {
        "has_mana": False,
        "mana_capacity": 0.0,
        "mana_regeneration_rate": 0.0,
        "mana_efficiency": 0.0,
        "mana_resistance": 0.0,
        "mana_conductivity": 0.0,
        "mana_absorption": 0.0,
        "mana_reflection": 0.0,
        "mana_drain": 0.0,
        "is_mana_conductive": False,
        "magic_conductivity": 0.0,
        "magic_resistance": 0.0
    })
    # Add more properties as needed