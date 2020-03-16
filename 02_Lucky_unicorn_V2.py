# Lucky Unicorn Decomposition Step 3
# Generate a random token

# To do
# Set up starting amount
# choose 100 tokens (ie: play 100 rounds and...)
#   count # of unicorns and multiply 5
#   count # of horse / zebra and multiply by 0.5
#   count # of donkeys
#   work out total won / lost

import random

How_much = 100
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey",
          "unicorn"]

uni_count = 0
zebhor_count = 0
donkey_count = 0

for item in range(0,How_much):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        uni_count += 1
    elif chosen =="donkey":
        donkey_count += 1
    else:
        zebhor_count += 1

    print(chosen)

# Money calculations
winnings = uni_count * 5 + zebhor_count * 0.5

print("**** Win / Loss Calculation*****")
print("# Unicorns: {}".format(uni_count))
print("# Zebra and Horses: {}".format(zebhor_count))
print("# Donkey: {}".format(donkey_count))

print()
print("You spent ${}".format(How_much))
print("You go home with ${:.2f}".format(winnings))