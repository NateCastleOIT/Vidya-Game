from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Inventory:
    inventory: Dict[str, Any]
