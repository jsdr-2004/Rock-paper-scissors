import random
uc = input("enter your choice('rock','paper','scissors')")
pc = ['rock','paper','scissors']
cc = random.choice(pc)
print(f"your choice is {uc},computer's choice is {cc}")
if uc == cc:
    print(f"Both players selected {uc}. It's a tie!")
elif uc == "rock":
    if cc == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif uc == "paper":
    if cc == "rock":
        print(" You win!")
    else:
        print(" You lose.")
elif uc == "scissors":
    if cc == "paper":
        print("You win!")
    else:
        print("You lose.")
