from dataclasses import dataclass
from Components.C_Base_Type import Component
from Enums.states_of_matter import StateOfMatter

@dataclass
class PhysicalProperties(Component):
    """Normalized physical and sensory properties (0.0 to 1.0 where applicable)."""

    # General & Material
    weight: float = 10.0
    volume: float = 1.0
    density: float = 0.5
    is_stackable: bool = False
    max_stack_size: int = 1
    is_tangible: bool = True
    state_of_matter: str = "solid"  # solid, liquid, gas

    # Structural / Mechanical
    hardness: float = 0.5
    toughness: float = 0.5
    brittleness: float = 0.5
    elasticity: float = 0.5
    ductility: float = 0.5
    malleability: float = 0.5
    tensile_strength: float = 0.5
    compressive_strength: float = 0.5
    shear_strength: float = 0.5
    impact_resistance: float = 0.5
    friction_coefficient: float = 0.5
    is_fragile: bool = False

    # Thermal
    melting_point: float = 0.5
    boiling_point: float = 0.5
    thermal_conductivity: float = 0.5
    specific_heat_capacity: float = 0.5
    flash_point: float = 0.5
    thermal_expansion: float = 0.5
    is_flammable: bool = False

    # Chemical
    acidity: float = 0.5
    permeability: float = 0.5
    porosity: float = 0.5
    is_biodegradable: bool = False

    # Electromagnetic
    is_conductive: bool = False
    is_magnetic: bool = False
    is_radiative: bool = False
    reflectivity: float = 0.5
    transparency: float = 0.0
    luminosity: float = 0.0

    # Sensory
    color: str = "gray"
    texture: str = "smooth"
    odor: str = "none"
    taste: str = "none"
