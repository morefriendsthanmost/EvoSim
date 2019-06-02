#File to add code for the creatures
import math

unique_ID = 0
class Creature(object):

    '''
    The class to define a creature, its properties and the various things it can do
    '''

    def init(self,x_location,y_location,speed,cycle_energy,mass):

        '''
        Defines a creature on the class calling
        '''

        self.x_location = x_location
        self.y_location = y_location
        self.speed = speed
        self.cycle_energy = cycle_energy
        self.current_energy = None
        self.mass = mass

        global unique_ID
        unique_ID += 1
        self.ID = unique_ID #possibly not needed?

    def moveOneTick(self,direction,tick_length):

        '''
        Moves the creature for a distance defined by 'self.speed' * 'tick_length' in direction 'direction', a radian value from the positive x axis in a counter-clockwise direction (as is the standard in maths), then subtracts the distance moved from energy required to make this manuever from the current energy
        '''

        self.x_location += (self.speed * tick_length * math.cos(direction))
        self.y_location += (self.speed * tick_length * math.sin(direction))
        self.current_energy += -(self.mass * self.speed/tick_length) # based off of mv^2/2 - except wanted it to be per unit distance, so then divide by distance, which becomes mv^2/2*v*t, which is mv/2t. Very much up to debate.

    def eatFood(self,food_energy):
        
        '''
        Adds food consumed to the current energy
        '''

        self.current_energy += food_energy