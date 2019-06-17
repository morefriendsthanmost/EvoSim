#For running the code - acts like a .exe file

import Creatures as crt
import Environment as env
import UI

environment = env.Environment(1, 6)
for i in range (3):
    radii_of_creatures_over_time, creature_positions_over_time, radii_of_foods_over_time, food_positions_over_time = environment.runCycle()
    UI.display_cycle(radii_of_creatures_over_time, creature_positions_over_time, radii_of_foods_over_time, food_positions_over_time, 0.05)
    environment.afterCycle ()