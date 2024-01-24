#TASK-3 GENERATE RANDOM PASSWORD

import random
import string

def create_password(length):

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    character_list = list(letters + digits + punctuation)

    if length > len(character_list):
        print("Error: Password length is greater than the numbers of available characters.")
        return None

    password = ''.join(random.sample(character_list, length))
    return password

size = int(input("\nEnter the length of the password in digits that you want to create: "))

password = create_password(size)
if password:
    print(f"Your Password of length {size} is:", password)
