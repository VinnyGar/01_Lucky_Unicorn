# Lucky Unicorn Decompose Step 2
# Generate a random token

import random

tokens = ["Horse", "Zebra", "Donkey", "Unicorn"]

for item in range(1,15):
    chosen = random.choice(tokens)
    print(chosen)
