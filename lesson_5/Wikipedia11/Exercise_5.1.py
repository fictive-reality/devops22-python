# See PDF for instructions https://studentportal.nackademin.se/pluginfile.php/282644/mod_resource/content/1/extra_string_lab.pdf

# ------------------------------------EXERCISE 5.1------------------------------------

# Skapa ett program som frågar om två strängar och sedan skriver ut dem
# på varsin rad, omgivna av citationstecken med ett och samma printkommando. Outputen ska se ut exempelvis så här:
# 'Första strängen'
# "Andra strängen"

first_string = input("Give me a string: ")
second_string = input("Give me a second string: ")

print(f'"{first_string}"\n"{second_string}"')