from dataclasses import dataclass
from typing import Dict
from Components.C_Base_Type import Component

@dataclass
class Attributes(Component):
    attributes: Dict[str, bool] = None
    
