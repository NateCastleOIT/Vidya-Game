from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Attributes:
    attributes: Dict[str, str] = None
    
