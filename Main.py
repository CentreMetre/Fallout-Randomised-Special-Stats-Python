'''
Author: CentreMetre | Martin McLaren
Date started: 16/01/2022
'''

#------Imports------

from multiprocessing.sharedctypes import Value
import random

#------Imports------
#------------
#------Constant variables------

MaxPointsGamesList = {'Fallout 3' : 40,
             'Fallout NV' : 40,
             'Fallout 4' : 28
             } #used a dictionary sintead of assigning them to variables so that i can more easily check the game chosed and assign the max amount of points using the variable names.
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

GamesList = ['3', 'NV', '4']
YesOrNo = ''' [Y]es or [N]o'''
YesCheck = ['y', 'yes'] #Makes it easier to check if a 'Yes' input is entered. The programme will .lower() all yes or no inputs
NoCheck = ['n', 'no'] #Makes it easier to check if a 'No' input is entered. The programme will .lower() all yes or no inputs
InvalidInput = 'The input you entered is invalid. Please try again.'
#capitalise = capitalize()

#------Constant variables------


SpecialDict = {
    'Strength' : 1,
    'Perception' : 1,
    'Endurance' : 1,
    'Charisma' : 1,
    'Intellegence' : 1,
    'Agility' : 1,
    'Luck' : 1
    } #Default starting points



SpecialList = list(SpecialDict)

def WhatGame():
    print('What game are you playing? (3 = FO3, NV = New Vegas, 4 = FO4)')
    Game = str(input())
    Game = Game.upper()
    print(Game)
    if Game not in GamesList:
        print(InvalidInput)
        WhatGame()
    elif Game in GamesList:
        print(('You chose Fallout {}, is this correct?' + YesOrNo).format(Game))
        input()
        GeneratePoints(Game)

'''
def GetSeed(Game):
    IsSeed = False
    Seed = 0
    print(''''''Do you want a seed for the random number generator? '''''' + YesOrNo + '''''' (A seed is a number that the random number generator uses make a number. 
          If you use a seed, using that seed again will make you generate the same number)'''''')
    input().lower()
    if input in YesCheck: 
        try:
            Seed = input()
            Seed = float(Seed)
            IsSeed = True
            print('Enter a number')
            GeneratePoints(Game, IsSeed, Seed)
        except ValueError:
            print(InvalidInput)
            GetSeed(Game)
        finally:
            print('Something went wrong. Please close and reopen the programme')
    elif input in NoCheck:
        GeneratePoints(Game, IsSeed, Seed)
    else:
        print(InvalidInput)
'''#i dont think a seed would work, so this is not going to be used.

def GeneratePoints(Game): #, IsSeed, Seed): #when there was gonna be a seed for the RNG
    MaxPoints = MaxPointsGamesList[Game]
    PointsLeft = MaxPointsGamesList[Game]
    for i in range(0, len(SpecialDict)):
        PointsToApply = random.randint()
        PointsLeft = PointsLeft - PointsToApply
        if 
        
        
    

WhatGame()