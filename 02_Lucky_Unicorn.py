# lucky Unicorn Decomposition Step 3
# GEnerate a random token

# To do
# Set up starting amount
# choose 100 tokens (ie: play 100 rounds and...)
#   count # of unicorns and multiply 5
#   count # of horse / zebra and multiply by 0.5
#   count # of donkeys
#   work out total won / lost

import random

How_much = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

uni_count = 0
zebhor_count = 0
donkey_count = 0

for item in range(1,How_much):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        uni_count += 1
    elif chosen =="donkey":
        donkey_count += 1
    else:
        zebhor_count += 1

    print(chosen)

print("**** Win / Loss Calculation*****")
print("# Unicorns: {}".format(uni_count))
