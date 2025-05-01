from dataclasses import dataclass
from typing import Dict, Any
from Components.C_Base_Type import Component

@dataclass
class StatusEffects(Component):
    """Base class for status effects."""
    effects: Dict[str, Any] = None# Dictionary of status effects