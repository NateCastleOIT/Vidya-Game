from dataclasses import fields, is_dataclass, MISSING
import json
from typing import Dict
from uuid import UUID
from Systems.S_Component_Registry import ComponentRegistry


def extract_dict_schema(field):
    """Try to infer the contents of a dict from its default_factory."""
    if field.default_factory != MISSING:
        try:
            value = field.default_factory()
            if isinstance(value, dict):
                return {k: type(v).__name__ for k, v in value.items()}
        except Exception:
            pass
    return "dict"

def component_class_to_dict(cls):
    if not is_dataclass(cls):
        return {}

    result = {}
    for field in fields(cls):
        if field.type in [dict, Dict]:
            result[field.name] = extract_dict_schema(field)
        else:
            result[field.name] = field.type.__name__
    return result
    
def entity_to_dict(entity_id: UUID, component_registry: ComponentRegistry):
    entity_components = component_registry.get_all_components_of_entity(entity_id)
    components_dict = {}
    for component_cls in entity_components:
        components_dict[component_cls.__name__] = component_class_to_dict(component_cls)

    return components_dict
