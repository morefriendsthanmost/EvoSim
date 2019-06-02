#File to add code for the creatures
import math

unique_ID = 0

class Creature(object):

    '''
    The class to define a creature, its properties and the various things it can do
    '''

    def init(self, x_location, y_location, speed, cycle_energy, radius, sensory_range):

        '''
        Defines a creature on the class calling
        '''

        self.x_location = x_location
        self.y_location = y_location
        self.speed = speed
        self.current_energy = None
        self.radius = radius
        self.volume = 4/3 * math.pi * pow(self.radius,3)
        self.sensory_range = sensory_range

        global unique_ID
        unique_ID += 1
        self.ID = unique_ID #possibly not needed?

    def moveOneTick(self,direction,tick_length):

        '''
        Moves the creature for a distance defined by 'self.speed' * 'tick_length' in direction 'direction', a radian value from the positive x axis in a counter-clockwise direction (as is the standard in maths), then subtracts the distance moved from energy required to make this manuever from the current energy
        '''

        self.x_location += (self.speed * tick_length * math.cos(direction))
        self.y_location += (self.speed * tick_length * math.sin(direction))
        self.current_energy += -(self.volume * self.speed / tick_length) # based off of mv^2/2 - except wanted it to be per unit distance, so then divide by distance, which becomes mv^2/2*v*t, which is mv/2t. Very much up to debate.

    def eatFood(self, food_energy):
        
        '''
        Adds food consumed to the current energy
        '''

        self.current_energy += food_energy

    def getSensoryData(self):
        '''
        Discovers what is within the sensory range of the creature
        '''
        #yet to figure out - needs to return an array of objects in the range of this creatures senses - food and other creatures, possibly with the other creatures being seperated into threat or mate? assuming reproduction is done traditionally...
        pass 

    def findPath(self, tick_length):
        for each in self.getSensoryData():
            #find the best thing to run towards/find something to run away from
            pass
        #find direction to move from sensory data
        self.moveOneTick(direction, ticklength)

    def getLocation(self):

        '''
        returns the coordinates of the creature
        '''

        return (self.x_location, self.y_location)

    def runTick(self,tick_length):
        
        '''
        defines how the creature deals with a tick
        '''

        #do sensory stuff
        #do movement
        #metabolism
        self.current_energy += -(0.007*self.sensory_range*self.volume)
