from Entities.E_BaseEntity import Entity

class EntityBuilder:
    def __init__(self, c_registry, e_registry):
        self.c_registry = c_registry
        self.e_registry = e_registry
        self.components = []

    def build_entity_from_dict(self, entity_dict):
        entity = Entity()
        entity_id = entity.id

        # Register the entity
        self.e_registry.register(entity_id)

        # Register all components from the dictionary
        for comp_cls_name, comp_kwargs in entity_dict.items():
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