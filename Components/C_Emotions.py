from dataclasses import dataclass
from typing import Dict

@dataclass
class Emotions:
    happy_sad: float = 0.9
    enjoyment_disgust: float = 0.5
    love_hate: float = 0.5
    comfort_fear: float = 0.5
    pride_shame: float = 0.5
    trauma_events: Dict[str, float] = None

    @property
    def trauma(self) -> float:
        """
        Calculates the initiative based on the Dexterity and Luck attributes.
        
        Returns:
            int: The initiative value.
        """
        return self.happy + self.sad

    