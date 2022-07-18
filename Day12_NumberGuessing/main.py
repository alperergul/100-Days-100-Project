import art
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(answer, guess):
    if(answer == guess):
        return True
    else:
        return False


def set_difficulty():

    if(input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy"):
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(art.logo)

    print('Welcome to the Number Gussing Game!')
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    while True:
        user_guess = int(input("Type your guess: "))
        result = check_guess(answer, user_guess)

        if(result):
            print('You Win!')
            break
        else:
            print('Your guess is wrong.')
            turns -= 1
            if(turns > 0):
                if(user_guess < answer):
                    print(
                        f"You have {turns} attempt remaining to guess the number.")
                    print("Up!")
                else:
                    print(
                        f"You have {turns} attempt remaining to guess the number.")
                    print("Down!")
            else:
                print(
                    f"You have {turns} attempt remaining to guess the number.")
                print('Game Over!')
                break


game()
