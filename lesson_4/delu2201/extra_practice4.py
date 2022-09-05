#Dennis Lunnelid
#Extra övningar Lektion 4. 

# Övning 1
for i in range(1, 11):
    print("Hello, user!")


#Övning 2
iterations = 2
number = 2

for x in range(8):
    print(f" {str(number) * iterations}")
    x += 1
    number +=1
    iterations +=1

#Övning 3

correct = 22
guess = int(input("Enter an Integer: ")).strip()

while guess != correct:
    if guess < correct:
        print("No, its higher")
        guess = int(input("Enter an Integer: "))
    elif guess > correct:
        print("No, its lower!")
        guess = int(input("Enter an Integer: "))
else:
    print("Congratulations! You´re correct!")

