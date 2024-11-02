import random
computer_action = random.choice(["Rock","Paper","scissors"])

while True:
    user_action = input("Enter your choice: ").lower()
    if computer_action == user_action:
        print("Both are selected same. So, it's Tie!")
    elif computer_action == "Rock":
        if user_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif computer_action == "Paper":
        if user_action == "Rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")              
    elif computer_action == "scissors":
        if user_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")          
    else:
        print("Invalid input, please enter rock, paper, or scissors.")        
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break        