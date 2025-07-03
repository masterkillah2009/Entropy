# Entropy
⚠️ This script is for educational purposes only. Do not use this against real passwords, systems, or users. This is to demonstrate the weakness of short, low-entropy passwords and the power of randomness in brute-force scenarios.

Entropy is a brute force algorithm that tries to crack passwords by looping over a list of possible passwords. However, unlike most brute force algorithms, the password are not stored in a wordlist. They are randomly generated and are unpredictable as a result. 

To initiate the program, the user is required to enter a password. After that, the program randomly generates passwords as a way to guess the password you input.  
This procedure accounts for the password length so it doesn't just generate passwords of various lengths. I will soon implement a feature where the procedure accounts for each individual character in a password. 

The amount of time it takes to find the password that was input by the user depends on two factors:
1. The length of the password 
2. The variation of characters
Passwords with shorter lengths and a small variation of characters don't take so much time to crack whereas passwords with greater lengths and a wider variation of characters take longer to crack. However, take this with a grain of salt as since the passwords are randomly generated, it can even take long for shorter password to be cracked. 

Once the password is found, the program outputs the password, the number of attempts it took to find the password and the time and date at which it occurred. 
