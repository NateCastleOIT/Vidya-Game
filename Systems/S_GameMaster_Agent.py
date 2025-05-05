from pydantic import BaseModel
from dotenv import load_dotenv
import os
from agents import Agent, Runner

all_components_schema = {
        "Actions": {
            "actions": "Dict[str, str]"
        },
        "Attributes": {
            "attributes": "Dict[str, str]"
        },
        "CoreStats": {
            "STNG": "int",
            "VIGR": "int",
            "ENDR": "int",
            "DEXT": "int",
            "WILL": "int",
            "INTL": "int",
            "CHAR": "int",
            "MANA": "int",
            "ANAM": "int",
            "LUCK": "int",
            "available_points": "int",
            "armor_rating": "int"
        },
        "Description": {
            "description": "str"
        },
        "Emotions": {
            "happy_sad": "float",
            "enjoyment_disgust": "float",
            "love_hate": "float",
            "comfort_fear": "float",
            "pride_shame": "float",
            "trauma_events": "Dict[str, str]"
        },
        "EquipmentSlots": {
            "slots": "Dict[Enums.equipment_slots.EquipmentSlot, uuid.UUID]"
        },
        "GainsExperience": {
            "level": "int",
            "experience": "int",
            "experience_to_next_level": "int",
            "is_level_locked": "bool",
            "level_lock": "int",
            "experience_multiplier": "float"
        },
        "Inventory": {
            "inventory": "Dict[str, Any]"
        },
        "IsEquipable": {
            "slot_type": "Enums.EquipmentSlot",
            "requires_both_hands": "bool",
            "weight_penalty": "float"
        },
        "IsPlayer": {
            "is_player": "bool"
        },
        "MagicalProperties": {
            "conditional_effects": {
            "is_magical": "bool",
            "is_enchanted": "bool",
            "is_cursed": "bool",
            "is_haunted": "bool",
            "is_divine": "bool",
            "is_undead": "bool"
            },
            "magical_properties": {
            "has_mana": "bool",
            "mana_capacity": "float",
            "mana_regeneration_rate": "float",
            "mana_efficiency": "float",
            "mana_resistance": "float",
            "mana_conductivity": "float",
            "mana_absorption": "float",
            "mana_reflection": "float",
            "mana_drain": "float",
            "is_mana_conductive": "bool",
            "magic_conductivity": "float",
            "magic_resistance": "float"
            }
        },
        "Movement": {
            "speed": "int"
        },
        "Moves": {
            "moves": "Dict[str, bool]"
        },
        "Name": {
            "name": "str"
        },
        "PhysicalProperties": {
            "general_properties": {
            "weight": "float",
            "volume": "float",
            "density": "float",
            "is_stackable": "bool",
            "max_stack_size": "int",
            "is_tangible": "bool",
            "state_of_matter": "Enums.StateOfMatter"
            },
            "structural_properties": {
            "hardness": "float",
            "toughness": "float",
            "brittleness": "float",
            "elasticity": "float",
            "ductility": "float",
            "malleability": "float",
            "tensile_strength": "float",
            "compressive_strength": "float",
            "shear_strength": "float",
            "impact_resistance": "float",
            "friction_coefficient": "float",
            "is_fragile": "bool"
            },
            "thermal_properties": {
            "melting_point": "float",
            "boiling_point": "float",
            "thermal_conductivity": "float",
            "specific_heat_capacity": "float",
            "flash_point": "float",
            "thermal_expansion": "float",
            "is_flammable": "bool"
            },
            "chemical_properties": {
            "acidity": "float",
            "permeability": "float",
            "porosity": "float",
            "is_biodegradable": "bool"
            },
            "electromagnetic_properties": {
            "is_conductive": "bool",
            "is_magnetic": "bool",
            "is_radiative": "bool",
            "reflectivity": "float",
            "transparency": "float",
            "luminosity": "float"
            },
            "sensory_properties": {
            "color": "str",
            "texture": "str",
            "odor": "str",
            "taste": "str"
            }
        },
        "StatusEffects": {
            "effects": "Dict[str, Any]"
        }
    }

PROMPT = (
    f"""You are a game master for a tabletop role-playing game. Your job is to create a fun and engaging story for a player to play in.
    You will be shown the schema in which you can develop in game entities via defining their components.
    Here are the components available to you and their schemas:
    {all_components_schema}
    You can use any number of these components to build a single entity, you are not obligated to use all of them but you should do your best to determine the appropriate components to use.
    You will generate your output in a provided format.

    """)

class EntityBuild(BaseModel):
    story: str
    "Any story information that you want to provide to the player."

    entities: dict = {
        "entities": [
            {
                "entity_id": str,
                "components": dict
            }
        ]
    }
    "A dictionary of entities to be built. Each entity should have a unique ID and a dictionary of components."

class GameMaster():
    def __init__(self):
        self.game_master_agent = Agent(
            name="GameMaster",
            instructions=PROMPT,
            model="gpt-4.1",
            output_type=EntityBuild,
        )

        load_dotenv()

        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise EnvironmentError("OPENAI_API_KEY not found in environment.")

        self.history = []

    def add_response_to_history(self, response):
        self.history += [{"role": el.role, "content": el.content} for el in response.output]

    async def run_game_master(self):
        result = await Runner.run(
            self.game_master_agent,
            #self.api_key,
            prompt=PROMPT,
        )
        self.add_response_to_history(result)
        return result
        
    