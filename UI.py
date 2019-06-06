#File to add code for the display/UI
import Environment as env
import matplotlib.pyplot as plt

#for the test, let's create 6 pieces of food and one creature
creatures_over_time, foods_over_time = env.runCycle(1, 6, 100)

for i in range (100):
    #get the xs and the ys
    creatures_x_positions = []
    creatures_y_positions = []
    creatures_map_size    = []
    for j in range (len(creatures_over_time[i])):
        creatures_x_positions.append(creatures_over_time[i][j].x_location)
        creatures_y_positions.append(creatures_over_time[i][j].y_location)
        creatures_map_size.append(pow((2*creatures_over_time[i][j].radius),2))


    foods_x_positions = []
    foods_y_positions = []
    foods_map_size    = []
    for j in range (len(foods_over_time[i])):
        foods_x_positions.append(foods_over_time[i][j].x_location)
        foods_y_positions.append(foods_over_time[i][j].y_location)
        foods_map_size.append(pow((2*foods_over_time[i][j].radius),2))

    plt.plot(creatures_x_positions, creatures_y_positions, color= "red", marker = "o", markersize = creatures_map_size, linestyle = "None")
    plt.plot(foods_x_positions, foods_y_positions, color= "green", marker = "o", markersize = foods_map_size, linestyle = "None")

    plt.draw()
    
    plt.pause(0.5)