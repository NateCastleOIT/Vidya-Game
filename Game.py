from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

from Systems.S_Entity_Registry import EntityRegistry
from Systems.S_Entity_Builder import EntityBuilder
from Systems.S_Component_Loader import load_all_components, component_registry
from Enums.equipment_slots import EquipmentSlot
from Entities.E_Player_HUD import HUD

if __name__ == "__main__":
    app = QApplication(sys.argv)

    entity_registry = EntityRegistry()
    entity_builder = EntityBuilder(entity_registry)
    load_all_components()

    # Create a character entity
    hero = (
        entity_builder
        .with_component(
            component_registry["IsPlayer"], is_player=True)
        .with_component(
            component_registry["Name"], name="Arkyn")
        .with_component(
            component_registry["CoreStats"], 
            STNG=5, VIGR=5, ENDR=5, DEXT=5, WILL=5, INTL=5, CHAR=5, MANA=5, ANAM=5, LUCK=5)
        .with_component(
            component_registry["Inventory"], inventory=[])
        .with_component(
            component_registry["EquipmentSlots"], 
            slots={
                EquipmentSlot.HEAD: None,
                EquipmentSlot.HANDS: None,
            })
        .with_component(
            component_registry["GainsExperience"], level=1, experience=0)
        .with_component(
            component_registry["Moves"], moves = {"Fireball": 1, "Ice Spike": 1})
        .with_component(
            component_registry["Actions"])
        .with_component(
            component_registry["Attributes"])
        .with_component(
            component_registry["StatusEffects"])
        .with_component(
            component_registry["MagicalProperties"], is_magical=True, mana_capacity=0.75)
        .build()
    )

    # Create a HUD instance
    hud = HUD(entity_registry, hero)
    hud.show()

    sys.exit(app.exec_())