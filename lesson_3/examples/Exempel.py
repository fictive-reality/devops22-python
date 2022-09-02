# Unicode
print("\U0001F600")


# String
car = "volvo"

# Printar längden på innehållet i variabeln
print(len(car))

# [0:1] index, ger mig tillbaka första bokstaven i stringen. 0=första, 1=andra osv
print(car[0:1])

# [-2:] ger mig tillbaka de tvp sista karaktärerna i variabeln, kan vara bra för att ta reda på en filändelse.
filetype = "mintestfil.py"
print(filetype[-2:])

my_list = ["Hej", "Hejdå", 10, 20, 30, "Nackademin"] # Detta är en lista, definieras med []
print(my_list) 
print(my_list[1]) # Denna redan kommer att printa ut det andra värdet i listan, i detta fallet "Hejdå"
my_list.append("Nej") # Detta kommer att lägga till "Nej" i min lista
print(my_list)

my_dict = {"DÄED": ("Detta", "Är", "En", "Dict")}
print(type(my_dict))