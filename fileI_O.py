import os
import random

# with open ("file.txt", "w") as file:
#     file.write("hi this is new file ")
# print("file.txt is created")

# original_file= "file.md"

# new_file = "file.txt"
# os.rename(original_file,new_file)

# print(f"{original_file} name has been changed to {new_file}")
# file = 'file.txt'
# with open ('file.txt', 'w') as file:
#     pass

# if (file == " "):
#     print("Cleaned")
# else:
#     with open ('file.txt','r') as file:
#         file= file.read()
#         print("this is the content")



def game():
    print("You are playing the game . . . ")
    score = random.randint(1,6)

    with open ('file.txt') as f:
        highScore = f.read()
        if (highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0

    print(f"your Score: {score}")
    if (score>highScore):
        with open ('file.txt', 'w') as f:
            f.write(str(score))
    return score


game()
