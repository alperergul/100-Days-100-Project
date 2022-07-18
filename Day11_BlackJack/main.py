############### Blackjack Project #####################

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from replit import clear
import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)


def check_ace(cards):
    if(cards.count(11) != 0):
        return True
    else:
        return False


def total_score(cards):
    total = 0
    for i in cards:
        total += i

    return total


def print_winner(user, computer):
    if(user > 21):
        if(computer <= 21):
            print('Computer win!')
        else:
            print('No winner!')
    elif(computer > 21):
        if (user <= 21):
            print('You win!')
        else:
            print('No winner!')
    elif(computer == 21 == user):
        print('No winner!')
    elif(computer < 21 and user < 21):
        if(computer > user):
            print('Computer win!')
        elif(user > computer):
            print('You win!')
        else:
            print('No winner!')


def play_game():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    while True:

        for i in range(0, 2):
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        user_score = total_score(user_cards)
        computer_score = total_score(computer_cards)

        if(user_score == 21 or computer_score == 21):
            print_winner(user_score, computer_score)
            break

        while True:
            user_answer = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if(user_answer == 'y'):
                user_cards.append(random.choice(cards))
                user_score = total_score(user_cards)

                print(f"Your cards: {user_cards}")
                if(user_score > 21):
                    if(check_ace(user_cards)):
                        for i in range(0, len(user_cards)):
                            if (user_cards[i] == 11):
                                user_cards[i] = 1
                        user_score = total_score(user_cards)

                    if user_score > 21:
                        user_answer = 'n'

            if(user_answer == 'n'):
                while computer_score <= 16:
                    computer_cards.append(random.choice(cards))
                    computer_score = total_score(computer_cards)
                print(f"Computer Cards: {computer_cards}")
                print(f"Your Score: {user_score}")
                print(f"Computer Score: {computer_score}")
                print_winner(user_score, computer_score)
                break

        break


while True:

    status = input("Do you want to play Black Jack? Type 'y' or 'n'")

    if(status == 'y'):
        clear()
        play_game()
    else:
        break
