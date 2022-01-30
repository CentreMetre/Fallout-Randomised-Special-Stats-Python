'''
Author: CentreMetre | Martin McLaren | https://github.com/CentreMetre
Date started: 16/01/2022
Note: This is just kinda project i decided to make since i was bored, and wanted to test my renewed pyrthon skills, i am gonna make this in C# winforma also
'''

#------Imports------

import random

from pkg_resources import UnknownExtra

#------Imports------
#------------
#------Constant variables------

MaxPointsGamesDict = {'Fallout 3' : 40, #Defualt of 5 per attribute + 5 ( (5*7) + 5 )
             'Fallout NV' : 40, #NV will always be used in place of 'New Vegas' in variable names. #Defualt of 5 per attribute + 5 ( (5*7) + 5 )
             'Fallout 4' : 28 #This includes the mandatory 1 on each stat:
             } #used a dictionary sintead of assigning them to variables so that i can more easily check the game chosed and assign the max amount of points using the variable names.
'''
Fallout3MaxPoints = 40 #Defualt of 5 per attribute + 5 ( (5*7) + 5 )
FalloutNVMaxPoints = 40 #NV will always be used in place of 'New Vegas' in variable names. #Defualt of 5 per attribute + 5 ( (5*7) + 5 )
Fallout4MaxPoints = 28 #This includes the mandatory 1 on each stat:
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
YesCheck = ['y', 'yes'] #Makes it easier to check if a 'Yes' input is entered. The programme will manually .lower() all yes or no inputs
NoCheck = ['n', 'no'] #Makes it easier to check if a 'No' input is entered. The programme will manually .lower() all yes or no inputs
InvalidInput = 'The input you entered is invalid. Please try again.'
UnknownError = 'An error occured! But we dont know what... Please restart the programme.'

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

SpecialNameList = ['Strength','Perception','Endurance' ,'Charisma','Intellegence','Agility','Luck']
PointList = [1, 1, 1, 1, 1, 1, 1]
SpecialList = list(SpecialDict)

'''
def YesOrNoCheck(input):
    if input in YesCheck:
        return 'Yes'
    elif input in NoCheck:
        return 'No'
    elif input not in YesCheck or input not in NoCheck:
        return 'Invalid Input'
    else:
'''  

def WhatGame():
    print('What game are you playing? (3 = FO3, NV = New Vegas, 4 = FO4)')
    Game = str(input())
    Game = Game.upper()
    #print(Game) #DEBUG
    if Game not in GamesList:
        print(InvalidInput)
        WhatGame()
    elif Game in GamesList:
        Game = 'Fallout ' + Game
        print(('You chose {}, is this correct?' + YesOrNo).format(Game))
        UserConfirm = input().lower()
        if UserConfirm in YesCheck:
            GeneratePoints(Game)
        elif UserConfirm in NoCheck:
            WhatGame()
        elif UserConfirm not in YesCheck or input not in NoCheck:
            print(InvalidInput)
            WhatGame()
        else:
            print(UnknownError)

def GeneratePoints(Game): #, IsSeed, Seed): #when there was gonna be a seed for the RNG
    #MaxPoints = MaxPointsGamesDict[Game] never used
    #PointsAssigned = 0 never used
    for i in range(len(SpecialDict)):
        print('i = ' + str(i)) #DEBUG
        r = random.randrange(1,10)
        print(r) #DEBUG
        PointList[i] = r
        print('points list int', PointList) #DEBUG
    if sum(PointList) == MaxPointsGamesDict[Game]: #holy fuck a miricle, highly unlikely tho.    
        PrintPoints(PointList, Game)
    elif sum(PointList) > MaxPointsGamesDict[Game]: #bigger than, e.g. 35/28 used on FO4
        ChangePoints(PointList, Game)
    elif sum(PointList) < MaxPointsGamesDict[Game]:
        ChangePoints(PointList, Game)
    else:
        print(UnknownError)
    
def ChangePoints(PointList, Game): #changes the points if there are to many
    print('On ChangePoints()') #DEBUG
    if sum(PointList) > MaxPointsGamesDict[Game]: #chckes to see if thesum of the points is bigger than the max points for the game chosen
        print('On if sum > game')
        for i in range(len(PointList)): #might have to redo all of this 
            if sum(PointList) == MaxPointsGamesDict[Game]:
                PrintPoints(PointList)
            elif PointList[i] == 1:
                continue
            elif PointList[i] > 1:
                PointList[i] =- 1
            else:
                print(UnknownError)
        PrintPoints(PointList, Game)
    elif sum(PointList) == MaxPointsGamesDict[Game]: #if by some miracle the sum of the points is the max of the game chosen the points will be printed out
        PrintPoints(PointList)
    elif sum(PointList) < MaxPointsGamesDict[Game]: #checks to see if the sum of the points is smaller than the max points for the game chosen
        for i in range(len(PointList)): #might have to redo all of this 
            if sum(PointList) == MaxPointsGamesDict[Game]:
                PrintPoints(PointList)
            elif PointList[i] == 1:
                continue
            elif PointList[i] > 1:
                PointList[i] =+ 1
            else:
                print(UnknownError)
        PrintPoints(PointList, Game)
    else:
        print(UnknownError)
    

def PrintPoints(PointsList, Game):
    print('Points Used: ' + str(sum(PointsList)))
    for i in range(len(SpecialNameList)):
        SpecialDict[SpecialNameList[i]] = PointList[i]
        print(SpecialNameList[i] + ': ' + str(SpecialDict[SpecialNameList[i]]))
        #print('\n')
        
'''
def GetSeed(Game):
    IsSeed = False
    Seed = 0
    print('Do you want a seed for the random number generator? ' + YesOrNo + ' (A seed is a number that the random number generator uses make a number. If you use a seed, using that seed again will make you generate the same number)')
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
'''#i dont think a seed would work since it would create decimal numbers, so this is not going to be used.


    
    # for i in range(0, len(SpecialDict)):
    #     PointsToApply = random.randint()
    #     PointsLeft = PointsLeft - PointsToApply
    #     if i == 4:
            
        
        
    
#Just generate N random numbers, compute their sum, divide each one by the sum and multiply by M.
#list[] = 
    

WhatGame()