import os
from openai import OpenAI
from typing import Literal
from dotenv import load_dotenv


class LLMController:
    def __init__(self, model="gpt-4.1"):
        load_dotenv()

        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise EnvironmentError("OPENAI_API_KEY not found in environment.")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.roles = {
            "user": {
                "system_prompt": "You are the assistant helping the user.",
                "history": []
            },
            "gm": {
                "system_prompt": "You are the Game Master running a simulation.",
                "history": []
            },
            "player": {
                "system_prompt": "You are a player character in a fantasy RPG world.",
                "history": []
            }
        }
        self.active_role: Literal["user", "gm", "player"] = "user"
        self._initialize_roles()

    def _initialize_roles(self):
        for role_data in self.roles.values():
            role_data["history"].append({
                "role": "system",
                "content": role_data["system_prompt"]
            })

    def set_role(self, role: Literal["user", "gm", "player"]):
        if role not in self.roles:
            raise ValueError(f"Invalid role: {role}")
        self.active_role = role

    def send_message(self, message: str) -> str:
        role_data = self.roles[self.active_role]
        role_data["history"].append({"role": "user", "content": message})

        response = self.client.responses.create(
            model=self.model,
            input=message
        )

        reply = response.output_text
        role_data["history"].append(reply)
        return reply
