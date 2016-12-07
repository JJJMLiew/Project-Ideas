
from street import *
def ending():
    print('The wind blows, this far uptown is much colder than the the rest of city, its heart it empty')
    whatnow=input('\n>walk towards the heart\n>leave\n:')

    if whatnow=='walk towards the heart':
          print('creey alter')
          if len(inventory)==3:
              print('woo ending you did it')
          else:
              print('it is cold')
              leave=input('\n>leave')


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
