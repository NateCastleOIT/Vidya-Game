import inspect
import Components  # the package
from dataclasses import is_dataclass
from Systems.S_Entity_To_JSON import component_class_to_schema

schema = {}

def add_component(component_cls, instance):
    if component_cls not in schema:
        schema[component_cls] = {}
    schema[component_cls] = component_class_to_schema(instance)


def all_components_to_schema(c_registry):
    """Convert all components in the registry to schema."""


    component_classes = {}

    for name, cls in inspect.getmembers(Components, inspect.isclass):
        # Filter to include only those classes defined in the Components module
        if cls.__module__.startswith("Components"):
            if is_dataclass(cls):
                component_classes[name] = cls()


    for component_cls, instance in component_classes.items():
        add_component(component_cls, instance)
        c_registry.add_to_all(instance)
    return schema