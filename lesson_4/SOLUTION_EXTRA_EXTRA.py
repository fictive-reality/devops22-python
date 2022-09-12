text = "Jag pluggar på Nackademin"

# 7 höger Qhn wsbnnhy we Uhjrhkltpu
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
new_text = ""

for letter in text:
    if letter.upper() not in chars:
        new_text += letter
        continue
    char_index = chars.index(letter.upper()) + 7
    new_char = chars[char_index % len(chars)]
    if letter.isupper():
        new_text += new_char
    else:
        new_text += new_char.lower()

print(new_text)
