#Task : Python program Rock-Paper-Scissor Game.

import random

def game():
    while True:
        possible_choice = ["rock","paper","scissor"]
        user_choice = input("Enter your choice(rock,paper,scissor): ").lower()
        while user_choice not in possible_choice:
            user_choice = input("Invalid input. Enter your choice(rock,paper,scissor): ").lower()
        computer_choice = random.choice(possible_choice)
        print(f"\nYou chose :{user_choice} \n")
        print(f"\nComputer chose:{computer_choice} \n")

        if user_choice == computer_choice:
            print(f"Both chose {computer_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Paper beats rock! You lose!")
            else:
                print("Rock beats scissor! You win!")
        elif user_choice == "paper":
            if computer_choice == "scissor":
                print("Scissor beats paper! You lose!")
            else:
                print("Paper beats rock! You win!")
        elif user_choice == "scissor":
            if computer_choice == "rock":
                print("Rock beats Scissor! You lose!")
            else:
                print("Scissor beats paper! You win!")  

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes" , "no"]:
            play_again = input("Invalid input. Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    game()

