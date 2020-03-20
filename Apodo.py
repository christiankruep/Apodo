#Apodo.py
#By Christian Kruep

"""A false name generator"""
from __future__ import print_function
import random
import time

def main():
    """Chooses two names from the two seperated
       word banks and prints them to the command line."""
    first_bank = ('Gus', 'Enoch', 'Flo', 'Theoden', 'Pippin', 'Samwise',
                  'Loial', 'Gandalf', 'Matrim', 'Perrin', 'Randy', 'Bob',
                  'Theoden', 'Andrew', 'Arnie', 'Clunt', 'Kvothe', 
                  'Rincewind', 'Twoflower', 'Mort', 'Krom', 'Bravd',
                  'Deacon', 'Rand', 'Thom', 'Minipat', 'Wile E.')

    last_bank = ('Longfellow', 'De Smet', 'Cauthon', 'Al Thor', 'The Grey',
                 'Wizard', 'De Los Altos', 'Bell', 'Anglesmith', 'Del Gato',
                 'Underhill', 'Root', 'Bard', 'Barksdale',
                 'McNulty', 'Flagstaff', 'Guster', 'Coyote')

    print ('\nWelcome to Apodo')
    print ('State of the art false name generator')
    print ('Would you like generate a false name? y/n')
    response = input('-->')

    if response == 'y':
        while True:
            random_name = random.choice(first_bank) + ' ' + random.choice(last_bank)
            time.sleep(1)
            print('GENERATING NAME!')
            time.sleep(1)
            print('      BEEP!')
            time.sleep(1)
            print('BOP!')
            time.sleep(1)
            print('      BOINK!')
            time.sleep(1)
            print ('Your new falsname is... ' + random_name)
            response = input('Is this acceptable? y/n -->')
            if response == 'y':
                print ('Then you shall henceforth be known as '
                       + random_name)
                break
            else: 
                print('Alright we are doing this again')
        print ('Thank you for using the Apodo')

    else:
        print ('Then what are you doing here?.')
        print ('Goodbye!')

if __name__ == "__main__":
    main()
