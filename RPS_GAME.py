import random


def play_game():
    options = ["R", "P", "S"]

    CPU_choice = random.choice(options)

    valid = True

    while valid == True:
        your_option = input("Choose Letter Between R, P or S \n")
        if your_option not in options:
            print(f"Invlid Input Made, Kindly Choose Between the List {options}")
        
        if your_option == CPU_choice:
            print("You Tie")
            valid = True
            
        elif your_option == "S" and CPU_choice == "R":
            print(f"User({your_option}) : Computer({CPU_choice}) ")
            print("Rock Crushes Scissors, You Lost!")
            valid = True

        elif your_option == "R" and CPU_choice == "P":
            print(f"User({your_option}) : Computer({CPU_choice}) ")
            print("You Lost!")
            valid = True
            
        elif your_option == "P" and CPU_choice == "S":
            print(f"User({your_option}) : Computer({CPU_choice})")
            print("Paper Covers Rock, You Lost!")
            valid = True

        elif your_option == "R" and CPU_choice == "S":
            print(f"User({your_option}) : Computer({CPU_choice}) ")
            print("You Won!")
            valid = False
            
        elif your_option == "P" and CPU_choice == "R":
            print(f"User({your_option}) : Computer({CPU_choice})")
            print("You Won!")
            valid = False
            
        elif your_option == "S" and CPU_choice == "P":
            print(f"User({your_option}) : Computer({CPU_choice})")
            print("You Won!")
            valid = False

play_game()