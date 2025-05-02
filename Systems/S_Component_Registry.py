class ComponentRegistry:
    def __init__(self):
        self.registry = {}  # {ComponentClass.__name__: {uuid: instance}}

    def register(self, component_cls):
        if component_cls not in self.registry:
            self.registry[component_cls] = {}

    def add(self, entity_id, component_instance):
        component_cls = type(component_instance)
        if component_cls not in self.registry:
            self.register(component_cls)
        self.registry[component_cls][entity_id] = component_instance

    def get(self, component_cls):
        return self.registry.get(component_cls, {})

    def get_component_of_entity(self, component_cls, entity_id):
        return self.get(component_cls).get(entity_id)

    def get_all_components_of_entity(self, entity_id):
        return {
            comp_cls: comps[entity_id]
            for comp_cls, comps in self.registry.items()
            if entity_id in comps
        }

    def entities_with_component(self, component_cls):
        return list(self.get(component_cls).keys())