print('Type in the response you want, a list of prompts will be given')
def main():
    start=input('\nYou awaken in a darkened room. A light flickers:\n >go towards the light\n')
    if start.lower()=='go towards the light':
        print('\n\n\nYou walk towards it. It is blinding. It is... \n\nelectronic')
        print('\n\n\n\nYou grasp the glowstick-candle object and press a button on the side\nThe object brightens and you see that you are not in a cave but rather a room')
        print('You see a door\nYou open it\nBeyond is a city, a dark endless vast metropolis far as the eye can see, with infinitely tall skyscrapers with aspects from every culture')
        print('You stand there for a moment, shocked by the landscape before your eyes instinctually snap to the view before you.\n\nMainstreet')
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
    input('\nPress enter:\n')
    print("\n\n\nIt is night in the city and mainstreet stretches before you.\nThe long street is lit in the darkness by neon light, lamps, torches, any and every possible lightsource")
    print('All held by people in a all sorts of clothing and styles as they walk about, talking, singing, laughing, \nor just going about as stars swirl ahead above and the moon glows')
    print("\n\n\n\nAfter a glance around you notice a few things:")
    print('\n\nNot far to your left is a alleyway, oddly dark in comparaison to the lights.\nYou hear an odd scraping noise and other soft sounds.\nIt looks damp too.')
    print('\n\nFloodlights cut through the black sky as they frame a thin building not far off to the side.\nThe very very big sign with blinking arrows pointing to it reads:\"How much do YOU know?\"\nIt looks... interesting')
    print('\n\nA massive building dominates a full block of street, even this far you can see the strobing lights and the booming music that thumps a soild beat.\nClearly a nightclub')
    print('\n\nFar far down at the very end of the street it is oddly dark.\nAt the end you only see the dark rise of a hill that seems to sprout above the rest')
    choice = input('\n\n\n\n>go far downstreet\n>head towards the dark alleyway\n>step into the brightly lit building\n>walk into the nightclub\n>check your inventory\n>look behind\n:')
    if choice.lower() == 'go far downstreet':
            print('\nYou head down the street')
            ending()

    elif choice.lower() == 'head towards the dark alleyway':
        gameintroPT1()
        gameintroPT2()
        game()

    elif choice.lower() == 'step into the brightly lit building':
        riddleintroPT1()
        riddleintroPT2()
        riddle()

    elif choice.lower() == 'walk into the nightclub':
        guessintroPT1()
        guessintroPT2()
        guess()

    elif choice.lower() == 'other game':
        print('LINK #guess GAME')

    elif choice.lower() == 'check your inventory':

        if len(inventory)==0:
                print('\n\nYou carry nothing on you')
                street()
        else:
            for item in inventory:
                item.describe()
            street()

    elif choice.lower() == 'look behind':
        print('\nYou look behind you. The building you were in is mirrored to your left and right. Simple small structures with no windows and only a door.\nYou try the handle. It is locked')
        street()

    else:
        print('\n\nnot an option')
        street()


def riddleintroPT1():
    for item in inventory:
        if item.name == 'Cufflinks':
            print('\nThe structure is dark, and the door locked. A sign hanging says \"we are closed! Thanks for playing our riddles 3!\"')
            Rchoice=input('\n>leave\n:')
            if Rchoice=='leave':
                street()
            else:
                print('You leave regardless')
                street()
        else:
            node=0
def riddleintroPT2():
    print('\nLights dance as you enter the building. In a flash of light and smoke, a masked figure appears before you.')
    print('\"Welcome one, welcome all. To my game of riddles three!\"  Fanfare follows as trumpets blare and confetti rains from the darkness above\n\"We\'re here because You need me and I need you. Lets get to the punch then shall we? After all, we have no choice\" A bright light shines into your face as the figure points their cane at you')
