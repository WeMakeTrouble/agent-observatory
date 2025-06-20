def render_simulation_state_to_text(state):
    """Formats the current simulation state into a simple text string."""
    agent = state["active_agents"][0]
    
    agent_details = (
        f"  AGENT: {agent.name} ({agent.agent_id})\n"
        f"  ---------------------------------\n"
        f"  | Location: {agent.location}\n"
        f"  | Cognitive State: {agent.current_state['cognitive_state']}\n"
        f"  | Ikigai Level: {agent.current_state['ikigai_level']:.2f}\n"
        f"  | Inventory: {agent.inventory['items']}"
    )

    recent_events = '\n'.join([f"  > {event}" for event in state["world_events"][-5:]])

    return (
        f"============================================================\n"
        f"| MULTIVERSE SIMULATION | STEP: {str(state['step']).zfill(4)}\n"
        f"============================================================\n"
        f"--- WORLD STATE ---\n"
        f"  > Location: The Transit Hub (The White)\n"
        f"  > Environment: Still, Silent, Bright\n\n"
        f"--- ACTIVE AGENTS ---\n{agent_details}\n\n"
        f"--- RECENT EVENTS ---\n{recent_events}\n"
        f"============================================================"
    )
