from dataclasses import dataclass
from typing import Dict


@dataclass
class Actions:
    actions: Dict[str, bool] = None
    
