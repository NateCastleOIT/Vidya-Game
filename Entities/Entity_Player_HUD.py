from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QComboBox, QApplication, QScrollArea, QFormLayout, QGroupBox
)
from PyQt5.QtCore import Qt

class HUD(QWidget):
    def __init__(self, character):
        super().__init__()
        self.setWindowTitle(f"{character.name}'s HUD")
        self.setGeometry(100, 100, 400, 600)

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        widget = QWidget()
        layout = QVBoxLayout(widget)

        # --- Basic Stats Section ---
        basic_stats_box = QGroupBox("Basic Info")
        basic_layout = QFormLayout()

        self.labels = {}
        integer_fields = [
            'level', 'experience', 'health_points', 'mana_points',
            'action_points', 'movement_speed', 'physical_defense', 'mental_defense'
        ]
        for field in integer_fields:
            label = QLabel(str(getattr(character, field)))
            basic_layout.addRow(f"{field.replace('_', ' ').title()}:", label)
            self.labels[field] = label

        basic_stats_box.setLayout(basic_layout)
        layout.addWidget(basic_stats_box)

        # --- Dictionaries as Dropdowns ---
        self.add_dropdown(layout, "Skills", character.skills)
        self.add_dropdown(layout, "Moves", character.moves)
        self.add_dropdown(layout, "Attributes", character.attributes)
        self.add_dropdown(layout, "Status Effects", character.status_effects)

        scroll.setWidget(widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def add_dropdown(self, layout, title, data_dict):
        group_box = QGroupBox(title)
        group_layout = QVBoxLayout()

        combo = QComboBox()
        for key, value in data_dict.items():
            combo.addItem(f"{key}: {value}")

        group_layout.addWidget(combo)
        group_box.setLayout(group_layout)
        layout.addWidget(group_box)

    def update_stat(self, field, value):
        if field in self.labels:
            self.labels[field].setText(str(value))
