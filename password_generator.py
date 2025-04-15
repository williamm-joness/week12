import string
import random

letter = 0
while letter < 12:
    print(random.choice(string.ascii_lowercase))
    letter += 1