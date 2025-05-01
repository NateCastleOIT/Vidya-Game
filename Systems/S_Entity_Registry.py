import uuid
from collections import defaultdict
from Systems.S_Base_System import System

class EntityRegistry(System):
    def __init__(self):
        self.entities = set()  # Set of all entity IDs
        self.components = defaultdict(dict)  # {ComponentClass: {entity_id: component_instance}}

    def create_entity(self) -> uuid.UUID:
        entity_id = uuid.uuid4()
        self.entities.add(entity_id)
        return entity_id

    def delete_entity(self, entity_id: uuid.UUID):
        if entity_id in self.entities:
            self.entities.remove(entity_id)
            for comp_dict in self.components.values():
                comp_dict.pop(entity_id, None)

    def add_component(self, entity_id: uuid.UUID, component):
        comp_type = type(component)
        self.components[comp_type][entity_id] = component

    def get_component(self, entity_id: uuid.UUID, component_cls):
        return self.components.get(component_cls, {}).get(entity_id)

    def has_component(self, entity_id: uuid.UUID, component_cls) -> bool:
        return entity_id in self.components.get(component_cls, {})

    def remove_component(self, entity_id: uuid.UUID, component_cls):
        if entity_id in self.components.get(component_cls, {}):
            del self.components[component_cls][entity_id]

    def get_all_components(self, entity_id: uuid.UUID) -> dict:
        components = {
            comp_type.__name__: comps[entity_id].__dict__
            for comp_type, comps in self.components.items()
            if entity_id in comps
        }

        return components

    def get_entities_with_component(self, component_cls):
        return list(self.components.get(component_cls, {}).keys())

