# Lucky Unicorn payment mechanic

# To do
# Assume starting amount is $10
# Allow manual token input for testing purposes
# Adjust total correctly for a given token
#   - if it's a Unicorn = +5
#   - if it's a Donkey = -1
#   - if it's a Zebra / Horse = -0.5
# Give user feedback based on winnings...
# State new total

# Assume starting amount is $10
total = 10

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

