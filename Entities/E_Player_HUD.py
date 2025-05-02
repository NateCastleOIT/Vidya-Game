from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame
from Systems import ComponentRegistry
from Systems import component_name_map
import dataclasses

class HUD(QWidget):
    def __init__(self, registry: ComponentRegistry, entity_id):
        super().__init__()
        self.registry = registry
        self.entity_id = entity_id

        self.setWindowTitle("Entity HUD")
        self.resize(400, 600)  # Set a fixed or resizable height

        # Main layout of the HUD window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Container inside scroll area
        scroll_content = QFrame()
        scroll_layout = QVBoxLayout(scroll_content)

        # Attach to HUD
        scroll.setWidget(scroll_content)
        self.layout.addWidget(scroll)

        # Render everything into scroll layout
        self.render_components(scroll_layout)

    def render_components(self, layout):
        components = self.registry.get_all_components_of_entity(self.entity_id)

        for comp_cls, comp_data in components.items():
            layout.addWidget(QLabel(f"<b>{comp_cls.__name__}</b>"))

            for f in dataclasses.fields(comp_data):
                val = getattr(comp_data, f.name)
                meta = f.metadata

                if meta.get("ui") == "dropdown":
                    dropdown = QComboBox()
                    dropdown.addItems(meta["options"])
                    dropdown.setCurrentText(val)
                    dropdown.setEnabled(False)  # Optional: make it read-only for now
                    layout.addWidget(dropdown)

                elif isinstance(val, dict):
                    for k, v in val.items():
                        layout.addWidget(QLabel(f"\t{f.name}.{k}: {v}"))

                else:
                    layout.addWidget(QLabel(f"\t{f.name}: {val}"))

