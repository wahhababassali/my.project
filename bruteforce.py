

import itertools
import string
import time

# Define the character set and target password
charset = string.ascii_lowercase
target = "dog"

# Record the start time and initialize attempts
start = time.time()
attempts = 0

# Generate all possible combinations of characters
for attempt in itertools.product(charset, repeat=len(target)):
    attempts += 1
    guess = ''.join(attempt)

    # Check if the guess matches the target
    if guess == target:
        print(f"Password found: {guess} in {attempts} tries and {time.time() - start:.2f} seconds!")
        break


