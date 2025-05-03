import uuid

class Character:
    def __init__(self,
        is_player=False,
        name="Steve", 
        base_stats={
            "STNG": 5,
            "VIGR": 5,
            "ENDR": 5,
            "DEXT": 5,
            "WILL": 5,
            "INTL": 5,
            "CHAR": 5,
            "MANA": 5,
            "ANAM": 5,
            "LUCK": 5,
        }
        ):


        self.id = uuid.uuid4()

        self.is_player = is_player

        self.name = name

        self.base_stats = base_stats
        self.available_points = 0

        if is_player:
            self.base_stats, self.available_points = Calculate_Stats(self.base_stats, available_points=self.available_points)
        
        self.skills = {
            "acrobatics":       self.base_stats["DEXT"],
            "animal_handling":  self.base_stats["STNG"],
            "athletics":        self.base_stats["CHAR"],
            "bartering":        self.base_stats["CHAR"],
            "bluffing":         self.base_stats["CHAR"],
            "climbing":         self.base_stats["STNG"],
            "cooking":          self.base_stats["DEXT"],
            "divination":       self.base_stats["ANAM"],
            "disguise":         self.base_stats["DEXT"],
            "dual_wielding":    self.base_stats["DEXT"],
            "healing":          self.base_stats["WILL"],
            "history":          self.base_stats["INTL"],
            "hunting":          self.base_stats["ANAM"],
            "farming":          self.base_stats["STNG"],
            "intimidation":     self.base_stats["CHAR"],
            "investigation":    self.base_stats["INTL"],
            "insight":          self.base_stats["INTL"],
            "evasion":          self.base_stats["DEXT"],
            "martial_arts":     self.base_stats["DEXT"],
            "martial_attack":   self.base_stats["STNG"],
            "magic":            self.base_stats["WILL"],
            "magic_attack":     self.base_stats["WILL"],
            "mining":           self.base_stats["STNG"],
            "leadership":       self.base_stats["CHAR"],
            "persuasion":       self.base_stats["CHAR"],
            "finesse":          self.base_stats["DEXT"],
            "stealth":          self.base_stats["DEXT"],
            "survival":         self.base_stats["ANAM"],
            "sharpshooter":     self.base_stats["ANAM"],
            "swimming":         self.base_stats["ENDR"],
            "two-handed":       self.base_stats["STNG"],
        }

        self.level = 1
        self.experience = 0
        self.inventory = []
        self.profieciency = self.level / 5
        self.initiative = self.base_stats["ANAM"]
        self.movement_speed = self.base_stats["DEXT"] * 5
        self.armor_rating = 0
        self.physical_defense = 40 + self.base_stats["ENDR"] + self.armor_rating
        self.mental_defense = 40 + self.base_stats["WILL"] + self.profieciency
        self.action_points = self.base_stats["VIGR"]
        self.mana_points = self.base_stats["MANA"] * 5
        self.health_points = self.base_stats["VIGR"] * 5

        self.actions = []

        self.moves = {
                        "Martial_Weapon_Attack" : True,
                        "Martial_Apply_Status"  : False,
                        "Sweeping_Slash"        : False,
                        "Power_Strike"          : False,
                        "Dash"                  : False,
                        "Roll"                  : False,
                        "Dive"                  : False,
                        "Grab"                  : False,
                        "Grapple"               : False,
                        "Bite"                  : False,
                        "Parry"                 : False,
                        "Riposte"               : False,
                        "Martial_Projectile"    : False,
                        "Martial_Volley"        : False,
                        "Block"                 : False,
                        "Defend"                : False,
                        "Deflect"               : False,
                        "Push"                  : False,
                        "Slam"                  : False,

                        "Magic_Projectile"      : False,
                        "Magic_Volley"          : False,
                        "Beam"                  : False,
                        "Cone"                  : False,
                        "Aura"                  : False,
                        "Miasma"                : False,
                        "Pillar"                : False,
                        "Disk"                  : False,
                        "Magic_Apply_Status"    : False,
                        "Summon"                : False,
                        "Shield"                : False,
                        "Create"                : False,
                        "Shift"                 : False,
                        "Portal"                : False,
                        "Control"               : False,
                        "Dispell"               : False,
        }

        self.attributes = {
                        "Area_of_Effect"    : False,
                        "Extended"          : False,
                        "Elemental"         : False,
                        "Ricochet"          : False,
                        "Chained"           : False,
                        "Apply_Status"      : False,
                        "Disarm"            : False,
                        "Precise"           : False,
                        "Staggering"        : False,
                        "Charged_Up"        : False,
                        "Powerful"          : False,
                        "Triggered"         : False,
                        "Delayed"           : False,
                        "Selective"         : False,
                        "Healing"           : False,
                        "Restorative"       : False,
                        "Reviving"          : False,
                        "Sneaky"            : False,
                        "Distracting"       : False,
                        "Homing"            : False,
                        "Disguised"         : False,
                        "Static"            : False,
                        "Quick"             : False,
                        "Fast"              : False,
                        "Burst"             : False,
                        "Restricted"        : False,
                        "Gamble"            : False,
        }

        self.status_effects = {
                        "Buff"              : False,
                        "Debuff"            : False,
                        "Goaded"            : False,
                        "Frightened"        : False,
                        "Terrified"         : False,
                        "Hidden"            : False,
                        "Invisible"         : False,
                        "Charmed"           : False,
                        "Controlled"        : False,
                        "Disguised"         : False,
                        "Blind"             : False,
                        "Deaf"              : False,
                        "Bleeding"          : False,
                        "Freezing"          : False,
                        "Burning"           : False,
                        "Electrified"       : False,
                        "Rotting"           : False,
                        "Dissolving"        : False,
                        "Purified"          : False,
                        "Transformed"       : False,
                        "Silenced"          : False,
                        "Weakened"          : False,
                        "Madness"           : False,
                        "Wet"               : False,
                        "Petrified"         : False,
                        "Restrained"        : False,
                        "Incapacitated"     : False,
                        "Enlarged"          : False,
                        "Reduced"           : False,
                        "Immune"            : False,
                        "Flying"            : False,
                        "Dehydrated"        : False,
        }

