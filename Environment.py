#File to add code for the environment in which the creatures reside

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
