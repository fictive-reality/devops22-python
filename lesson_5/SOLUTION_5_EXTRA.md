# Solution Exercise

## Exercise 4 - `Extra`

Write a program that handles salary negotiations. The user is the employee and the boss is your program.

1. The boss tells the user it's current salary and currency
2. The employee ask for more money with an input. I.e 2000 more
3. The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
4. The employee ask again for another amount i.e 1800
5. The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 4 and 5 iterates in a loop until the employee quit or the boss accept the amount.`

```python

salary = 10000
currency = 'SEK'
print(f"Your current salary is {salary} {currency}")

# 2
initial_increase = int(input("How much do you expect in salary increase? "))

# 3
percentage = initial_increase / salary * 100
print(f"You ask for a increase of {percentage}%, the answer is NO!")

# 6
decision = "NO"
while decision != 'YES':
    # 4
    increase = input("How much do you expect in salary increase? ")
    if increase == 'quit':
        break
    # 5
    increase_in_proc = int(increase) / salary * 100
    if (int(increase) < initial_increase):
        decision = 'YES'
        print(f"You ask for a increase of {percentage}%, I accept!")
    else:
        print(
            f"You ask for a increase of {percentage}%, the answer is {decision}!")

```
