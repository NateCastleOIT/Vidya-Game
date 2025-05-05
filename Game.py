from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys
import asyncio
import json
import os
from pathlib import Path

from Utils import generate_directory_inits

from Enums import EquipmentSlot

from Systems import (AdminView,     # Systems.S_AdminView.AdminView
                    EntityRegistry, 
                    ComponentRegistry, 
                    EntityBuilder, 
                    load_all_components,
                    LLMController,
                    entity_to_dict,
                    entity_to_schema,
                    convert_keys_to_str,
                    all_components_to_schema,
                    GameMaster,
)

# Need this to reference component types in the EntityBuilder
from Components import (
    IsPlayer, Name, CoreStats, Inventory, EquipmentSlots, GainsExperience, Moves, Actions, Attributes, StatusEffects, PhysicalProperties, MagicalProperties, Movement
)

def generate_inits():
    # Load all entities, components, systems
    generate_directory_inits()

async def main() -> None:
    # Initialize game
    generate_inits()

    app = QApplication(sys.argv)

    llmcontroller = LLMController()
    entity_registry = EntityRegistry()
    component_registry = ComponentRegistry()
    entity_builder = EntityBuilder(component_registry, entity_registry)
    load_all_components()
    all_components_schema = all_components_to_schema(component_registry)
    with open("temp_all_components_schema.JSON", "w") as file:
        json_ready = convert_keys_to_str(all_components_schema)
        json.dump(json_ready, file, indent=2)

    # Create a character entity
    # character = (
    #     entity_builder
    #     .with_component(IsPlayer, is_player=True)
    #     .with_component(Name, name="Arkyn")
    #     .with_component(CoreStats, STNG=5, VIGR=5, ENDR=5, DEXT=5, WILL=5, INTL=5, CHAR=5, MANA=5, ANAM=5, LUCK=5)
    #     .with_component(Inventory, inventory=[])
    #     .with_component(EquipmentSlots, slots={
    #                                         EquipmentSlot.HEAD: None,
    #                                         EquipmentSlot.NECK: None,
    #                                         EquipmentSlot.CHEST: None,
    #                                         EquipmentSlot.BACK: None,
    #                                         EquipmentSlot.ARM: [None] * 2,
    #                                         EquipmentSlot.WAIST: None,
    #                                         EquipmentSlot.LEG: None,
    #                                         EquipmentSlot.HAND: None,
    #                                         EquipmentSlot.HAND: None,
    #                                         EquipmentSlot.FOOT: [None] * 2,
    #                                         EquipmentSlot.MAIN_HAND: None,
    #                                         EquipmentSlot.OFF_HAND: None,
    #                                         EquipmentSlot.FINGER: [None] * 10,
    #                                     })
    #     .with_component(GainsExperience, level=1, experience=0)
    #     .with_component(Moves, moves = {"Fireball": 1, "Ice Spike": 1})
    #     .with_component(Actions)
    #     .with_component(Attributes)
    #     .with_component(StatusEffects)
    #     .with_component(PhysicalProperties)
    #     .with_component(MagicalProperties)
    #     .with_component(Movement, speed=69.0)
    #     .build()
    # )

    # blob = (
    #     entity_builder
    #     .with_component(IsPlayer, is_player=False)
    #     .with_component(Name, name="blob")
    #     .with_component(CoreStats, STNG=5)
    #     .with_component(Inventory, inventory=[])
    #     .with_component(EquipmentSlots, slots={
    #                                         EquipmentSlot.HEAD: None,
    #                                         EquipmentSlot.MAIN_HAND: None,
    #                                         EquipmentSlot.OFF_HAND: None,

    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                         EquipmentSlot.FINGER: None,
    #                                     })
    #     .with_component(GainsExperience, level=1, experience=0)
    #     .with_component(Moves, moves={"Fireball": 1, "Ice Spike": 1})
    #     .with_component(Actions)
    #     .with_component(Attributes)
    #     .with_component(StatusEffects)
    #     .with_component(PhysicalProperties)
    #     .build()
    # )

    # dict_of_entity = entity_to_dict(character, component_registry)

    # with open("temp_entity_json.JSON", "w") as file:
    #     json_ready = convert_keys_to_str(dict_of_entity)
    #     json.dump(json_ready, file, indent=2)

    # schema_of_entity = entity_to_schema(character, component_registry)

    # with open("temp_entity_schema.JSON", "w") as file:
    #     json_ready = convert_keys_to_str(schema_of_entity)
    #     json.dump(json_ready, file, indent=2)
    
    # rebuild the entity from the dict
    #entity_id = entity_builder.build_entity_from_dict(dict_of_entity)
    # entity_id = entity_builder.build_entity_from_dict(schema_of_entity) # returns a dict with types, not values for generating GPT Schema

    # gamemaster = GameMaster()
    # result = gamemaster.run_game_master()
    # print("\n\n\n" + result)
    

    stored_entities = entity_builder.build_entities_from_folder(
        "Generated Entities", 
        entity_names=["Lord.json"],
        )

    # Create a HUD instance
    admin_view = AdminView(component_registry, entity_registry)
    admin_view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
   asyncio.run(main())