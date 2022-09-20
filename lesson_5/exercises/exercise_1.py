#Basic usage

from os import terminal_size


first_name = "Bengt"

last_name = "Bengtsson"

tele_number = "070123456789"

print(first_name, last_name, tele_number)

full_name = (first_name + " " + last_name)

print(len(full_name), len(first_name), len(last_name))

print(first_name, last_name,"\n",tele_number)

print(full_name + " " + tele_number) # i.

print(f'{full_name} {tele_number}') # ii.

print("{}".format(full_name), "{}".format(tele_number)) # iii.

print("%s" % full_name, tele_number) # iv.