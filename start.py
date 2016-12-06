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
            print('still here. still locked.')
            break
    if temp==5:
        print('\n*click*\n\"fantastic. took you long enough.\"\nhe sighs and rummages through his pockets.\n\n\"my thanks. your reward.\"')
    else:
        print('failure')
        print('*The lock has reset, try again*')

def game(go):
    decision = input('\n>press a button\n>check the lock\n>attempt to unlock\n:')
    if decision.lower() == 'press a button':
            alter('status')
            game('play')
    elif decision.lower() == 'check the lock':
        check('status')
        game('play')
    elif decision.lower() == 'attempt to unlock':
        unlock('status')
    else:
        print('not an option')
        game('play')

game('play')
