from street import *
def guessintro():
    import random
    print('Hey there. you look like you\'re in need of something. I\'m bored, need some fun, lets play a game!\nsay, whats your name?')
    myName = input()
def guess():
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


class Party():
    def __init__(self):
        self.name="Party hat"
        self.description="A faded party hat, it has a faint glow"
    def describe(self):
        print(self.name+ ': '+self.description)
