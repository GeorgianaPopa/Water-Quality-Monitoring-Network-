import random

NODES = {
    "Node_1": {"temp": (10, 25), "ph": (6.5, 8.5), "turb": (0, 5)},
    "Node_2": {"temp": (12, 28), "ph": (6.0, 9.0), "turb": (0, 6)},
    "Node_3": {"temp": (8, 22), "ph": (6.8, 8.2), "turb": (0, 4)}
}

def read_sensors(node_id):
    cfg = NODES[node_id]

    temperature = round(random.uniform(*cfg["temp"]), 2)
    ph = round(random.uniform(*cfg["ph"]), 2)
    turbidity = round(random.uniform(*cfg["turb"]), 2)

    return temperature, ph, turbidity