def CleanUp_UserInput_for_Stats(user_input):
    base_stats_types = ["STNG", "VIGR", "ENDR", "DEXT", "WILL", "INTL", "CHAR", "MANA", "ANAM", "LUCK"]

    user_input = str.upper(user_input)

    if user_input in base_stats_types or user_input == "REMOVE" or user_input == "EXIT":
        return user_input
    else:
        print("Invalid input. Please enter a valid stat or 'REMOVE' to decrease a stat.")
        return None

def Print_Base_Stats(base_stats, available_points):
    """
    # Prints the stats of a E_Character: in a readable format.
    """
    # Table of simple colors for reference:
    # \033[1;30m - Black
    # \033[1;31m - Red
    # \033[1;32m - Green
    # \033[1;33m - Yellow
    # \033[1;34m - Blue
    # \033[1;35m - Purple
    # \033[1;36m - Cyan
    # \033[1;37m - White
    print(f"     \033[1;32mAvailable points: {available_points}\033[0m")
    print("\t \033[1;31mStat\033[0m | \033[1;34mValue\033[0m")
    print("\t----- | -----")
    for stat, value in base_stats.items():
        print(f"\t {stat} |   {value}")

def Calculate_Stats(base_stats, available_points=0):
    """
    # Allows a player E_Character: to calculate their stats.

    """
    while True:
        
        Print_Base_Stats(base_stats, available_points)
        user_input = CleanUp_UserInput_for_Stats(input("What stat would you like to increase?"))

        if user_input == "EXIT":
            print("Exiting stat selection.")
            break
        elif user_input == "REMOVE":

            Print_Base_Stats(base_stats, available_points)

            user_input = CleanUp_UserInput_for_Stats(input("What stat would you like to decrease?"))
            if user_input in base_stats and base_stats[user_input] > 1:
                base_stats[user_input] -= 1
                available_points += 1
            elif user_input == "EXIT":
                print("Exiting stat selection.")
                break
            else:
                print("Invalid input. Please enter a valid stat.")
        elif user_input in base_stats:
            if available_points > 0:
                base_stats[user_input] += 1
                available_points -= 1
            else:
                print("Not enough points to increase stat.")
        else:
            print("Invalid input. Please enter a valid stat.")

    return base_stats, available_points