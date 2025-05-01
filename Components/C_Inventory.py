from dataclasses import dataclass
from typing import Dict, Any
from Components.C_Base_Type import Component

@dataclass
class Inventory(Component):
    inventory: Dict[str, Any]
