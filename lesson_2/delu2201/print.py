from cgi import print_arguments
from multiprocessing.connection import wait
#Create vars for print-program

integer = 1
flyttal = 3.14
my_String = "skriv ut denna sträng"
my_bool = True
my_none = None

#Print values in vars
print(integer)
print(flyttal)
print(my_String)
print(my_bool)
print(my_none)

print(f"Skriver ut samtliga variablar i följd: {integer}, {flyttal}, {my_String}, {my_bool}, {my_none}")

hello_string = input('Skriv ordet "hello":')

print(hello_string * 2)

