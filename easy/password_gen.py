# Difficulty: I

import random
import string

length = int(input("How long should the password be? "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for i in range(length))
print(password)