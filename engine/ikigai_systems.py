import random

def process_thought_cycle(agent):
    """The first 'tick' of the Ikigai Engine for a single agent."""
    possible_actions = [{"name": "Explore", "type": "Discovery"}]
    
    if "Strange Rock" in agent.inventory["items"]:
        possible_actions.append({"name": "Build Simple Wall", "type": "Creation"})

    best_action = None
    highest_score = -float('inf')

    for action in possible_actions:
        score = 0
        if action["name"] == "Explore":
            score += agent.current_state["emotional_state"]["curiosity"] * 10
            if len(agent.inventory["items"]) > 0:
                score -= 5
        elif action["name"] == "Build Simple Wall":
            score += agent.current_state["desire_for_shelter"] * 10
            if "analyst" in agent.background:
                score += 7
        
        if score > highest_score:
            highest_score = score
            best_action = action
    
    return best_action

def execute_action(agent, action):
    """Executes the chosen action and modifies the Echo's state."""
    if action["name"] == "Explore":
        agent.location['x'] += random.randint(-5, 5)
        agent.location['y'] += random.randint(-5, 5)
        if random.random() < 0.3:
            agent.inventory["items"].append("Strange Rock")
            return f"EVENT: {agent.name} found a 'Strange Rock'!"
    elif action["name"] == "Build Simple Wall":
        agent.inventory["items"].remove("Strange Rock")
        return f"EVENT: {agent.name} built a 'Simple Wall' segment."
    return None
