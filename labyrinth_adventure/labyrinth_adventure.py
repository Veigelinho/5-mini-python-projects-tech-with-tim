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
    print("Green Path")


def red_path():
    print ("Red Path")


def yellow_path():
    print("Yellow Path")
    print("""\nAt first you walk down a long corridor. Then you come a to a crossing with three paths.
You hear some pleasant café music playing from the left.
You hear two women laughing from the right.
You look foward and can see a yellow tree with glitter in the distance
""")
    input_correct = False
    while not input_correct:
        player_choice = input("Where do you go? Press l for left, r for right or s for straight. > ").lower()
        
        if player_choice not in ("l", "r", "s"):
            print("Invalid Choice.")
        
        else:
            input_correct = True
            if player_choice == "l":
                print("""\nYou follow the music. As you walk town the hall, the music get louder and louder" \
You walk around a corner and see a bright, round room, with a small table in the middle.
On the table, there is a radio, and a small box.
What do you first do? Turn off the radio? Or open the box?""")
                input_correct = False
                while not input_correct:
                    player_choice = input("Press r for radio or b for box. > ").lower()
                    if player_choice not in ("r", "b"):
                        print("Invalid Choice.")
                    else:
                        input_correct = True
                        pass # Add if statement for radio and box
            elif player_choice == "r":
                print("""\nThe laughter has spiked your interest. As you follow the path, you make a turn around the corner.
The laughter has suddenly stopped.
\nYou see a big forest in front of you, with thousands of animals you have never seen.                      
There is a small river and a boat on top of it. The river flows from right to left.
On the right, you see a huge waterfall, and a cave just behind it.
Do you take the boat to the left, or walk towards the cave?""")
                input_correct = False
                while not input_correct:
                    player_choice = input("Press b for boat or c for cave. > ").lower()
                    if player_choice not in ("b", "c"):
                        print("Invalid Choice.")
                    else:
                        input_correct = True
                        if player_choice == "b":
                            print("""\nYou enter the boat. You start going down the stream. For some reason, the boat gets faster and faster

You realize you are headed straight for a waterfall. It's to late. You fall down the waterfall and die.
""")
                            # Add game over function.
                        else:
                            print("\nYou start walking towards a waterfall. On the way there, you walk past a banana tree.")
                            player_choice = input("Do you take some bananas with you? Type y for yes or n for no. > ").lower()
                            input_correct = True
                            while not input_correct:
                                if player_choice not in ("y", "n"):
                                    print("Invalid Choice.")
                                
                                elif player_choice == "y":
                                    print("You took 5 bananas with you.")
                                
                            print("""\nAlright. You continue waking towards the cave. As you enter, the laughter suddenly begins again.
The waterfall gets more intense, shutting you inside the cave.
\nou have no choice but to continue walking. It is dark, but you can still see things clearly.
You come across a fork in the road. You look to the left and see a portal.
To your right, you can hear laughter. But you cannot see anything.
Where do you go?""")
                            input_correct = False
                            while not input_correct:
                                player_choice = input("Type p for portal or l for laughter. >")
                                if player_choice not in ("p", "l"):
                                    print("Invalid Choice.")
                                elif player_choice == "p":
                                    input_correct = True
                                    print("""You entered the portal.
.
.
.
""")
                                    black_path()
                                else:
                                    print("""\nYou continue walking towards the laughter.
But as you get closer, the laughter slowly turns into barking.
There are hundreds of Bulldogs. It's too late. They have already seen you.
\nThey start running towards you, and you have no chance. You die.""")
                                    # Add game over funtion.                           

            




def black_path():
    print("Black Path")


def purple_path():
    print("Purple Path")


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

