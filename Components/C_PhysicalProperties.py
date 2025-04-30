from Component_Base_Type import Component

@dataclass
class PhysicalProperties(Component):
    """Physical properties of an entity."""
    weight: float
    stackable: bool
    max_stack_size: int
    is_tangible: bool
    state_of_matter: str  # e.g., solid, liquid, gas
    density: float
    volume: float
    is_fragile: bool
    is_flammable: bool
    is_conductive: bool
    is_magnetic: bool
    is_radiative: bool
    hardness: float
    melting_point: float
    boiling_point: float
    thermal_conductivity: float
    color: str
    texture: str
    odor: str
    taste: str
    is_biodegradable: bool
    acidity: float
    
    

