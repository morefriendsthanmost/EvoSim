#File to add code for the creatures

unique_ID = 0
class Creature(object):

    '''
    The class to define a creature, its properties and the various things it can do
    '''

    def init(self,x_location,y_location,speed):

        '''
        Defines a creature on the class calling
        '''

        self.x_location = x_location
        self.y_location = y_location
        self.speed = speed

        global unique_ID
        unique_ID += 1
        self.ID = unique_ID #possibly not needed?
