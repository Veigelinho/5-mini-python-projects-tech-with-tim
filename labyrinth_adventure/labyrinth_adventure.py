introduction_message = """This mysterious labyrinth holds the most precious and
valuable diamond the world has ever seen.

It was stolen by an unknown gang decades ago, and many people have
attempted to find the diamond here.

No one ever came back out of this labyrinth...

Do you want to enter it? Y/N"""

starting_message = """Welcome to the mysterious labyrinth!
At any point of the game, press q to quit the game."""

staging_area_message = """You are in the staging area.
There are 5 paths to choose from.

Press R for the Red Path of Fire
Press G for the Green Path of Poison
Press Y for the Yellow Path of Deception
Press B for the Black Path of Death
Press P for the Purple Path of Mushrooms"""

def staging_area():
    print(staging_area_message)
    path_choice = input("> ").lower()
    
    if path_choice not in ["r", "g", "y", "b", "p"]:
        print("Invalid Entry.")
        staging_area()
    else:
        
        play(path_choice)


def play(path_choice):
    
    if path_choice == "r":
        red_path()
    
    elif (path_choice) == "g":
        green_path()

    elif (path_choice) == "y":
        yellow_path()

    elif (path_choice) == "b":
        black_path()
    
    else:
        purple_path()
    


def green_path():
    print("green path")


def red_path():
    print ("red path")


def yellow_path():
    print("yellow path")


def black_path():
    print("black path")


def purple_path():
    print("purple path")


wants_to_play = False

while not wants_to_play:
    print(introduction_message)
    player_choice = input("> ").lower()
    
    if player_choice == "y":
        wants_to_play = True
        player_health_level = 100
        staging_area()
    
    elif player_choice == "n":
        print("Bummer. See you next time...")
        print(f"""\n\"It is not death that a man should fear,
but he should fear never beginning to live\"        ~ Marcus Aurelius
""")
        break
    
    else:
        print("Invalid entry. Please type Y for Yes or N for No")

