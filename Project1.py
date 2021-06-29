# taking input from the user, take their name and the amount in this transaction
name = input("Please enter your name")
money = float(input("Please enter an amount in £"))

# target, reads the spend limit from the amount file
target = float(open("Spend Limit.txt", "r").read())

# f, opens the log file in append mode
f = open("Transaction Logs.txt", "a")

# a, opens the amount file (spend limit file) in write mode
a = open("Spend Limit.txt", "w")

PIN = 1234

# This loop checks if the amount entered is above or below the user's spend limit and asks for their pin number if it is above
if money <= target:
    print("Amount entered is less than your no pin limit, pin is not required and transaction is successful")
elif money > target:
    pin1 = input("Transaction is above your no pin limit, please enter your pin")
    while PIN != int(pin1):
        print("Incorrect pin please try again")
        pin1 = input("Please enter your pin")
    else:
        print("Transaction successful")

# writing the details of the transaction to the log file
f.write(str(name) + " £" + str(money) + "\n") # writing the details of the transaction to the log file
f.close()


# This is a loop that allows the user to change their spend limit

config = input("Would you like to change you no pin spend limit? (Y/N)")
if config == "Y":
    a.write(input("please enter your new spend limit in £")) # takes and writes the new input to the amount file

    # small message to close out the program and show the user that the interaction is over
    print("Spend limit changed, Have a nice day!")

elif config == "N":

    # small message to close out the program and show the user that the interaction is over
    print("All actions exhausted, have a nice day!")


