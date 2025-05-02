from dataclasses import dataclass

@dataclass
class Name:
    """Name of the component."""

    # General
    name: str = "Unnamed"