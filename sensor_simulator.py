import random

def read_temperature():
    return round(random.uniform(5.0, 30.0), 2)

def read_ph():
    return round(random.uniform(6.0, 9.0), 2)

def read_turbidity():
    return round(random.uniform(0.0, 10.0), 2)

def read_tds():
    return round(random.uniform(50, 500), 2)
