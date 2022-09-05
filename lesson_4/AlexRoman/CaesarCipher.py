# Caesar Cipher

user_text = input("Enter the text you want encrypted : ").upper()
user_shift = int(input("Enter the ammount of sidesteps: "))



#shift = 3 # the shift count
#text = "HELLO WORLD"
encryption = ""
for c in user_text:
    #chech if character is an uppercase letter
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
    else:
        # since character is not uppercase, leave it as it is
        encryption += c
print("Plaint text: ",user_text)
print("Encrypted text: ", encryption)