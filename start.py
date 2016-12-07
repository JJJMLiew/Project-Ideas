from street import *

print('Type in the response you want, a list of prompts will be given')



def main():
    start=input('\nYou awaken in a darkened room. A light flickers:\n >go towards the light\n')
    if start.lower()=='go towards the light':
        print('\nYou walk towards it. It is blinding. It is... \nelectronic')
        street()
    else:
        print('\nyou decide to stay in the dark for a while longer')
        main()


main()
