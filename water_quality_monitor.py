import csv
import time
from collections import defaultdict
from sensor_simulator import read_sensors, NODES

WINDOW_SIZE = 10  

history = defaultdict(list)

def adaptive_threshold(values, margin):
    avg = sum(values) / len(values)
    return avg - margin, avg + margin


with open("water_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Node", "Temperature", "pH", "Turbidity", "Status"])

while True:
    for node in NODES.keys():
        temperature, ph, turbidity = read_sensors(node)

        history[node].append(ph)
        if len(history[node]) > WINDOW_SIZE:
            history[node].pop(0)

        if len(history[node]) >= 5:
            ph_min, ph_max = adaptive_threshold(history[node], margin=0.7)
        else:
            ph_min, ph_max = 6.5, 8.5

        status = "GOOD"
        if ph < ph_min or ph > ph_max or turbidity > 5:
            status = "BAD"

        timestamp = time.strftime("%H:%M:%S")

        with open("water_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, node, temperature, ph, turbidity, status])

        print(
            f"[{timestamp}] {node} | "
            f"T={temperature}°C | pH={ph} ({ph_min:.2f}-{ph_max:.2f}) | "
            f"Turb={turbidity} → {status}"
        )

    time.sleep(5)
