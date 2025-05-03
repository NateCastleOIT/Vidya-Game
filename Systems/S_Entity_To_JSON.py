from dataclasses import fields, is_dataclass, MISSING
import json
from typing import Dict
from uuid import UUID
from Systems.S_Component_Registry import ComponentRegistry

def extract_dict_schema(instance, field):
    """Get the actual stored dict from an instance's field."""
    value = getattr(instance, field.name)
    if field.default_factory != MISSING:
        try:
            # Check if the field has a default factory and if it's a dict
            if isinstance(value, dict):
                return {k: type(v).__name__ for k, v in value.items()}
        except Exception:
            pass
    return type(value).__name__  # returns the type for schema

def extract_dict_values(instance, field):
    """Get the actual stored dict from an instance's field."""
    value = getattr(instance, field.name)
    return value  # actual stored values


#=============================================================================

# def component_class_to_schema(cls_instance):
#     if not is_dataclass(cls_instance):
#         return {}

#     result = {}
#     for field in fields(cls_instance):
#         if field.type in [dict, Dict]:
#             result[field.name] = extract_dict_schema(field)
#         else:
#             result[field.name] = field.type.__name__
#     return result

def component_class_to_schema(cls_instance):
    if not is_dataclass(cls_instance):
        return {}

    result = {}
    for field in fields(cls_instance):
        result[field.name] = extract_dict_schema(cls_instance, field)
    return result

def component_class_to_dict(cls_instance):
    if not is_dataclass(cls_instance):
        return {}

    result = {}
    for field in fields(cls_instance):
        result[field.name] = extract_dict_values(cls_instance, field)
    return result

#=============================================================================
    
def entity_to_schema(entity_id: UUID, component_registry: ComponentRegistry):
    entity_components = component_registry.get_all_components_of_entity(entity_id)
    components_dict = {}
    for component_cls, instance in entity_components.items():
        components_dict[component_cls.__name__] = component_class_to_schema(instance)

    return {
        "entity_id": str(entity_id),
        "components": components_dict
    }

def entity_to_dict(entity_id: UUID, component_registry: ComponentRegistry):

    entity_components = component_registry.get_all_components_of_entity(entity_id)

    components_dict = {}
    for component_cls, instance in entity_components.items():
        components_dict[component_cls.__name__] = component_class_to_dict(instance)

    return {
        "entity_id": str(entity_id),
        "components": components_dict
    }
