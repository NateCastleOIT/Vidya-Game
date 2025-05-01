from dataclasses import dataclass
from typing import Dict
from Components.C_Base_Type import Component

@dataclass
class Actions(Component):
    actions: Dict[str, bool] = None
    
