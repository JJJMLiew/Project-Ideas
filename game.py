from street import *

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
        street('go')
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


class Gold():
    def __init__(self):
        self.name="Statuette"
        self.description="A small golden statue of a kneeling figure"
    def describe(self):
        print(self.name+ ': '+self.description)
