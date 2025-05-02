import importlib
import inspect
import os
from pathlib import Path

from Components.C_Base_Type import Component

component_registry = {} # Maps component classes to their instances
component_name_map = {}  # Maps component class names to their respective classes

def load_all_components(component_folder="Components"):
    base_path = Path(component_folder)
    for file in os.listdir(base_path):
        if not file.startswith("C_") or not file.endswith(".py"):
            continue

        module_name = f"{component_folder}.{file[:-3]}".replace("/", ".")  # e.g., Components.C_Name
        module = importlib.import_module(module_name)

        # Register all dataclass components that inherit from Component
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Component) and obj is not Component:
                component_registry[name] = obj
                component_name_map[obj.__name__] = obj
