from dataclasses import dataclass
from Components.C_Base_Type import Component

@dataclass
class IsPlayer(Component):
    is_player: bool = True
    