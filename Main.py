'''
Author: CentreMetre | Martin McLaren
Date started: 16/01/2022
'''

Fallout3MaxPoints = 40 #Defualt of 5 per attribute + 5 ( (5*7) + 5 )
FalloutNVMaxPoints = 40 #NV will always be used in place of 'New Vegas' in variable names. #Defualt of 5 per attribute + 5 ( (5*7) + 5 )
Fallout4MaxPoints = 28 #This includes the mandatory 1 on each stat:
'''
----------------
Strength: 1
Perception: 1
Endurance: 1
Charisma: 1
Intellegence: 1
Agility: 1
Luck: 1
---------------
Points Left: 21
'''

Special = {'Strength' : 1, 'Perception' : 1, 'Endurance' : 1, 'Charisma' : 1, 'Intellegence' : 1, 'Agility' : 1, 'Luck' : 1} #Default starting points

def WhatGame():
    GamesList = ['3', 'NV', '4']
    print('What game are you playing? (3 = FO3, NV = New Vegas, 4 = FO4)')
    Game = str(input())
    Game = Game
    #Game = 'Fallout ' + Game
    for _game in GamesList:
        if _game == Game:
            print('You have chosen ' 'Fallout ' + Game)
        elif _game != Game:
            print()
    #print(Game)
    
WhatGame()