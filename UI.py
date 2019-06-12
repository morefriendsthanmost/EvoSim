#File to add code for the display/UI
import Environment as env
import matplotlib.pyplot as plt
import math as maths

#for the test, let's create 6 pieces of food and one creature
radii_of_creatures_over_time, creature_positions_over_time, radii_of_foods_over_time, food_positions_over_time = env.runCycle(1, 6, 100)

fig, ax = plt.subplots()
for i in range (99):
    #get the xs and the ys
    ax.cla()
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    ax.text(-45,-45, "tick "+str(i+1))

    creatures_x_positions = []
    creatures_y_positions = []
    creatures_map_size    = []
    creature_markers = []
    for j in range (len(radii_of_creatures_over_time[i])):
        ax.add_artist(plt.Circle((creature_positions_over_time[i][j][0], creature_positions_over_time[i][j][1]), radii_of_creatures_over_time[i][j], color='r'))


    foods_x_positions = []
    foods_y_positions = []
    foods_map_size    = []
    for j in range (len(radii_of_foods_over_time[i])):
        ax.add_artist(plt.Circle((food_positions_over_time[i][j][0], food_positions_over_time[i][j][1]), radii_of_foods_over_time[i][j], color='b'))

    plt.draw()
    
    plt.pause(0.05)
plt.show()