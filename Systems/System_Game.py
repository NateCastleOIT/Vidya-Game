from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys
from Class_Player_HUD import HUD
from Class_Character import Character

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a character instance
    hero = Character(True, "Hero")

    # Create a HUD instance
    hud = HUD(hero)
    hud.show()

    print("HUD is displayed. You can now interact with it.")
    print("you get hit for 6 dmg.")
    input("Press Enter to update the HUD...")

    hud.update_stat('health_points', hero.health_points - 6)

    sys.exit(app.exec_())