from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Actions:
    # actions: dict = field(default_factory=lambda: {
    #     "Attack": "Attack",
    # })
    # actions: Dict[str, str] = field(default_factory=dict)
    actions: Dict[str, str] = None
    
