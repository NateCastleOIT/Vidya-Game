from dataclasses import dataclass

@dataclass
class CoreStats:
    STNG: int = 5
    VIGR: int = 5
    ENDR: int = 5
    DEXT: int = 5
    WILL: int = 5
    INTL: int = 5
    CHAR: int = 5
    MANA: int = 5
    ANAM: int = 5
    LUCK: int = 5
    available_points: int = 0
    armor_rating: int = 0
    
    @property
    def initiative(self) -> int:
        """
        Calculates the initiative based on the Dexterity and Luck attributes.
        
        Returns:
            int: The initiative value.
        """
        return self.ANAM

    @property
    def health_points(self) -> int:
        """
        Calculates the health points based on the Vigor attribute.
        
        Returns:
            int: The health points value.
        """
        return self.VIGR * 5

    @property
    def mana_points(self) -> int:
        """
        Calculates the mana points based on the Mana attribute.
        
        Returns:
            int: The mana points value.
        """
        return self.MANA * 5

    @property
    def action_points(self) -> int:
        """
        Calculates the action points based on the Vigor attribute.
        
        Returns:
            int: The action points value.
        """
        return self.VIGR

    @property
    def physical_defense(self) -> int:
        """
        Calculates the physical defense based on the Strength and Endurance attributes.
        
        Returns:
            int: The physical defense value.
        """
        return 40 + self.ENDR + self.armor_rating

    @property
    def mental_defense(self) -> int:
        """
        Calculates the mental defense based on the Will attribute.
        
        Returns:
            int: The mental defense value.
        """
        return 40 + self.WILL + self.proficiency_bonus

    @property
    def skills(self):
        """
        Returns a dictionary of skills and their corresponding attributes.
        
        Returns:
            dict: A dictionary where the keys are the skill names and the values are the attribute associated with each skill.
        """
        return {
            "acrobatics":       self.DEXT,
            "animal_handling":  self.STNG,
            "athletics":        self.CHAR,
            "bartering":        self.CHAR,
            "bluffing":         self.CHAR,
            "climbing":         self.STNG,
            "cooking":          self.DEXT,
            "divination":       self.ANAM,
            "disguise":         self.DEXT,
            "dual_wielding":    self.DEXT,
            "healing":          self.WILL,
            "history":          self.INTL,
            "hunting":          self.ANAM,
            "farming":          self.STNG,
            "intimidation":     self.CHAR,
            "investigation":    self.INTL,
            "insight":          self.INTL,
            "evasion":          self.DEXT,
            "martial_arts":     self.DEXT,
            "martial_attack":   self.STNG,
            "magic":            self.WILL,
            "magic_attack":     self.WILL,
            "mining":           self.STNG,
            "leadership":       self.CHAR,
            "persuasion":       self.CHAR,
            "finesse":          self.DEXT,
            "stealth":          self.DEXT,
            "survival":         self.ANAM,
            "sharpshooter":     self.ANAM,
            "swimming":         self.ENDR,
            "two-handed":       self.STNG,
        }

