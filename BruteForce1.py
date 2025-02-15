import random
import string
from datetime import datetime
# Importing all the necessary modules

password = input("Enter your password: ")
# Asking the user to enter their password

attempts = 0

possible_chars = ''.join(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits)
# Creating a string of all possible characters
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    # Starting an infinite loop
    guess = ''.join(random.choice(possible_chars) for _ in range(len(password)))
    # Generating a random password of the same length as the user's password
    attempts += 1
    print(f"Attempt {attempts}. Password: {guess}")
    # Incrementing the number of attempts
    if guess == password:
        print(f"Password found in {attempts} attempts at {current_time}")
        break
        # If the generated password matches the user's password, print the number of attempts and break th
    
    else:
        continue
        