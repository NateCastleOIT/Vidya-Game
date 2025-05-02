from dataclasses import dataclass, field
from Enums.states_of_matter import StateOfMatter

@dataclass
class PhysicalProperties:
    """Normalized physical and sensory properties (0.0 to 1.0 where applicable)."""

    # General & Material
    general_properties: dict = field(default_factory=lambda: {
        "weight": 10.0,
        "volume": 1.0,
        "density": 0.5,
        "is_stackable": False,
        "max_stack_size": 1,
        "is_tangible": True,
        "state_of_matter": "solid"  # solid, liquid, gas
    })

    # Structural / Mechanical
    structural_properties: dict = field(default_factory=lambda: {
        "hardness": 0.5,
        "toughness": 0.5,
        "brittleness": 0.5,
        "elasticity": 0.5,
        "ductility": 0.5,
        "malleability": 0.5,
        "tensile_strength": 0.5,
        "compressive_strength": 0.5,
        "shear_strength": 0.5,
        "impact_resistance": 0.5,
        "friction_coefficient": 0.5,
        "is_fragile": False
    })

    # Thermal
    thermal_properties: dict = field(default_factory=lambda: {
        "melting_point": 0.5,
        "boiling_point": 0.5,
        "thermal_conductivity": 0.5,
        "specific_heat_capacity": 0.5,
        "flash_point": 0.5,
        "thermal_expansion": 0.5,
        "is_flammable": False
    })

    # Chemical
    chemical_properties: dict = field(default_factory=lambda: {
        "acidity": 0.5,
        "permeability": 0.5,
        "porosity": 0.5,
        "is_biodegradable": False
    })

    # Electromagnetic
    electromagnetic_properties: dict = field(default_factory=lambda: {
        "is_conductive": False,
        "is_magnetic": False,
        "is_radiative": False,
        "reflectivity": 0.5,
        "transparency": 0.0,
        "luminosity": 0.0
    })

    # Sensory
    sensory_properties: dict = field(default_factory=lambda: {
        "color": "gray",
        "texture": "smooth",
        "odor": "none",
        "taste": "none"
    })
