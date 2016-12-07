print('Type in the response you want, a list of prompts will be given')



def main():
    start=input('\nYou awaken in a darkened room. A light flickers:\n >go towards the light\n')
    if start.lower()=='go towards the light':
        print('\nYou walk towards it. It is blinding. It is... \nelectronic')
        street()
    else:
        print('\nyou decide to stay in the dark for a while longer')
        main()

inventory=[]
class Cufflinks():
    def __init__(self):
        self.name="Cufflinks"
        self.description="A pair of silver cufflinks, shaped like eyes"
    def describe(self):
        print(self.name+ ': '+self.description)


class Party():
    def __init__(self):
        self.name="Party hat"
        self.description="A faded party hat, it has a faint glow"
    def describe(self):
        print(self.name+ ': '+self.description)

class Gold():
    def __init__(self):
        self.name="Statuette"
        self.description="A small golden statue of a kneeling figure"
    def describe(self):
        print(self.name+ ': '+self.description)

def street():

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
            street()

    elif choice.lower() == 'look behind':
        print('look bbaaaahd')
        street()

    else:
        print('not an option')
        street()
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


symbols = {'p1': 0,'p2': 1,'p3': 0, 'p4': 1,'p5': 0}
def gameintro():
    print('you there. i need help. ')
    print('emerges form shadows ')
    print('no do not go. ')
    print('I know what you need, i see it ')
    print('\nget this blasted lock off of me and i will give it')
    words = input("\n>Why?\n:")
    print('\nwhy? are you blind my. hands. are. locked. simpleton. ')
    print('\nit does not matter how i got into this. all that matters is that we can make an exhange of services and goods')
    print('\nchange the all the X to O, a simple puzzle but one i am physically unable to do. *he jangles his chains*')
    print('\nSo you will help me yes?...\ngood.')


def alter(name):
    position = input('\n>1\n>2\n>3\n>4\n>5\n:')
    if position== '1':
        symbols['p2'] += 1

    elif position== '2':
        symbols['p1'] += 1
        symbols['p3'] += 1

    elif position== '3':
        symbols['p2'] += 1
        symbols['p4'] += 1

    elif position== '4':
        symbols['p3'] += 1
        symbols['p5'] += 1

    elif position== '5':
        symbols['p4'] += 1

    else:
        print('what are you doing. that is not a button. stop pressing that....\nStop.')



def check(name):
    for word, meaning in sorted(symbols.items()):
        if int(meaning)%2== True:
            print('X')
        else:
            print('O')

def unlock(name):
    temp=0
    for word, meaning in (symbols.items()):
        if meaning%2==0:
            temp+=1
        elif (meaning%2==0)==False:
            print('still here. still locked.')
            break
    if temp==5:
        print('\n*click*\n\"fantastic. took you long enough.\"\nhe sighs and rummages through his pockets.\n\n\"my thanks. your reward.\"')
        item2=Gold()
        inventory.append(item2)
        print('\nYou watch the man slink back into the inky dark of the alleyway and return to mainstreet')
        street()
    else:
        print('failure')
        print('*The lock has reset, try again*')
        game()

def game():
    decision = input('\n>press a button\n>check the lock\n>attempt to unlock\n:')
    if decision.lower() == 'press a button':
            alter('status')
            game()
    elif decision.lower() == 'check the lock':
        check('status')
        game()
    elif decision.lower() == 'attempt to unlock':
        unlock('status')
    else:
        print('not an option')
        game()

def guessintro():

    print('Hey there. you look like you\'re in need of something. I\'m bored, need some fun, lets play a game!\nsay, whats your name?')

def guess():
    import random
    myName = input()
    print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

    TRIES_ALLOWED = 6
    number = random.randint(1, 20)

    for tries in range(1,6):
        guess = int(input("Take a guess: "))

        if guess > number:
            print('Nope. That\'s too high. heh.')
        elif guess < number:
            print('Too low, too slow kiddo.')
        else:
            print('hahaha! you got it! My number was ' +str(number)+ ' Well a deals a deal and I\'ve had fun. Here\'s you prize!')
            item1=Party()
            inventory.append(item1)
            print('\nShe hums a catchy tune as she retreats into the club, the doors close and you return to mainstreet feeling oddly lightheaded')
            street()
    else:
        print('You\'re taking too long, The number I was thinking of was ' + str(number)+' bored now. Try me again later, bye. ')
        street()

def ending():
    print('The wind blows, this far uptown is much colder than the the rest of city, its heart it empty')
    whatnow=input('\n>walk towards the heart\n>leave\n:')

    if whatnow=='walk towards the heart':
          print('creey alter')
          if len(inventory)==3:
              print('woo ending you did it')
              break
          else:
              print('it is cold')
              leave=input('\n>leave\n:')


              if leave=='leave':
                    print('\nYou leave')
                    street()
              else:
                    print('not an option')
                    ending()


    elif whatnow=='leave':
          print('BACK TO MAINSTREET')
          street()
    else:
          print('not an option')
          ending()
main()
