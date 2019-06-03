#File to add code for the environment in which the creatures reside
def getDistance(position_one, position_two):
    '''
    Takes in two touples of (x,y) locations and finds the distance between them
    '''
    return pow((pow((position_one[0]-position_two[0]),2) + pow((position_one[1]-position_two[1]),2)),1/2)


class Environment(object):
    def __init__(self, creatures, foods):

        '''
        Defines the enviroment on the class calling
        '''

        self.creatures = creatures
        #will get the position of each creature
        positions_of_creatures = []
        for i in range (len(creatures)):
            positions_of_creatures.append(creatures[i].getLocation())
        self.positions_of_creatures = positions_of_creatures

        self.foods = foods
        #will get the position of each piece of food
        for i in range (len(foods)):
            positions_of_foods.append(foods[i].getLocation())
        self.positions_of_foods = positions_of_foods

        all_objects = []
        for i in range (len(foods)):
            temp = []
            temp.append(foods[i])
            temp.append(foods[i].getLocation())
            all_objects.append(temp)
        for i in range (len(creatures)):
            temp = []
            temp.append(creatures[i])
            temp.append(creatures[i].getLocation())
            all_objects.append(temp)         

        #####Define ticklenght, to change when we know more about it#####
        self.ticklenght = 1


    def getObjects(self):

        '''
        returns the coordinates of the piece of food
        '''

        return (self.all_objects)

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

        self.energy = energy
        self.x_location = x_location
        self.y_location = y_location
        self.radius = pow((energy/420000),(1/3))


    def getLocation(self):

        '''
        returns the coordinates of the piece of food
        '''

        return (self.x_location, self.y_location)
    pass
