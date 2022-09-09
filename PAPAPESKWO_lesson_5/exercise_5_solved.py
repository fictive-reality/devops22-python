#1
firstname = input("What is your first name? ").capitalize()
lastname = input("What is your surname? ").capitalize()
tele = input("What is your telebobo number? ")

fullname = firstname + " " + lastname

print(f"{fullname} \n{tele} ")
print(len(fullname))

print('Good morning {}'.format(fullname))
print('Good morning %s' % fullname)
print(f'Good morning {fullname}')
print("Good morning " + fullname)

#2
fullname = "Tomislav Orlovac"
print(fullname[:5])
print(fullname[1:-1])
print(fullname.upper()[::2])
print(fullname[::-1])
print(fullname[4:5])

#3
import emoji
car_price = int(input("What is the cost of your new car? "))
if car_price <= 30000:
    print('\n{melting face}')
elif car_price <= 100000:
    print("\n{winking face}")
elif car_price <= 350000:
    print("\n{money-mouth face}")
elif car_price > 350000:
    print("\n{hot face}")

#4
