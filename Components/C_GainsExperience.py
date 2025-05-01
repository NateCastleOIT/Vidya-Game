from dataclasses import dataclass
from Components.C_Base_Type import Component

@dataclass
class GainsExperience(Component):
    level: int = 1
    experience: int = 0
    experience_to_next_level: int = 100
    is_level_locked: bool = False
    level_lock: int = -1
    experience_multiplier: float = 1.0

    @property
    def profieciency_bonus(self) -> int:
        """
        Calculates the proficiency bonus based on the current level.
        
        The proficiency bonus increases every 5 levels.
        
        Returns:
            int: The proficiency bonus.
        """
        return int(self.level / 5)
    
