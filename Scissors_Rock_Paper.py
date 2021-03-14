import random

# paper covers rock
# scissors cut paper
# rock smash scissors
num1, num, hen = 0, 0, 0
hands = ["scissors", "rock", "paper"]
while True:
    hen += 1
    hand = input("Scissors, Rock and Paper")
    n = random.randint(0, 2)
    comphand = hands[n]
    if hand.lower() == comphand:
        print("Tie")
    elif hand.lower() == "paper" and comphand == "rock":
        print("Win, Paper covers Rock")
        num += 1
    elif hand.lower() == "paper" and comphand == "scissors":
        print("Lost, Scissors cut Paper")
        num1 += 1
    elif comphand == "paper" and hand.lower() == "rock":
        print("The Pc wins, Paper covers Rock")
        num1 += 1
    elif comphand == "paper" and hand.lower() == "scissors":
        print("You wins, Scissors cut Paper")
        num += 1
    elif hand.lower() == "scissors" and comphand == "rock":
        print("You Lost, Rock smash Scissors")
        num1 += 1
    elif hand.lower() == "scissors" and comphand == "paper":
        print("You win, Scissors cut Paper")
        num += 1
    elif comphand == "scissors" and hand.lower() == "rock":
        print("Pc Wins, Rock smash scissors")
        num1 += 1
    elif comphand == "scissors" and hand.lower() == "paper":
        print("Pc Lost, Scissors cut Paper")
        num += 1
    elif hand.lower() == "rock" and comphand == "scissors":
        print("You win, Rock smash scissors")
        num += 1
    elif hand.lower() == "rock" and comphand == "paper":
        print("You lost, Paper covers Rock")
        num1 += 1
    elif comphand == "rock" and hand.lower() == "scissors":
        print("Pc Wins, Paper covers Rock")
        num1 += 1
    elif comphand == "rock" and hand.lower() == "paper":
        print("Pc Lost, Scissors cut Paper")
        num += 1
    else:
        print("Enter a hand...")

    if hen >= 11:
        if num == num1:
            print("Tie\n")
            print("Total:", "You", num, "Pc: ", num1)
        elif num > num1:
            print("You win,", num, "point over", num1, )
            break
        elif num1 > num:
            print("Pc wins,", num1, "point over", num, )
            break
    else:
        pass

# print("The Pc's earned", num1, "point")
# print("You've earned", num, "point")
