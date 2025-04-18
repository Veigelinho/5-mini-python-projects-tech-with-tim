import random

is_integer = False

while not is_integer:
    top_of_range = input("Type a number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        is_integer = True
    else:
        print("That was not a number!")

random_number = random.randint(0, top_of_range)
times_guessed = 0

while True:
    guess = input(f"Guess a number between 1 and {top_of_range}: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number!")
        continue
    times_guessed += 1
    
    if guess == random_number:
        print(f"Congrats! You guessed {random_number} after {times_guessed} tries!")
        break
    
    elif guess > random_number:
        print("That was too high. Try again")
        
    else:
        print("That was too low. Try again")

    