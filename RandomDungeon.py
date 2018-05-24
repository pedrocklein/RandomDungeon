
# coding: utf-8

# In[1]:

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


#Setting up globals
room_id = 0
passage_id = 0


#Defining ID functions
def getRoomID():
    global room_id
    room_id = room_id + 1

    return 'room_' + format(room_id)

def getPassageID():
    global passage_id
    passage_id = passage_id + 1

    return 'passage_'+format(passage_id)


def generateInitialArea():
    
    random_initial_area = np.random.randint(1,11)
    
    if random_initial_area == 1:
        return {
            'id' : getRoomID(),
            'description' : 'Quadrada, 6 x 6 m; passagem em cada parede',
            'dimensions' : (4,4,'s'),
            'passages': 4,
            'doors': 0,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 2:
        return {
            'id' : getRoomID(),
            'description' : 'Quadrada, 6 x 6 m; porta em duas paredes, passagem na terceira parede',
            'dimensions' : (4,4,'s'),
            'passages': 1,
            'doors' : 2,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 3:
        return {
            'id' : getRoomID(),
            'description' : 'Quadrada, 12 x 12 m; porta em tres paredes',
            'dimensions' : (8,8,'s'),
            'passages': 0,
            'doors' : 3,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 4:
        return {
            'id' : getRoomID(),
            'description' : 'Retangular, 24 x 6 m, com fileiras de colunas no meio;' + 
                            ' duas passagens levando para cada parede longa, portas em cada parede curta',
            'dimensions' : (16,4,'r'),
            'passages': 2,
            'doors' : 2,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 5:
        return {
            'id' : getRoomID(),
            'description' : 'Retangular, 6 x 12 m; passagem em cada parede',
            'dimensions' : (4,8,'r'),
            'passages': 4,
            'doors' : 0,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 6:
        return {
            'id' : getRoomID(),
            'description' : 'Circular, 12 m de diametro; uma passagem em cada direção cardinal',
            'dimensions' : (8, 0,'c'),
            'passages': 4,
            'doors' : 0,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 7:
        return {
            'id' : getRoomID(),
            'description' : 'Circular, 12 m de diametro; uma passagem em cada direcao cardinal; ' +
                            'poco no meio da sala (pode levar para o nivel inferior)',
            'dimensions' : (8,0,'c'),
            'passages': 4,
            'doors' : 0,
            'secret_doors': 0,
            'wells' : 1
        }
    elif random_initial_area == 8:
        return {
            'id' : getRoomID(),
            'description' : 'Quadrada, 6 x 6 m; porta em duas paredes, passagem na terceira parede, porta secreta' 
                             + ' na quarta parede',
            'dimensions' : (4,4,'q'),
            'passages': 1,
            'doors' : 2,
            'secret_doors': 1,
            'wells' : 0
        }
    elif random_initial_area == 9:
        return {
            'id' : getPassageID(),
            'description' : 'Passagem, 3 m de largura; intersecao em T',
            'dimensions' : (2,0,'T'),
            'passages': 3,
            'doors' : 0,
            'secret_doors': 0,
            'wells' : 0
        }
    elif random_initial_area == 10:
        return {
            'id' : getPassageID(),
            'description' : 'Passagem, 3 m de largura; intersecao de quatro vias',
            'dimensions' : (2,0,'+'),
            'passages': 4,
            'doors' : 0,
            'secret_doors': 0,
            'wells' : 0
        }       
    
    return 'Error:', random_initial_area, 'does not exist!'


def generateExits(is_large):
    random_exits = np.random.randint(1,21)
    n_exits = 0
    if (random_exits >= 1) and (random_exits <= 3):
        if not is_large:
            n_exits = 0
        else:
            n_exits = 0
    elif (random_exits >= 4) and (random_exits <= 5):
        if not is_large:
            n_exits = 0
        else:
            n_exits = 1
    elif (random_exits >= 6) and (random_exits <= 8):
        if not is_large:
            n_exits = 1
        else:
            n_exits = 1
    elif (random_exits >= 9) and (random_exits <= 11):
        if not is_large:
            n_exits = 1
        else:
            n_exits = 2
    elif (random_exits >= 12) and (random_exits <= 13):
        if not is_large:
            n_exits = 2
        else:
            n_exits = 2
    elif (random_exits >= 14) and (random_exits <= 15):
        if not is_large:
            n_exits = 2
        else:
            n_exits = 3
    elif (random_exits >= 16) and (random_exits <= 17):
        if not is_large:
            n_exits = 3
        else:
            n_exits = 3
    elif (random_exits == 18):
        if not is_large:
            n_exits = 3
        else:
            n_exits = 4
    elif (random_exits == 19):
        if not is_large:
            n_exits = 4
        else:
            n_exits = 5
    elif (random_exits == 20):
        if not is_large:
            n_exits = 4
        else:
            n_exits = 6
    exits = []
    for i in range(n_exits):
        location = ''
        random_location = np.random.randint(0,21)
        if (random_location >=1) and (random_location <=7):
            location = 'Parede oposta à entrada'
        elif (random_location >=8) and (random_location <=12):
            location = 'Parede à esquerda da entrada'
        elif (random_location >=13) and (random_location <=17):
            location = 'Parede à direita da entrada'
        elif (random_location >=18) and (random_location <=20):
            location = 'Mesma parede da entrada'
        
        exits.append(
            (
                'door' if np.random.randint(1,3) < 2 else 'passage',                
                location
            )
        )
    return exits

def generateRoom(id_from):
    random_room = np.random.randint(1,20)
    if (random_room == 1) | (random_room == 2):
        is_large = False
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Quadrada, 6 x 6 m' + description,
            'dimensions' : (4,4,'s'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 3) | (random_room == 4):
        is_large = False
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Quadrada, 9 x 9 m' + description, 
            'dimensions' : (6,6,'s'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 5) | (random_room == 6):
        is_large = False
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Quadrada, 12 x 12 m' + description, 
            'dimensions' : (8,8,'s'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room >= 7) | (random_room <= 9):
        is_large = False
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Retangular, 6 x 9 m' + description, 
            'dimensions' : (4,6,'r'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room >= 10) | (random_room <= 12):
        is_large = False
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Retangular, 9 x 12 m' + description, 
            'dimensions' : (6,8,'r'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room >= 13) | (random_room <= 14):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Retangular, 12 x 15 m' + description, 
            'dimensions' : (8,10,'r'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 15):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Retangular, 15 x 24 m' + description, 
            'dimensions' : (10,16,'r'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 15):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Retangular, 15 x 24 m' + description, 
            'dimensions' : (10,16,'r'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 16):
        is_large = False
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Circular, 9 m de diametro' + description, 
            'dimensions' : (6,0,'c'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 17):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Circular, 15 m de diametro' + description, 
            'dimensions' : (10,0,'c'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 18):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Octogonal, 12 x 12 m' + description, 
            'dimensions' : (8,8,'o'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 19):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Octogonal, 18 x 18 m' + description, 
            'dimensions' : (12,12,'o'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }
    elif (random_room == 20):
        is_large = True
        exits = generateExits(is_large)
        doors = 0
        passages = 0
        description = ''
        for exit in exits:
            if exit[0] == 'door':
                doors = doors + 1
            elif exit[0] == 'passage':
                passages = passages + 1
            description = description + "; one " + exit[0] + ' at ' + exit[1] 
        return{
            'id': getRoomID(),
            'description': 'Trapezoide, aproximadamente 12 x 18 m' + description, 
            'dimensions' : (8,12,'t'),
            'passages' : passages, 
            'doors': doors,
            'secret_doors': 0,
        }


def generateStairs(id_from):
    random_stair = np.random.randint(1,21)
    
    if (random_stair >=1) and (random_stair <=4):
        return {
            'id' : getPassageID(),
            'description': 'Desce um nivel para uma camara',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair >=5) and (random_stair <=8):
        return {
            'id' : getPassageID(),
            'description': 'Desce um nivel para uma passagem de 6 m de comprimento',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==9):
        return {
            'id' : getPassageID(),
            'description': 'Desce dois niveis para uma camara',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==10):
        return {
            'id' : getPassageID(),
            'description': 'Desce dois niveis para uma passagem de 6 m de comprimento',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==11):
        return {
            'id' : getPassageID(),
            'description': 'Desce três niveis para uma camara',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==12):
        return {
            'id' : getPassageID(),
            'description': 'Desce tres níveis para uma passagem de 6 m de comprimento',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==13):
        return {
            'id' : getPassageID(),
            'description': 'Sobe um nivel para uma camara',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==14):
        return {
            'id' : getPassageID(),
            'description': 'Sobe um nivel para um passagem de 6 m de comprimento',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==15):
        return {
            'id' : getPassageID(),
            'description': 'Sobe para um beco sem saida',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==16):
        return {
            'id' : getPassageID(),
            'description': 'Desce para um beco sem saida',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==17):
        return {
            'id' : getPassageID(),
            'description': 'Chamine sobe um nivel para uma passagem de 6 m de comprimento',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==18):
        return {
            'id' : getPassageID(),
            'description': 'Chamine sobe dois niveis para uma passagem de 6 m de comprimento',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==19):
        return {
            'id' : getPassageID(),
            'description': 'Fosso (com ou sem elevador) para um nivel abaixo em uma camara',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }
    elif (random_stair ==20):
        return {
            'id' : getPassageID(),
            'description': 'Fosso (com ou sem elevador) para um nivel acima em uma camara e um nivel abaixo em uma camara',
            'dimensions' : (2,2,'s'),
            'passages' : 0, 
            'doors': 0,
            'secret_doors': 0,
        }    


def generatePassages(id_from):
    random_passage = np.random.randint(1,21)
    if (random_passage == 1) or (random_passage == 2): 
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 9 m, sem portas ou passagens laterais',
            'dimensions' : (6,1,'l'),
            'coming_from': id_from,
            'passages': 1,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 3):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, porta a direita, então 3 m adicionais a frente',
            'dimensions' : (4,1,'l'),
            'coming_from': id_from,
            'passages': 1,
            'doors' : 1,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 4):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, porta a esquerda, então 3 m adicionais a frente',
            'dimensions' : (9,1,'l'),
            'coming_from': id_from,
            'passages': 1,
            'doors' : 1,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 5):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m; passagem termina em uma porta',
            'dimensions' : (4,1,'l'),
            'coming_from': id_from,
            'passages': 0,
            'doors' : 1,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 6) or (random_passage == 7):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, passagem lateral a direita, então 3 m adicionais a frente',
            'dimensions' : (6,1,'l'),
            'coming_from': id_from,
            'passages': 2,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 8) or (random_passage == 9):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, passagem lateral a esquerda, então 3 m adicionais a frente',
            'dimensions' : (4,1,'l'),
            'coming_from': id_from,
            'passages': 2,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 8) or (random_passage == 9):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, passagem lateral a esquerda, então 3 m adicionais a frente',
            'dimensions' : (6,1,'l'),
            'coming_from': id_from,
            'passages': 2,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 8) or (random_passage == 9):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, passagem lateral a esquerda, então 3 m adicionais a frente',
            'dimensions' : (6,1,'l'),
            'coming_from': id_from,
            'passages': 2,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 10):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, chega a um beco sem saída, ' +
                            '10 por cento de chance de ter uma porta secreta',
            'dimensions' : (4,1,'l'),
            'coming_from': id_from,
            'passages': 0,
            'doors' : 0,
            'secret_doors': (1 if np.random.randint(1,10) == 7 else 0),
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 11) or (random_passage == 12):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, então a passagem vira à direita e continua por 3m ',
            'dimensions' : (4,2,'Lr'),
            'coming_from': id_from,
            'passages': 1,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage == 13) or (random_passage == 14):
        return {
            'id' : getPassageID(),
            'description' : 'Linha reta de 6 m, então a passagem vira à esquerda e continua por 3 m',
            'dimensions' : (4,2,'Ll'),
            'coming_from': id_from,
            'passages': 1,
            'doors' : 0,
            'secret_doors': 0,
            'width': (1 if np.random.randint(1,13) < 3 else 2)
        }
    elif (random_passage >= 15) and (random_passage <= 19):
        return generateRoom(id_from)
    elif (random_passage == 20):
        return generateStairs(id_from)    

def generateDungeon(levels = 0, reset_global_ids = True):    
    
    if reset_global_ids:
        global room_id
        global passage_id
        room_id = 0
        passage_id = 0
    
    with file('Dungeon.txt', 'w') as f:
        dungeon = []
        total_exits = 0
        initial_area = generateInitialArea()
        dungeon.append(initial_area)
        f.write(format(initial_area)+'\n')
        current_level = 1
        
        for di, dungeon_item in enumerate(dungeon):
            dungeon.pop(di)
            if current_level != levels:
                if 'passage' in dungeon_item['id']:
                    total_exits = dungeon_item['doors'] + dungeon_item['passages'] + dungeon_item['secret_doors']
                elif 'room' in dungeon_item['id']:
                    total_exits = dungeon_item['doors'] + dungeon_item['passages']
                for exit in range(total_exits):                
                    new_passage = generatePassages(dungeon_item['id'])        
                    dungeon.append(new_passage)
                    f.write(format(new_passage)+'\n')                
                current_level = current_level + 1
            else:
                f.close()
                break
    print "This dungeon generation has reached its end at level ", current_level
    f.close()    

generateDungeon()
