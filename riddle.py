from street import *
def riddleintro():
    print('\nLights dance as you enter the building. In a flash of light and smoke, a masked figure appears')
    print('\"Welcome one, welcome all. To my game of riddles three!\nYou need me, I need you. Lets get to it shall we?\"')

def riddle():
    print('\nMy first riddle is this:\nbutt \nWhat am I?')
    ans1='butt'
    ans2='elf'
    ans3='gah'


    guess = input("Take a guess: ")
    if guess.lower() == ans1:
        print('Congratulations! You\'ve done and solved it, onto the next one')
    else:
        print('incorrect. how sad.')
        riddle()


    print('riddle2')
    guess = input("Take a guess: ")
    if guess.lower() == ans2:
        print('congrats2')
    else:
        print('incorrect. how sad.')
        riddle()


    print('riddle3')
    guess = input("Take a guess: ")
    if guess.lower() == ans3:
        print('Great job ond ei donwb sf')
        item3=Cufflinks()
        inventory.append(item3)
        print('The lights dim as the figure fades out of view. You hear a small thump and notice a small box on the floor.\nYou pick it up and when look back up, you are back on mainstreet.\nHow mysterious')
        street()
    else:
        print('Soooooo close, try again later.')
        street()

class Cufflinks():
    def __init__(self):
        self.name="Cufflinks"
        self.description="A pair of silver cufflinks, shaped like eyes"
    def describe(self):
        print(self.name+ ': '+self.description)
