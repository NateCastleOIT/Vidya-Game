from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

from Utils.generate_components_init import generate_component_init

from Systems import ComponentRegistry
from Systems import EntityBuilder
from Systems import load_all_components
from Enums import EquipmentSlot
from Entities.E_Player_HUD import HUD

# Need this to reference component types in the EntityBuilder
from Components import (
    IsPlayer, Name, CoreStats, Inventory, EquipmentSlots, GainsExperience, Moves, Actions, Attributes, StatusEffects, PhysicalProperties, MagicalProperties
)

def generate_comp_init():
    # Load all components
    generate_component_init()
    

if __name__ == "__main__":
    # Initialize game
    generate_comp_init()


    app = QApplication(sys.argv)

    component_registry = ComponentRegistry()
    entity_builder = EntityBuilder(component_registry)
    load_all_components()

    # Create a character entity
    hero = (
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
                                            EquipmentSlot.ARM: None,
                                            EquipmentSlot.ARM: None,
                                            EquipmentSlot.WAIST: None,
                                            EquipmentSlot.LEGS: None,
                                            EquipmentSlot.HAND: None,
                                            EquipmentSlot.HAND: None,
                                            EquipmentSlot.FOOT: None,
                                            EquipmentSlot.FOOT: None,
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
        .with_component(MagicalProperties)
        .build()
    )

    # Create a HUD instance
    hud = HUD(component_registry, hero)
    hud.show()

    sys.exit(app.exec_())