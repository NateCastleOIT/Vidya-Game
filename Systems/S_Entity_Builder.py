from Entities.E_Base_Entity import Entity

class EntityBuilder:
    def __init__(self, registry):
        self.registry = registry
        self.entity_id = Entity().id

    def with_component(self, component_cls, **kwargs):
        instance = component_cls(**kwargs)
        self.registry.add(self.entity_id, instance)
        return self

    def build(self):
        return self.entity_id