#File to add code for the environment in which the creatures reside
import Creatures as crt
import numpy as np

def generateRandomNumberWithLowerLimit (mean, sigma, lower_limit):
    x = np.random.normal(mean, sigma)
    while (x < lower_limit):
        x = np.random.normal(mean, sigma)
    return x

def generateFoodVariables (length_of_map, mean_energy = 1.0):
    '''
    Takes the length of the map from side to side and generates a random position, with higher chance of it being near the centre
    '''

    x = np.random.normal(0.0, 15)
    while (abs(x) > length_of_map/2):
        x = np.random.normal(0.0, 15)
    y = np.random.normal(0.0, 15)
    while (abs(y) > length_of_map/2):
        y = np.random.normal(0.0, 15)
    energy = generateRandomNumberWithLowerLimit (mean_energy, 0.2, 0.01)

    return x,y,energy

def generateCreatureVariables (length_of_map, mean_speed = 1.0, mean_radius = 1.5, mean_sensory_range = 40):
    '''
    Takes the length of the map from side to side and generates all the random variables needed for a creature to work. the result cannot be passed directly to the creature init function since it lacks environment
    '''
    #chooses a random part of the borders to spawn the creatures in
    border = np.random.choice([1, 2, 3, 4])  
    if (1 == border):
        y = -50
        x = np.random.normal(0.0, 15)
        while (abs(x) > length_of_map/2):
            x = np.random.normal(0.0, 15)
    elif (2 == border):
        x = -50
        y = np.random.normal(0.0, 15)
        while (abs(y) > length_of_map/2):
            y = np.random.normal(0.0, 15)
    elif (3 == border):
        y = 50
        x = np.random.normal(0.0, 15)
        while (abs(x) > length_of_map/2):
            x = np.random.normal(0.0, 15)
    elif (4 == border):
        x = 50
        y = np.random.normal(0.0, 15)
        while (abs(y) > length_of_map/2):
            y = np.random.normal(0.0, 15)


    speed         = generateRandomNumberWithLowerLimit (mean_speed, 0.3, 0.1)
    radius        = generateRandomNumberWithLowerLimit (mean_radius, 0.2, 0.1)
    sensory_range = generateRandomNumberWithLowerLimit (mean_sensory_range, 5, 0.1)
    return  x, y, speed, radius, sensory_range

def getDistance(position_one, position_two):
    '''
    Takes in two touples of (x,y) locations and finds the distance between them
    '''
    return pow((pow((position_one[0]-position_two[0]),2) + pow((position_one[1]-position_two[1]),2)),1/2)


class Environment(object):
    def __init__(self, number_of_creatures, number_of_foods, tick_length = 1):

        '''
        Defines the enviroment on the class calling
        '''

        creatures = []
        for i in range (number_of_creatures):
            x, y, speed, radius, sensory_range = generateCreatureVariables (100)
            creaturs.append(crt.Creature(x, y, speed, 250, radius, sensory_range, self))
        self.creatures = creatures
        #will get the position of each creature
        positions_of_creatures = []
        for i in range (len(creatures)):
            positions_of_creatures.append(creatures[i].getLocation())
        self.positions_of_creatures = positions_of_creatures

        foods = []
        for i in range (number_of_foods):
            foods.append(Food(generateFoodVariables (100)))
        self.foods = foods
        #will get the position of each piece of food
        for i in range (len(foods)):
            positions_of_foods.append(foods[i].getLocation())
        self.positions_of_foods = positions_of_foods

    

        #####Define tick_length, to change when we know more about it#####
        self.tick_length = tick_length


    def getObjects(self):

        '''
        returns the coordinates of the piece of food
        '''
        all_objects = []
        for i in range (len(creatures)):
            temp = []
            temp.append(creatures[i])
            temp.append(creatures[i].getLocation())
            all_objects.append(temp)  
        for i in range (len(foods)):
            temp = []
            temp.append(foods[i])
            temp.append(foods[i].getLocation())
            all_objects.append(temp)   
        return (all_objects)

    def tick (self):
        
        '''
        Makes a time unit pass in the simulation
        '''
        #goes through each of the creatures
        for i in range (len(self.creatures)):
            #gets the direction it will move in
            direction = self.creatures[i].findPath()
            #makes the creature move in that direction
            creatures[i].moveOneTick(direction,tick_length)
            # updates the list of positions
            positions_of_creatures[i] = creatures[i].getLocation()
            #checks if the creature ovelaps with food, and if so, consumes it and then removes it from the list of foods
            for j in range (len(self.foods)):
                distance = getDistance(positions_of_foods[j],positions_of_creatures[i])
                if (distance < (creatures[i].radius+foods[j].radius)):
                    creatures[i].eatFood(foods[i].energy)
                    del foods[j]
                    del positions_of_foods[j]
                    
        pass
    pass

class Food(object):
    def init(self, x_location, y_location, energy):

        '''
        Defines a piece of food on the class calling
        '''

        self.energy     = energy
        self.x_location = x_location
        self.y_location = y_location
        self.radius     = pow((energy/420000),(1/3))


    def getLocation(self):

        '''
        returns the coordinates of the piece of food
        '''

        return (self.x_location, self.y_location)
    pass
