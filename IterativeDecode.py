"""
Password Decoder 
Uses Iteration
Kostas Spyropoulos
"""
import string
import random

target = str(input("Enter password"))


# string containing the password cracked correctly
passwordCracked = ""
                   
# array contains all printable characters
charList = []
                   
for character in string.printable:
    charList.append(character)
    
# counter i iterates through target checking if the guessed char is equal to the taget's ith element
i = 0

# while loop runs until password is cracked
while target != passwordCracked:
    # guess random character
    char = str(random.choice(charList))
    
    # if random character guess is equal to the ith element of the password,
    # increment i, reset charList to original length and characters, and 
    # add correctly guessed character to passwordCracked
    if char == target[i]:
        i += 1
        charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
        passwordCracked = passwordCracked + char
    # if random character is not equal to ith element, remove char from charList to increase chances of finding correct char
    # by removing the incorrect character for that ith element of target
    else:
        charList.remove(char)
    
print("Cracked password: " + str(passwordCracked))
