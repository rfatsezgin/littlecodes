import random

user_wins = 0
computer_wins = 0

options = ["Rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Bilgisayar ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Sen Kazandın! ")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Sen Kazandın! ")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Sen Kazandın! ")
        user_wins += 1
    
    else:
        print("Bilgisayar Kazandı! ")
        computer_wins += 1

print("Sen Kazandın", user_wins, "times.")
print("Bilgisayar Kazandı", computer_wins, "times.")
print("Bye Bye Kaç Bakalım EZİK")

if user_input == "taş" and computer_pick == "makas":
        print("Sen Kazandın! ")
        user_wins += 1

    elif user_input == "kağıt" and computer_pick == "taş":
        print("Sen Kazandın! ")
        user_wins += 1


    elif user_input == "makas" and computer_pick == "gağıt":
        print("Sen Kazandın! ")
        user_wins += 1
    
    else:
        print("Bilgisayar Kazandı! ")
        computer_wins += 1
    with open   

    if user_input == "taş" and computer_pick == "makas":
        print("Sen Kazandın! ")
        user_wins += 1

    elif user_input == kağıt" and computer_pick == "taş":
        print("Sen Kazandın! ")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Sen Kazandın! ")
        user_wins += 1
    
    else:
        print("Bilgisayar Kazandı! ")
        computer_wins += 1

print("sen kazandın")
print("computer win", else, + ("computer_pic"))