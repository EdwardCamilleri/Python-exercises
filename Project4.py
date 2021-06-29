# taking user input for their name and their room measurements
name = input("What is your name? ")
Length = float(input("What is the length of the room?: "))
Width = float(input("What is the width of the room?: "))

# calculating the area from the measurements and displaying it to the user
Area = Length * Width
print("The Area of your room is " + str(Area) + " Meters squared.")


# loop to compare the users area against the area limit
maxarea = open("Area Limit.txt", "r").read()
if float(Area) > float(maxarea):
    print("Sorry this room size is too big and is not available.")
else:
    print("This room size is available.")

# writing the users name and room area to the log file
open("Area Logs.txt", "a").write(name + " " + str(Area) + " Meters Squared room" + "\n")


# loop to give user the option to change the area limit
config = input("Would you like to change the room area limit? (Y/N) ")
if config == "Y":
    open("Area Limit.txt", "w").write(input("please enter your new area limit"))
    # small message to close out the program and show the user that the interaction is over
    print("Area limit successfully changed, Have a nice day!")

elif config == "N":
    # small message to close out the program and show the user that the interaction is over
    print("All options exhausted, Have a nice day!")


