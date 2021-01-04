import random
import sys

def line_break():
    print("-" * 10)

def continue_game():
    """Ask player that want to continue playing or not"""
    while True:
        print("Continue or Not:")
        print("1. Continue")
        print("2. Quit")

        try:
            choice = int(input("> "))
        except:
            print("Enter only a number!!!")
            line_break()
            continue

        if choice == 1:
            break
        elif choice == 2:
            sys.exit(0)

def user_guess(range, life):
    """Computer random a number for user to guess."""
    random_number = random.randint(1, range)
    guess = 0
    life = life

    while guess != random_number and life > 0:
        if life > 1:
            print("You have {} lifes left".format(life))
        else:
            print("You have {} life left".format(life))

        try:
            guess = int(input("Guess a number between 1 and {}: ".format(range)))

        except:
            print("Enter only a number!!!")
            line_break()
            continue

        if guess > range:
            print("Enter only a number between 1 and {}!".format(range))
            line_break()
            continue

        if guess < random_number:
            print("Too low.")
            line_break()
            life -= 1
        elif guess > random_number:
            print("Too high.")
            line_break()
            life -= 1

    if guess == random_number:
        print("Congratulations!!! You have guessed correct number: {}".format(random_number))
    else:
        print("You lose!!! The correct number is {}".format(random_number))

    continue_game()

def select_life():
    """Select life time"""
    while True:
        print("Enter a number of life")

        try:
            life = int(input("> "))
        except:
            print("Enter only a number!!!")
            line_break()
            continue

        return life

def select_range():
    """Select number range"""
    while True:
        print("Enter number range to play")

        try:
            range = int(input("> "))
        except:
            print("Enter only a number!!!")
            line_break()
            continue

        return range

def select_mode():
    """Select game mode."""
    while True:
        print("Game Mode:")
        print("1. Let's I guess AI random number")
        print("2. Quit")

        try:
            mode = int(input("> "))
        except:
            print("Enter only a number!!!")
            line_break()
            continue

        if mode not in [1, 2]:
            print("Enter only 1 or 2!")
            line_break()
            continue

        if mode == 2:
            sys.exit(0)

        range = select_range()
        life = select_life()
        if mode == 1:
            user_guess(range, life)

def main():
    """main function of the game."""
    print("Welcome to Number Guessing Game!!!")
    select_mode()

if __name__ == "__main__":
    main()
