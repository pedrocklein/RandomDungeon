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

#Setting up globals
room_id = 0
passage_id = 0

#Defining imports
import numpy as np

#Defining ID functions

def getRoomID():
    global room_id
    room_id = room_id + 1

    return room_id

def getPassageID():
    global passage_id
    passage_id = passage_id + 1

    return passage_id

#Defining generation functions
def generateStartingArea():
    '''
    ÁREA INICIAL
    A tabela Área Inicial produz uma câmara ou um conjunto de corredores na entrada da sua masmorra. Quando rolar para uma área inicial aleatória, 
    escolha uma das portas ou passagens levando para a área inicial como a entrada da masmorra como um todo.
    Quando tiver escolhido a entrada, role na tabela apropriada para cada passagem ou porta levando para fora da área inicial. 
    Cada passagem se estende 3 metros além da área inicial. Após esse ponto, verifique na tabela Passagem para cada passagem para determinar o que existe além.
    Use a tabela Atrás de uma Porta para determinar o que existe atrás de portas e portas secretas.
    :return: 
    '''
    random_starting_area = np.randint(1,11)
    starting_area = {}
    
    #Transcription of the table for starting area
    if random_starting_area == 1:
        #Quadrada, 6x6m; passagem em cada parede
        starting_area['ID'] = getRoomID()
        starting_area['dimensions'] = (4,4) #dimensions are in squares
        starting_area['exits'] = [(getPassageID(), 'passage', 'north'),
                                  (getPassageID(), 'passage', 'south'),
                                  (getPassageID(), 'passage', 'east'),
                                  (getPassageID(), 'passage', 'west')]

    elif random_starting_area == 2:
        #Quadrada, 6x6m; porta em duas paredes, passagem na terceira parede
        starting_area['ID'] = getRoomID()
        starting_area['dimensions'] = (4, 4)  # dimensions are in squares
        coordinates = ['north', 'south', 'east', 'west']
        random_coordinate = np.randint(1, len(coordinates))
        first_passage = (getPassageID(), 'door', coordinates[random_coordinate])
        coordinates.pop(random_coordinate)
        random_coordinate = np.randint(1, len(coordinates))
        second_passage = (getPassageID(), 'door', coordinates[random_coordinate])
        coordinates.pop(random_coordinate)
        random_coordinate = np.randint(1, len(coordinates))
        third_passage = (getPassageID(), 'passage', coordinates[random_coordinate])

        starting_area['exits'] = [first_passage, second_passage, third_passage]

    elif random_starting_area == 3:
        #Quadrada, 12x12 m; porta em três paredes
        starting_area['ID'] = getRoomID()
        starting_area['dimensions'] = (8, 8)  # dimensions are in squares
        coordinates = ['north', 'south', 'east', 'west']
        random_coordinate = np.randint(1, len(coordinates))
        first_passage = (getPassageID(), 'door', coordinates[random_coordinate])
        coordinates.pop(random_coordinate)
        random_coordinate = np.randint(1, len(coordinates))
        second_passage = (getPassageID(), 'door', coordinates[random_coordinate])
        coordinates.pop(random_coordinate)
        random_coordinate = np.randint(1, len(coordinates))
        third_passage = (getPassageID(), 'door', coordinates[random_coordinate])

        starting_area['exits'] = [first_passage, second_passage, third_passage]
        pass
    elif random_starting_area == 4:
        #Retangular, 24x6 m, com fileiras de colunas no meio; duas passagens levando para cada parede longa, portas em cada parede curta
        pass
    elif random_starting_area == 5:
        pass
    elif random_starting_area == 6:
        pass
    elif random_starting_area == 7:
        pass
    elif random_starting_area == 8:
        pass
    elif random_starting_area == 9:
        pass
    elif random_starting_area == 10:
        pass
    
            

def generatePassage():
    pass

def generateDoor():
    pass

def generateChamber():
    pass

def generateStairs():
    pass