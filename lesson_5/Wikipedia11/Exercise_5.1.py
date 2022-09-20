# See PDF for instructions https://studentportal.nackademin.se/pluginfile.php/282644/mod_resource/content/1/extra_string_lab.pdf

# ------------------------------------EXERCISE 5.1------------------------------------

# Skapa ett program som frågar om två strängar och sedan skriver ut dem
# på varsin rad, omgivna av citationstecken med ett och samma printkommando. Outputen ska se ut exempelvis så här:
# 'Första strängen'
# "Andra strängen"

first_string = input("Give me a string: ")
second_string = input("Give me a second string: ")

# \n New line
print(f'"{first_string}"\n"{second_string}"') 

# \' to write single quote, \\' to write double quote
print(f'"{first_string}"\'"{second_string}"')

# To ignore escape sequence
print(f'"{first_string}"\r"{second_string}"')

# puts a tab
print(f'"{first_string}"\t"{second_string}"')

# Backspace
print(f'"{first_string}"\b"{second_string}"')

# This i dont know, its supposed to print one word 
# then indent the next. Needs to look into this more
print(f'"{first_string}"\f"{second_string}"')

# Same with this one, look into it more
print(f'"{first_string}"\v"{second_string}"')

print(f'"{first_string}"\0"{second_string}"')