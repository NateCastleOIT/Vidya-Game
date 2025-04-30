from Component_Baste_Type import Component

@dataclass
class StatusEffects(Component):
    """Base class for status effects."""
    effects: Dict[str, Any]  # Dictionary of status effects