# Caesar Cipher

from curses.ascii import islower

# User input
user_text = input("Enter the text you want encrypted : ")
user_shift = int(input("Enter the ammount of sidesteps: "))
# Initialize empty variable
encryption = ""
for c in user_text:
    #check if character is an uppercase letter
    if c.isupper():
        # find the position in 0 - 25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        # perform the shift
        new_index = (c_index + user_shift) % 26
        # convert to new character
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        # append to encrypted string
        encryption = encryption + new_character
    # check if character is a lowercase letter
    elif c.islower():
        # find the position in 0 - 25
        c_unicode = ord(c)
        c_index = ord(c) - ord("a")
        # perform the shift
        new_index = (c_index + user_shift) % 26
        # convert to new character
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        # append to encrypted string
        encryption = encryption + new_character  
    else:
        # since character is not a letter, leave it as it is
        encryption += c
print("Plaint text: ",user_text)
print("Encrypted text: ", encryption)