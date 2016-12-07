from riddle import *
from game import *
from guess import *
from ending import *


def street():
    inventory=[]
    print("\n\n\nIt is nighttime, you see a long street lit in darknessaaegfgbnergrthsrteh ")
    print("\nAfter a glance around you notice a few things")
    choice = input('\n>go upstreet\n>head towards the noisy alleyway\n>step into the brightly lit building\n>walk into the nightclub\n>check your inventory\n>look behind\n:')
    if choice.lower() == 'go upstreet':
            print('\nYou head up the street')
            ending()

    elif choice.lower() == 'head towards the noisy alleyway':
        gameintro()
        game()

    elif choice.lower() == 'step into the brightly lit building':
        riddleintro()
        riddle()

    elif choice.lower() == 'walk into the nightclub':
        guessintro()
        guess()

    elif choice.lower() == 'other game':
        print('LINK #guess GAME')

    elif choice.lower() == 'check your inventory':

        if len(inventory)==0:
                print('\nYou carry nothing on you')
                street()
        else:
            for item in inventory:
                item.describe()

    elif choice.lower() == 'look behind':
        print('look bbaaaahd')
        street()

    else:
        print('not an option')
        street()
