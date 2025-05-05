from PyQt5.QtWidgets import QPushButton, QLineEdit, QComboBox, QHBoxLayout, QTextEdit, QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame


import dataclasses
from Components import Name

from Systems.S_LLM_Controller import LLMController
from Systems.S_Component_Registry import ComponentRegistry

class HUD(QWidget):
    def __init__(self, c_registry: ComponentRegistry, entity_id):
        super().__init__()
        self.c_registry = c_registry
        self.entity_id = entity_id

        entity_name = str(self.c_registry.get_component_of_entity(Name, self.entity_id).name)

        self.setWindowTitle(entity_name + "'s HUD")
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
        components = self.c_registry.get_all_components_of_entity(self.entity_id)

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

                # elif isinstance(val, dict):
                #     for k, v in val.items():
                #         layout.addWidget(QLabel(f"\t{f.name}.{k}: {v}"))

                else:
                    layout.addWidget(QLabel(f"\t{f.name}: {val}"))

class LLMHUD(QWidget):
    def __init__(self, llm_controller: LLMController):
        super().__init__()
        self.llm = llm_controller

        self.setWindowTitle("LLM Interface")
        self.resize(500, 600)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Scrollable response area
        self.response_area = QTextEdit()
        self.response_area.setReadOnly(True)
        layout.addWidget(self.response_area)

        # Role switch dropdown
        role_layout = QHBoxLayout()
        self.role_dropdown = QComboBox()
        self.role_dropdown.addItems(["user", "gm", "player"])
        self.role_dropdown.currentTextChanged.connect(self.change_role)
        role_layout.addWidget(QLabel("LLM Role:"))
        role_layout.addWidget(self.role_dropdown)
        layout.addLayout(role_layout)

        # Input box + send button
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_button)
        layout.addLayout(input_layout)

    def change_role(self, new_role):
        self.llm.set_role(new_role)
        self.response_area.append(f"--- Switched to role: {new_role} ---")

    def send_message(self):
        user_input = self.input_box.text().strip()
        if not user_input:
            return
        self.response_area.append(f"[You]: {user_input}")
        self.input_box.clear()
        response = self.llm.send_message(user_input)
        self.response_area.append(f"[LLM-{self.llm.active_role}]: {response}")

class EntityLibraryExplorer(QWidget):
    def __init__(self, c_registry, e_registry):
        super().__init__()

        self.setWindowTitle("Entity Library Explorer")
        self.resize(600, 800)

        # Scroll setup
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QFrame()
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        scroll.setWidget(content)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)

        # Render LLM HUD
        llm_controller = LLMController()
        llm_hud = LLMHUD(llm_controller)
        content_layout.addWidget(llm_hud)

class AdminView(QWidget):
    def __init__(self, c_registry, e_registry):
        super().__init__()

        self.setWindowTitle("Entities HUD")
        self.resize(600, 800)

        # Scroll setup
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QFrame()
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        scroll.setWidget(content)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)

        # Render LLM HUD
        llm_controller = LLMController()
        llm_hud = LLMHUD(llm_controller)
        content_layout.addWidget(llm_hud)

        # Render each entity
        for eid in e_registry.registry:
            subhud = HUD(c_registry, eid)
            content_layout.addWidget(subhud)