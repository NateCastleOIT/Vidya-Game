from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

from Utils import generate_directory_inits

from Enums import EquipmentSlot

from Systems import (AdminView,
                    EntityRegistry, 
                    ComponentRegistry, 
                    EntityBuilder, 
                    load_all_components,
                    LLMController,
                    entity_to_dict,
)

# Need this to reference component types in the EntityBuilder
from Components import (
    IsPlayer, Name, CoreStats, Inventory, EquipmentSlots, GainsExperience, Moves, Actions, Attributes, StatusEffects, PhysicalProperties, MagicalProperties
)

def generate_inits():
    # Load all entities, components, systems
    generate_directory_inits()
    

if __name__ == "__main__":
    # Initialize game
    generate_inits()

    app = QApplication(sys.argv)

    llmcontroller = LLMController()
    entity_registry = EntityRegistry()
    component_registry = ComponentRegistry()
    entity_builder = EntityBuilder(component_registry, entity_registry)
    load_all_components()

    # Create a character entity
    character = (
        entity_builder
        .with_component(IsPlayer, is_player=True)
        .with_component(Name, name="Arkyn")
        .with_component(CoreStats, STNG=5, VIGR=5, ENDR=5, DEXT=5, WILL=5, INTL=5, CHAR=5, MANA=5, ANAM=5, LUCK=5)
        .with_component(Inventory, inventory=[])
        .with_component(EquipmentSlots, slots={
                                            EquipmentSlot.HEAD: None,
                                            EquipmentSlot.NECK: None,
                                            EquipmentSlot.CHEST: None,
                                            EquipmentSlot.BACK: None,
                                            EquipmentSlot.ARM: [None] * 2,
                                            EquipmentSlot.WAIST: None,
                                            EquipmentSlot.LEG: None,
                                            EquipmentSlot.HAND: None,
                                            EquipmentSlot.HAND: None,
                                            EquipmentSlot.FOOT: [None] * 2,
                                            EquipmentSlot.MAIN_HAND: None,
                                            EquipmentSlot.OFF_HAND: None,
                                            EquipmentSlot.FINGER: [None] * 10,
                                        })
        .with_component(GainsExperience, level=1, experience=0)
        .with_component(Moves, moves = {"Fireball": 1, "Ice Spike": 1})
        .with_component(Actions)
        .with_component(Attributes)
        .with_component(StatusEffects)
        .with_component(PhysicalProperties)
        .with_component(MagicalProperties)
        .build()
    )

    blob = (
        entity_builder
        .with_component(IsPlayer, is_player=False)
        .with_component(Name, name="blob")
        .with_component(CoreStats, STNG=5)
        .with_component(Inventory, inventory=[])
        .with_component(EquipmentSlots, slots={
                                            EquipmentSlot.HEAD: None,
                                            EquipmentSlot.MAIN_HAND: None,
                                            EquipmentSlot.OFF_HAND: None,

                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                            EquipmentSlot.FINGER: None,
                                        })
        .with_component(GainsExperience, level=1, experience=0)
        .with_component(Moves, moves = {"Fireball": 1, "Ice Spike": 1})
        .with_component(Actions)
        .with_component(Attributes)
        .with_component(StatusEffects)
        .with_component(PhysicalProperties)
        .build()
    )

    dict_of_entity = entity_to_dict(character, component_registry)
    
    # rebuild the entity from the dict
    entity_id = entity_builder.build_entity_from_dict(dict_of_entity)

    # Create a HUD instance
    admin_view = AdminView(component_registry, entity_registry)
    admin_view.show()

    sys.exit(app.exec_())