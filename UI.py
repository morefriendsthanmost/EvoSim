#File to add code for the display/UI
import Environment as env
import matplotlib.pyplot as plt

#for the test, let's create 6 pieces of food and one creature
radii_of_creatures_over_time, creature_positions_over_time, radii_of_foods_over_time, food_positions_over_time = env.runCycle(1, 6, 100)

for i in range (99):
    #get the xs and the ys
    creatures_x_positions = []
    creatures_y_positions = []
    creatures_map_size    = []
    for j in range (len(radii_of_creatures_over_time[i])):
        creatures_x_positions.append(creature_positions_over_time[i][j][0])
        creatures_y_positions.append(creature_positions_over_time[i][j][1])
        creatures_map_size   .append(pow((2*radii_of_creatures_over_time[i][j]),2))


    foods_x_positions = []
    foods_y_positions = []
    foods_map_size    = []
    for j in range (len(radii_of_foods_over_time[i])):
        foods_x_positions.append(food_positions_over_time[i][j][0])
        foods_y_positions.append(food_positions_over_time[i][j][1])
        foods_map_size   .append(pow((2*radii_of_foods_over_time[i][j]),2))
    plt.clf()
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)

    plt.scatter(creatures_x_positions, creatures_y_positions, color= "red", marker = "o", s = creatures_map_size, linestyle = "None")
    plt.scatter(foods_x_positions, foods_y_positions, color= "green", marker = "o", s = foods_map_size, linestyle = "None")
    
    plt.draw()
    
    plt.pause(0.05)
plt.show()