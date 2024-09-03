from art import logo, vs
from game_data import data
import random


# Function to generate a random index
def give_index():
    return random.randint(0, len(data)-1)


# Function to compare follower counts of two indices
def compare_follower_count(compare, against):
    return 'A' if data[compare]['follower_count'] > data[against]['follower_count'] else 'B'


# Function to display the current comparison data
def display_comparison(compare_index, against_index):
    print(
        f"Compare A: {data[compare_index]['name']}, {data[compare_index]['description']}, from {data[compare_index]['country']}.")
    print(vs)
    print(
        f"Against B: {data[against_index]['name']}, {data[against_index]['description']}, from {data[against_index]['country']}.\n")


# Function to validate the user's answer
def validate_answer(compare_index, against_index):
    while True:
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer in ['A', 'B']:
            return answer == compare_follower_count(compare_index, against_index)
        else:
            print("Invalid input. Please type 'A' or 'B'.")


# Main game loop
def play_game():
    score = 0
    compare_index = give_index()
    against_index = give_index()

    # Ensure indices are not the same
    while against_index == compare_index:
        against_index = give_index()

    while True:
        print(logo)

        # Display the current score if it's greater than 0
        if score > 0:
            print(f"You're right! Current score: {score}.\n")

        # Display the comparison data for "A" and "B"
        display_comparison(compare_index, against_index)

        # Validate the user's guess
        if validate_answer(compare_index, against_index):
            compare_index = against_index
            against_index = give_index()
            score += 1
        else:
            break

    # Final score display
    print("\n" * 20)
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


# Start the game
play_game()
