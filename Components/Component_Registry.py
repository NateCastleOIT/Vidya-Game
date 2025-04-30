class ComponentRegistry:
    def __init__(self):
        self._components = {}  # Dict[UUID, Dict[type, Component]]

    def add_component(self, entity: ItemEntity, component):
        self._components.setdefault(entity.id, {})[type(component)] = component

    def get_component(self, entity: ItemEntity, component_type: type):
        return self._components.get(entity.id, {}).get(component_type)