def riddle():
    print('\nMy first riddle is this:\nWhat goes on four feet in the morning, two feet at noon, and three feet in the evening? \nWhat am I?')
    ans1='man'
    ans2='nothing'
    ans3='e'


    guess = input("\nTake a guess:")
    if guess.lower() == ans1:
        print('\n\n\n\n\nCongratulations! You\'ve done and solved it.\nEasy is as easy does, a well known riddle!\nonto the next one! It\'s harder, I promise.')
    else:
        print('incorrect. how sad. Bye')
        street()


    print('\n\n\n\nWhat is greater than God,\nmore evil than the devil,\nthe poor have it,\nthe rich need it,\nand if you eat it, you\'ll die?')
    guess = input("\nTake a guess:")
    if guess.lower() == ans2:
        print('\n\n\n\n\n"Haha! correct! The answer was \'nothing\'!\"\n\"Two out of three done, onto the final riddle now! It will be the hardest yet!\"')
    else:
        print('incorrect. how sad. Bye')
        street()


    print('\n\n\nI am the first on Earth, the second in Heaven.\nI appear two times in a week yet you can only see me once in a year.')
    print('\nAlthough I am in the middle of the sea, I am not found in a month, but still make an appearance in February, June, September, October, November & December.')
    print('\nI am the beginning of the end, the end of every place.\nI am the beginning of eternity, the end of time and space.\nWhat am I?')
    guess = input("\nTake a guess:")
    if guess.lower() == ans3:
        print('\n\nExcellent, just excellent! Isn\'t it wonderful! The letter e, haha!\n\nWell here is your prize. I hope you\'ve had fun! Goodbye and goodnight')
        item3=Cufflinks()
        inventory.append(item3)
        print('\n\n\nThe lights dim as the figure fades out of view. You hear a small thump and notice a small box on the floor.\nYou pick it up and when look back up, you are back on mainstreet.\nHow mysterious')
        street()
    else:
        print('Soooooo close, try again later.\n You are forcibly ejected')
        street()



def gameintroPT1():
    for item in inventory:
        if item.name == 'Statuette':
            print('\nThe alleyway is dark and damp. There is nothing going on here. Yet the feel of eyes here makes the back of your neck shiver')
            Gchoice=input('\n>leave\n:')
            if Gchoice=='leave':
                street()
            else:
                print('You leave regardless')
                street()
        else:
            node=0
def gameintroPT2():
    print('\n\n\nYou enter the dark alley. Shadows lean around and you peer into the shadows where you could swear that that bag looks like a-\n\"you there. i need help.\" ')
    print('\n\nA figure emerges form shadows as you jerk back and unconsciously take a step back')
    print('\"no do not go.\" he says as you notice his arms. They are trapped in some odd device with buttons that have symbols down the middle')
    print('\n\"i know what you need, i see it in your eyes\"\n\"...\"')
    print('\n\"look. if you get this blasted lock off of me, i will give something good. something...of my spoils. but first i need your help\"')
    words = input("\n>Why?\n\n:")
    print('\n\"why? are you blind my. hands. are. locked.\"\n\"simpleton.\"')
    print('\n\"it does not matter how i got into this. all that matters is that we can make an exhange of services and goods\"')
    print('\n\"you need to change the all the X\'s to O\'s, a simple puzzle but one i am physically unable to do.\" *he jangles his chains*')
    print('\n\"So you will help me yes?...\"\n\ngood.')

symbols = {'p1': 0,'p2': 1,'p3': 0, 'p4': 1,'p5': 0}
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
            print('\n\n\"still here. still locked.\"')
            break
    if temp==5:
        print('\n*click*\n\"fantastic. took you long enough.\"\nhe sighs and rummages through his pockets.\n\n\"my thanks. your reward.\"')
        item2=Gold()
        inventory.append(item2)
        print('\nYou watch the man slink back into the inky dark of the alleyway and return to mainstreet')
        street()
    else:
        print('failure')
        print('*Try again*')
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


