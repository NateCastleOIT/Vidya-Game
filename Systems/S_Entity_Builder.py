from Entities.E_Base_Entity import Entity

class EntityBuilder:
    def __init__(self, c_registry, e_registry):
        self.c_registry = c_registry
        self.e_registry = e_registry
        self.components = []

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

        return entity_id