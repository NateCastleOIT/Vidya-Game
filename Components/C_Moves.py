from dataclasses import dataclass
from typing import Dict
from Components.C_Base_Type import Component

@dataclass
class Moves(Component):
    moves: Dict[str, bool] = None
    