def guessintroPT1():
        for item in inventory:
            if item.name == 'Party hat':
                print('\nThe club throbs with sound and light, you see bodies and shadows undulating to the music but you find nothing of interest')
                Uchoice=input('\n>leave\n:')
                if Uchoice=='leave':
                    street()
                else:
                    print('You leave regardless')
                    street()
            else:
                node=0
def guessintroPT2():
    print('\n\nA woman in a slinky outfit stumbles out as you go to enter. She holds a drink of some sort in one hand and a kazoo in the other')
    print('Her colorful costume catches your eye as she catches yours.\n\"Hey there. you look like you\'re in need of something! I\'m bored, need some fun, soooo, lets play a game!')
    print('\"shhhhh. SayNoMore. \nSay. Whats your name?\"')
def guess():
    import random
    myName = input()
    print('\n\n\n\"Well, ' + myName + ', We are going to play the numbers game. I am going to pick a random number and you have get it fast enough before I get bored\"')
    print('\"I\ll say if you\'re too high or low. If you get it fast enough you get a prize!\nSo.\nI am thinking of a number between 1 and 20.\"\n\"Go. Guess.\" ')

    TRIES_ALLOWED = 6
    number = random.randint(1, 20)

    for tries in range(1,6):
        guess = int(input("Take a guess:"))

        if guess > number:
            print('Nope. That\'s too high. heh.')
        elif guess < number:
            print('Too low, too slow kiddo.')
        else:
            print('\"hahaha! you got it! My number was ' +str(number)+ '\"\n\"Well a deals a deal and I\'ve had fun. Here\'s you prize!\"')
            item1=Party()
            inventory.append(item1)
            print('She leans in close and hands you something like it was a secret')
            print('\nA catchy tune escapes her lips as she retreats, pleased with her fun, into the club.\nThe doors close and you return to mainstreet feeling oddly lightheaded')
            street()
    else:
        print('\"You\'re taking too long, The number I was thinking of was ' + str(number)+' bored now. Try me again later, bye.\nShe twirls on her foot and returns to the club and you return to mainstreet\"')
        street()



def ending():
    print('The wind blows.\nThis far downtown is much colder than the the rest of city. There are no lights and apart from the one you hold')
    print('\n\nThe lights and sounds of mainstreet face far far behind you. You walk up the winding path to the hill where a single pitch-black ediface stands.\nIt\'s surface seems to absorb even the starlight above')
    print('Ahead is the center of the city.\nLooking behind and around you see the massive sprawl of this endless city, patches of light and darkness with billions of people')
    print('You face the struture. What do you do now?')
    whatnow=input('\n\n>walk towards the heart\n>leave\n:')

    if whatnow=='walk towards the heart':
          print('The dark heart of the city only has a single raised dais.\nEmpty yet you feel the urge, the need to do something')
          if len(inventory)==3:
              input('\nPress enter:\n')
              print('\n\n\nYou place the objects that you have collected over your journey. Odd, unconnected things that are from everywhere.')
              print('\"They represent the city.\" You hear, suddenly in your head.')
              input('\nPress enter:\n')
              print('\nSpinning about your eyes dart around looking for the voice.\nYet the room is still empty.\n\nYour head turns to the window where suddenly you see the smallest sliver of light peaking from beyond the horizon')
              input('\nPress enter:\n')
              print('\n\nDaytime is coming to the city.\nThe light rolls in faster and faster as it hits and envelops you in blinding light')
              print('\n\n\n\n You have reached the end.\n\nThanks for playing my game! (or watching me present it at least)\nSpecial thanks to Dr.Bochanski for teaching the class and letting us have fun!')
              import sys
              sys.exit
              sys.exit()
          else:
              print('it is cold. You are lacking in something. Some things. You can feel it.')
              leave=input('\n>leave\n:')


              if leave=='leave':
                    print('\nYou leave')
                    street()
              else:
                    print('not an option')
                    ending()


    elif whatnow=='leave':
          print('You go back to mainstreet')
          street()
    else:
          print('not an option')
          ending()



main()
