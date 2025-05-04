from dataclasses import fields, is_dataclass, MISSING
import json
from typing import Dict
from enum import Enum
from uuid import UUID
from Systems.S_Component_Registry import ComponentRegistry

def extract_comp_cls_schema(instance, field):
    value = getattr(instance, field.name)
    try:
        if field.type != MISSING and not (type(value) == dict):
            # If the field has a type annotation, use it
            value = str(field.type)
            return value.replace("typing.", "").replace("<class '", "").replace("'>", "").replace("<enum '", "Enums.")
            
        if (type(value) == dict):
            # If the field is a dictionary, convert keys to strings
            value = {str(k): (str(type(v))).replace("<class '", "").replace("'>", "").replace("<enum '", "Enums.")  for k, v in value.items()}
            return value
    except Exception:
        print(f"Error converting field {field.name} of {instance.__class__.__name__} to schema: {value}")

    value = str(type(value))
    return value.replace("<class '", "").replace("'>", "").replace("<enum '", "Enums.")  # actual stored values

def extract_dict_values(instance, field):
    """Get the actual stored dict from an instance's field."""
    value = getattr(instance, field.name)

    if isinstance(value, dict):
        flattened = {}
        for k, v in value.items():
            if isinstance(v, Enum):
                flattened[k] = v.value  # or str(v.name) if you prefer
            else:
                flattened[k] = v
        return flattened
        
    return value


#=============================================================================

def component_class_to_schema(cls_instance) -> dict:
    if not is_dataclass(cls_instance):
        return {}

    result = {}
    for field in fields(cls_instance):
        result[field.name] = extract_comp_cls_schema(cls_instance, field)
    return result

def component_class_to_dict(cls_instance) -> dict:
    if not is_dataclass(cls_instance):
        return {}

    result = {}
    for field in fields(cls_instance):
        result[field.name] = extract_dict_values(cls_instance, field)
    return result

#=============================================================================
    
def entity_to_schema(entity_id: UUID, component_registry: ComponentRegistry) -> dict:
    entity_components = component_registry.get_all_components_of_entity(entity_id)
    components_dict = {}
    for component_cls, instance in entity_components.items():
        components_dict[component_cls.__name__] = component_class_to_schema(instance)

    return {
        "entity_id": str(type(entity_id)),
        "components": components_dict
    }

def entity_to_dict(entity_id: UUID, component_registry: ComponentRegistry) -> dict:

    entity_components = component_registry.get_all_components_of_entity(entity_id)

    components_dict = {}
    for component_cls, instance in entity_components.items():
        components_dict[component_cls.__name__] = component_class_to_dict(instance)

    return {
        "entity_id": str(entity_id),
        "components": components_dict
    }

def convert_keys_to_str(obj):
    if isinstance(obj, dict):
        return {str(k): convert_keys_to_str(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_keys_to_str(i) for i in obj]
    elif hasattr(obj, '__dict__'):
        return convert_keys_to_str(vars(obj))
    else:
        return obj
