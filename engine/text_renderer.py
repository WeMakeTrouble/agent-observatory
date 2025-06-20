class Colors:
    HEADER = '\033[92m'
    BODY = '\033[32m'
    AGENT_NAME = '\033[93m'
    ENDC = '\033[0m'

def render_simulation_state_to_text(state):
    """Formats the current simulation state into a retro, green-screen string."""
    header = f"{Colors.HEADER}============================================================\n"
    header += f"| MULTIVERSE SIMULATION | STEP: {str(state['step']).zfill(4)}\n"
    header += f"============================================================{Colors.ENDC}"

    world_status = f"{Colors.HEADER}--- WORLD STATE ---{Colors.ENDC}\n"
    world_status += f"{Colors.BODY}  > Location: The Transit Hub (The White)\n"
    world_status += f"{Colors.BODY}  > Environment: Still, Silent, Bright\n{Colors.ENDC}"

    agent_details_list = []
    for agent in state["active_agents"]:
        agent_name_colored = f"{Colors.AGENT_NAME}{agent.name} ({agent.agent_id}){Colors.ENDC}{Colors.BODY}"
        agent_details = f"""
  AGENT: {agent_name_colored}
  ---------------------------------
  | Location: {agent.location}
  | Cognitive State: {agent.current_state['cognitive_state']}
  | Ikigai Level: {agent.current_state['ikigai_level']:.2f}
  | Inventory: {agent.inventory['items']}"""
        agent_details_list.append(agent_details)
    
    agent_status = f"{Colors.HEADER}--- ACTIVE AGENTS ---{Colors.ENDC}{Colors.BODY}" + ''.join(agent_details_list) + Colors.ENDC

    recent_events = '\n'.join([f'{Colors.BODY}  > {event}{Colors.ENDC}' for event in state["world_events"][-5:]])
    event_log = f"\n{Colors.HEADER}--- RECENT EVENTS ---{Colors.ENDC}\n{recent_events}"

    return f"{header}\n{world_status}\n{agent_status}\n{event_log}"
