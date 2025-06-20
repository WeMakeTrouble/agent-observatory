from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
from engine.agent import Echo
from engine.text_renderer import render_simulation_state_to_text

app = Flask(__name__)
CORS(app)

simulation_state = {"active_agents": [], "world_events": [], "step": 0}

def initialize_simulation():
    """Loads the seed data and prepares the simulation."""
    try:
        filepath = os.path.join(os.path.dirname(__file__), 'data', 'seeds', 'echo_001.json')
        with open(filepath, 'r') as f:
            character_data = json.load(f)
        one = Echo(character_data)
        simulation_state["active_agents"].append(one)
        simulation_state["world_events"].append(f"EVENT: {one.name} ({one.agent_id}) has arrived.")
        print("✅ Simulation Initialized Successfully.")
    except Exception as e:
        print(f"❌ Simulation Initialization Failed: {e}")

def run_simulation_tick():
    """Runs a single step of the simulation."""
    simulation_state["step"] += 1
    for agent in simulation_state["active_agents"]:
        action = agent.think()
        if action:
            event_result = agent.execute_action(action)
            simulation_state["world_events"].append(f"EVENT (Step {simulation_state['step']}): {agent.name} chose action '{action['name']}'.")
            if event_result:
                simulation_state["world_events"].append(event_result)

@app.route('/api/simulation-state')
def get_simulation_state():
    """API endpoint that returns the current state of the simulation."""
    run_simulation_tick()
    output = render_simulation_state_to_text(simulation_state)
    return jsonify({"terminal_output": output})

@app.route('/')
def index():
    return "<h1>Multiverse Engine API is running...</h1>"

if __name__ == "__main__":
    initialize_simulation()
    app.run(port=5000)
