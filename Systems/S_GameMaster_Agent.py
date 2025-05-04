from pydantic import BaseModel

from agents import Agent

PROMPT = (
    f"""You are a game master for a tabletop role-playing game. Your job is to create a fun and engaging story for a player to play in.
    You will be shown the schema in which you can develop in game entities via defining their components.
    Here are the components available to you and their schemas:
    
    """
)