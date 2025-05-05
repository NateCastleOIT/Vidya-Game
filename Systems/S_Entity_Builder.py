from Entities.E_BaseEntity import Entity
from pathlib import Path
import os
import json

class EntityBuilder:
    def __init__(self, c_registry, e_registry):
        self.c_registry = c_registry
        self.e_registry = e_registry
        self.components = []

    def build_entity_from_dict(self, entity_dict):
        entity = Entity()
        entity_id = entity.id

        entity_dict = {
            "entity_id": str(entity_id),
            "components": entity_dict
        }

        # Register the entity
        self.e_registry.register(entity_id)

        # Register all components from the dictionary
        for comp_cls_name, comp_kwargs in entity_dict["components"].items():
            comp_cls = self.c_registry.get_component_class_by_name(comp_cls_name)
            instance = comp_cls(**comp_kwargs)
            self.c_registry.add(entity_id, instance)

        return entity_id

    def with_component(self, component_cls, **kwargs):
        instance = component_cls(**kwargs)
        self.components.append((component_cls, instance))
        return self

    def build(self):
        entity = Entity()
        entity_id = entity.id

        # Register the entity
        self.e_registry.register(entity_id)

        # Register all components
        for comp_cls, instance in self.components:
            self.c_registry.add(entity_id, instance)

        # Clear builder state (optional, in case reused)
        self.components.clear()

        return entity.id


    def build_entities_from_folder(self, folder_path, entity_names=[]) -> dict:

        gen_entity_folder = Path.cwd() / folder_path

        entities = {}
        
        stored_entities = entity_names if entity_names else os.listdir(gen_entity_folder)

        for generated_entity in stored_entities:   
            if generated_entity.endswith(".json"):
                try:

                    with open(folder_path + "/" + generated_entity, "r", encoding="utf-8") as file:
                        entity_data = json.load(file)
                
                    entity_data = self.build_entity_from_dict(entity_data)
                    entities[generated_entity] = entity_data
                except Exception as e:
                    print(f"Error loading {generated_entity}: {e}")

        return entities