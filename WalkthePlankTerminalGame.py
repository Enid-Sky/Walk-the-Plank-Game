import random
import time

intro = (

    """
                                                     , _                       
 (|  |  |_/  _,   |\  |)      _|_  |)     _     /|/ \ |\   _,          |)  
  |  |  |   / |   |/  |/)      |   |/\   |/      |__/ |/  / |   /|/|   |/) 
   \/ \/    \/|_/ |_/ | \/     |_/ |  |/ |_/     |    |_/ \/|_/  | |_/ | \/
                                                                                                                                               

                                                                           


 ___________________________________________________________________
||     *                            *                         *  ||
||        *                 *                *                   ||
||                ___.                          *          *     ||
||       *    ___.\__|.__.           *                           ||
||            \__|. .| \_|.                                      ||
||            . X|___|___| .                         *           ||
||          .__/_||____ ||__.            *                /\     ||
||  *     .  |/|____ |_\|_ |/ _                          /  \    ||
||        \ _/ |_X__\|_  |\||~,~{                       /    \   ||
||         \/\ |/|    |_ |/:|`X'{                   _ _/      \__||
||          \ \/ |___ |_\|_.|~~~                   /    . .. . ..||
||         _|X/\ |___\|_ :| |_.                  - .......... . .||
||         | __\_:____ |  ||o-|            ___/........ . . .. ..||
||         |/_-|-_|__ \|_ |/--|       ____/  . . .. . . .. ... . ||
|| ........:| -|- o-o\_:_\|o-/:....../...........................||
|| ._._._._._\=\====o==o==o=/:.._._._._._._._._._._._._._._._._._||
|| _._._._._._\_\ ._._._._.:._._._._._._._._._._._._._.__._._._._||
|| ._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._||
||---------------------------------------------------------------||
                                            



""")

plank = [

    """
Take a step forward!

             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____   * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """
Another step forward!

             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____     * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^  
""",
    """
Getting nervous are you? 

             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____       * 
        \                   /=================== 
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """
I hope you know how to swim!
    
             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____         * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """
There's no turning back soon...
        
             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____           * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """

Getting awfully close to the edge!
    
             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____           * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """
Give it your best guess next time!
    
             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____             * 
        \                   /================== 
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """
That's the best you can do? 
        
             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____               * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ 
""",
    """
Any last words? 

             |    |    |                 
            )_)  )_)  )_)              
            )___))___))___)            
        )____)____)_____)  
        _____|____|____|____                 * 
        \                   /==================  
    ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    """,
    """

YOU ARE SHARKBAIT
                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_             
      \                         /// a  `~.___________
      / /~~~~-, ,__.    ,      ///  __,,,,)      o ' |   
      \/      \/    `~~~;   ,---~~-_`~---\ \----\-o--'  
                       /   /            / /
                      '._.'           _/_/
                                      ';|\   
    """]

parrot = ("""

        __,---.
       /__|o\  ) 
        `-\ / /
          ,) (,
         //   \\
        {(     )}
  =======""===""===============
          |||||
           |||
            |

        """)


def introduction():
    """Print game intro"""

    print(intro)
    time.sleep(2)
    print("Loading game...")
    time.sleep(4)
    print("\n\nARRRRRR!!!\nYou were captured by pirates! \nThe crew is ready to see you walk the plank! \nLucky for you, if there is something Captain Morgan likes \nmore than rum, it's a good game. \n\nGuess the name of Captain Morgan's parrot \nand you won't have to sleep with the fishies. \n\nBEWARE: Every wrong letter inches you closer to your doom!")


introduction()


def choose_to_play():
    while True:
        """asks player if they would like to play"""

        print("\nWould you like to play Walk the Plank?\n[A]ye or [N]ay\n")
        player_decision = input("> ").lower()

        if player_decision == "a":
            break
        elif player_decision == "n":
            print(
                "Too bad for you pirates don't take no for an answer. Start guessing!\n")
            break
        else:
            print("What was that, mate? We asked...")


choose_to_play()


def game_play(plank):
    """Main game play"""
    list_of_names = ["polly", "crackers", "jose", "jack"]
    parrot_name = random.choice(list_of_names)
    player_guess = ""
    display_word = []  # list stores display word
    attempts = 10

    for letter in parrot_name:
        """replace letters to hide name from player"""
        display_word.append(" * ")

    while (attempts > 0 and " * " in display_word):
        """While there are still attempts and letters to guess, get player guess"""
        joined_word = "".join(
            display_word)  # returns the string concatenated with the elements of an iterable

        print("His name is:  {}".format(joined_word))
        print("\nChoose a letter: ")
        player_guess = input("")
        player_guess = player_guess.lower()

        for letter in range(len(parrot_name)):
            """ Iterates over each character in parrot's name checking for a match"""
            if player_guess == parrot_name[letter]:
                # replace all letters in bird name that match the players guess
                display_word[letter] = player_guess

        if player_guess not in parrot_name:
            """Wrong guess deducts attempt by one, and displays corresponding plank image"""
            attempts = attempts - 1

            print("\nIncorrect! Attempts remaining: {}".format(attempts))
            # decrements element in list by attempts made
            print(plank[(len(plank) - 1) - attempts])

    if " * " not in display_word:
        """No blanks remaining triggers a win"""

        print("\nAye, mate, you guessed correctly!")
        print(parrot)
        print("\nNow give {} a cracker and live for another day!".format(parrot_name))

    else:
        """Loop ends because attempts reached 0"""
        time.sleep(3)

        print(parrot)
        print("\n{} the parrot wins!".format(parrot_name))


game_play(plank)


def play_again():

    print("\nWould you like to play again? [A]ye or [N]ay]\n")
    continue_game = input("> ").lower()
    if continue_game == "a":
        game_play(plank)

    elif continue_game == "n":
        print("Goodbye!")

    else:
        print("what was that, mate? [A]ye or [N]ay?")


play_again()
