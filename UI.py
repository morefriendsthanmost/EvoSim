#File to add code for the display/UI
import Environment as env
import Creatures as crt
import matplotlib.pyplot as plt
import numpy as np

def generateFoodVariables (length):
    '''
    Takes the length of the map from side to side and generates a random position, with higher chance of it being near the centre
    '''
    x = np.random.normal(0.0, 15)
    while (abs(x) > length/2):
        x = np.random.normal(0.0, 15)
    y = np.random.normal(0.0, 15)
    while (abs(y) > length/2):
        y = np.random.normal(0.0, 15)
    energy = np.random.normal(1.0, 0.2)
    while (energy < 0):
        energy = np.random.normal(0.0, 15)
    return x,y,energy

#for the test, let's create 6 pieces of food and one creature
foods = []
for i in range (6):
    foods.append(env.Food(generateFoodVariables (100)))
creatures = [crt.Creature()]#this needs to be filled in
