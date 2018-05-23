#!/usr/bin/env python

"""
RandomDungeon.py: Script for generating 
random dungeons according to the appendix 
from Dungeons and Dragons 5th Edition's 
Dungeon Master Guide.
"""

__author__ = 'Pedro Costa Klein'
__copyright__ = 'Copyright 2018, Pedro Costa Klein'
__credits__ = ''

__license__ = ''
__version__ = '0.1a'
__maintainer__= 'Pedro Costa Klein'
__email__ = 'pedrocklein@gmail.com'
__status__ = 'Prototype' #Devlopment, Production

#Defining imports
import numpy as np

#Defining genaration functions

def generateStartingArea():
    random_starting_area = np.randint(1,11)
    
    #Transcription of the table for starting area
    if random_staring_area == 1:
        pass
    elif random_staring_area == 2:
        #Square 20x20ft.: passage on each wall
    elif random_staring_area == 3:
        #Square 20x20ft.: door on two walls, passage in third wall
    elif random_staring_area == 4:
        
    elif random_staring_area == 5:
    elif random_staring_area == 6:
    elif random_staring_area == 7:
    elif random_staring_area == 8:
    elif random_staring_area == 9:
    elif random_staring_area == 10:
    
            

def generatePassage():
    pass

def generateDoor():
    pass

def generateChamber():
    pass

def generateStairs():
    pass