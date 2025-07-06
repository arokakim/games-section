import random

def start_game():
    #initialise the game
    print("ROLL THE DICE TO START THE GAME")
    start=random.randint(0, 6)
    if start==6:
        print(f"Congrats on the 6. You may start the game!")
    else:
        print(f'You rolled a {start} and you need a 6 to begin. Try again')

    return start



def dice():
    """
    simulates a dice roll"""

    roll = random.randint(0, 6)
    print(f"You got a {roll}")


def game():
    has_started=False
    starting = 1
    current_position = 0
    home = 100

    while current_position<home:
        roll = dice()
        if not has_started:

            if roll:
                print(f"You rolled {roll}")
                starting = 1
                roll = dice()
                if roll:
                    current_position = starting + roll
                    print(f"You rolled a {roll} and moved to position {current_position}")
                else:
                    print("You rolled a 6 again, move 6 steps forward")
            else:
                print(f"You need a 6 to start the game and you rolled a {roll}. Try Again!")
                if current_position is not home:
                    print(f"You are at position {current_position}. Roll again!")
                else:
                    if current_position == home:
                        print("Congrats! You win the game!")

                    return current_position
game()