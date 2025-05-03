from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class StatusEffects:
    """Base class for status effects."""
    effects: Dict[str, Any] = None# Dictionary of status effects