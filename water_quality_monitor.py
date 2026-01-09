import csv
import time
from sensor_simulator import *

THRESHOLDS = {
    "ph_min": 6.5,
    "ph_max": 8.5,
    "turbidity_max": 5.0,
    "tds_max": 300
}

with open("water_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Temperature", "pH", "Turbidity", "TDS", "Status"])

while True:
    temperature = read_temperature()
    ph = read_ph()
    turbidity = read_turbidity()
    tds = read_tds()

    status = "GOOD"

    if ph < THRESHOLDS["ph_min"] or ph > THRESHOLDS["ph_max"]:
        status = "BAD"
    if turbidity > THRESHOLDS["turbidity_max"]:
        status = "BAD"
    if tds > THRESHOLDS["tds_max"]:
        status = "BAD"

    timestamp = time.strftime("%H:%M:%S")

    with open("water_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, ph, turbidity, tds, status])

    print(f"[{timestamp}] Temp={temperature}°C | pH={ph} | Turb={turbidity} | TDS={tds} → {status}")

    time.sleep(5)
