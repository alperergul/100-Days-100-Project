from sklearn.metrics import SCORERS
from art import logo, vs
from dataset import data
import random


def game():
    print(logo)

    SCORE = 0
    while True:

        items = random.sample(data, 2)
        first_item = items[0]
        second_item = items[1]

        print(
            f"Compare A: {first_item['name']}, {first_item['description']}, from {first_item['country']} ")
        print(vs)
        print(
            f"Against B: {second_item['name']}, {second_item['description']}, from {second_item['country']} ")

        user_guess = input("Who was more follower? A or B: ").capitalize()

        if user_guess == "A" and first_item['follower_count'] > second_item['follower_count']:
            SCORE += 1
            print("You are right! go -> \n\n")
        elif user_guess == "B" and first_item['follower_count'] < second_item['follower_count']:
            print("You are right! go -> \n\n")
        else:
            print("Your score is " + str(SCORE) + "\n\n")

            print("You lose! \n\n")
            SCORE = 0


game()
