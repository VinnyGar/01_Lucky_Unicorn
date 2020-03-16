# Lucky Unicorn payment mechanic

# To do
# Ask user how much they have to play with
# If total is less than $1, quit
# If total is more than $1, ask user if they want to play again

# Assume starting amount is $10
total = int(input("How much would you like to play with? "))

keep_going = ""
while keep_going =="":

    # Allow manual token input for testing purposes
    token = input("Enter a token: ")

    # Adjust total correctly for a given token
    if token == "unicorn":
        total += 5
        feedback = "you wont $5! "
    elif token == "Donkey":
        total -= 1
        feedback = "Sorry! you lost $1 "
    else:
        total -= 0.5
        feedback = "Sorry! you lost 50 cents "

    print()

    print(feedback)
    print("You have {} left to play with".format(total))

    if total < 1:
        print ("Sorry! you don't have any more money to play with. Gamer over! ")
        keep_going = "end"
    else:
        keep_going = input ("Press <ENTER> to continue or any key to quit. ")

print("Thank you for playing. ")


