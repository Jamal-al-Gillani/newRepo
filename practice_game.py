import random


computer = random.choice([1,0,-1])
youString = input("Enter your choice : ")
youDict = {"s": 1,"w": -1, "g": 0}
reverseDict ={1 : "snake", -1 : "Water", 0 : "Gun"}
you = youDict[youString]

print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")


if (computer == you):
    print("It's a draw!")
else:
    if (computer ==-1 and you == 1):
        print("You win!")

    elif (computer ==-1 and you == 0):
        print("You Lose!")

    elif (computer ==-1 and you == -1):
        print("You Lose!")

    elif (computer ==1 and you == 0):
        print("You Win!")

    elif (computer ==0 and you == 1):
        print("You Lose!")
    
    else:
        print("Something went wrong!")