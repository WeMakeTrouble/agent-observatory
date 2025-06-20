from . import ikigai_systems

class Echo:
    """Represents a single autonomous agent in the Transit Hub."""
    def __init__(self, character_data):
        self.agent_id = character_data.get("agent_id")
        self.name = character_data.get("name")
        self.background = character_data.get("background")
        self.abilities = character_data.get("abilities")
        self.traits = character_data.get("traits")
        self.phantom_memories = character_data.get("phantomMemories")
        
        self.current_state = {
            "cognitive_state": "Idle", "ikigai_level": 1.0,
            "emotional_state": {"hope": 0.5, "fear": 0.3, "curiosity": 0.7},
            "desire_for_shelter": 0.6
        }
        self.inventory = {"items": []}
        self.location = {"x": 0, "y": 0}

    def think(self):
        """The main AI loop, which calls out to our Ikigai systems for logic."""
        return ikigai_systems.process_thought_cycle(self)
        
    def execute_action(self, action):
        """Performs the chosen action and updates the agent's state."""
        return ikigai_systems.execute_action(self, action)
