# Import necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the universe of discourse for temperature and fan speed
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Generate fuzzy membership functions automatically
temperature.automf(3)  # Creates three fuzzy sets: poor, average, good
fan_speed.automf(3)    # Creates three fuzzy sets: poor, average, good

# Define custom membership functions if needed (e.g., for 'hot' temperature)
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 35, 40])

# Update the membership function for 'high' fan speed if necessary
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [70, 85, 100])

# Define the fuzzy rules
rule1 = ctrl.Rule(temperature['poor'], fan_speed['poor'])  # Use 'poor' instead of 'slow'
rule2 = ctrl.Rule(temperature['average'], fan_speed['average'])  # Use 'average'
rule3 = ctrl.Rule(temperature['good'] | temperature['hot'], fan_speed['high'])  # Use 'high'

# Create and simulate a fuzzy control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Input a crisp value for temperature
fan_speed_simulation.input['temperature'] = 30.5

# Compute the result
fan_speed_simulation.compute()

# Output the fan speed
print(fan_speed_simulation.output['fan_speed'])

# Visualize the result
fan_speed.view(sim=fan_speed_simulation)
plt.show();