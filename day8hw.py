#WAP to create a game : 
#1. The game starts with a welcome message and instructions.
"""
The user types commands like start, stop, or help.
The program:
Starts or stops the car based on the user's input.
Checks if the car is already started or stopped and responds appropriately.
If the user types quit, the game exits.
For any other input, the program responds with a message saying it doesn't understand.
"""
print("Welcome to Car Game!.")
print("----------------------")
username=input("Enter Player Name : ")
print(f"<> Welcome to Car Game {username}. <>")
def game(usercmd):
    if usercmd=="Start":
        print("Start")
    elif usercmd=="Stop":
        print("Stop")