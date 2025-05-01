from Systems.S_Base_System import System

class EntityBuilder(System):
    def __init__(self, registry):
        self.registry = registry
        self.entity = registry.create_entity()

    def with_component(self, component_cls, **kwargs):
        component = component_cls(**kwargs)
        self.registry.add_component(self.entity, component)
        return self

    def with_instance(self, component_instance):
        self.registry.add_component(self.entity, component_instance)
        return self

    def build(self):
        return self.entity

"""EXAMPLE:

builder = EntityBuilder(registry)

player_id = (
    builder
    .with_component(Name, display_name="Arkyn")
    .with_component(CoreStats, STNG=6, DEXT=5, CHAR=8)
    .with_component(Inventory, items=[])
    .with_component(EquipmentSlots, slots={
        EquipmentSlotsEnum.HEAD: None,
        EquipmentSlotsEnum.WEAPON: None,
    })
    .with_component(MagicalProperties, is_magical=True, mana_capacity=0.75)
    .build()
)
"""