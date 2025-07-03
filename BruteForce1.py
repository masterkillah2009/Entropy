import random
import string
from datetime import datetime
# Importing all the necessary modules

password = input("Enter your password: ") # Prompting the user to input a password

attempts = 0 # Number of attempts before the brute forcing begins

possible_chars = ''.join(string.ascii_letters + string.punctuation + string.digits)
# Creating a string of all possible characters

while True: # Starting an infinite loop
    
    guess = ''.join(random.choice(possible_chars) for _ in range(len(password))) # Generates a random password
    attempts += 1 # Incrementing the number of times a password crack is attempted
    print(f"Attempt {attempts}. Password: {guess}")
    
    if guess == password: # Checks if the randomly generated password matches the user's input password.
        finish_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # The time at which the algorithm finishes its operations
        print(f"Password found after {attempts} attempts at {finish_time}") # Outputs the number of attempts it took to find the password and the time at which it was found
        break # Loop breaks
        
    
    else: # If the randomly generated password doesn't match the user's input password, continue the loop
        continue 
        
