class EntityRegistry:
    def __init__(self):
        self.registry = []  # {EntityClass.__name__: {uuid: instance}}

    def register(self, entity_id):
        if entity_id not in self.registry:
            self.registry.append(entity_id)

    def get(self, entity_id):
        return self.registry.get(entity_id, [])