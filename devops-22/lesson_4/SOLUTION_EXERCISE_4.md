# Exercise 4

## Instructions

The goal of this exercise is to learn about loops and control flow.

### `Exercise 1` even or odd

Write a program that fulfills the specification:

1. Ask the user for a integer
2. If the integer is even, print even
3. If the integer is odd, print odd

Solution

```Python
number = int(input("Enter a integer: "))

if number % 2:
    print("odd")
else:
    print("even")
```

### `Exercise 2` VIP

Write a program that fulfills the specification:

1. Ask the user for a name
2. Create a tuple with at least five names
3. If the user input is in the tuple, print the text "Welcome {name} your are on the list".
4. If the user input is not in the tuple, print "Sorry, you are not on the list".

Solution

```Python
vip = ("pelle", "lisa", "olle", "evert", "frida")
name = input("Skriv ditt namn: ")

if name in vip:
    print(f"Welcome {name} your are on the list")
else:
    print("Sorry, you are not on the list")
```

<div class="page"/>

### `Exercise 3` Repeat word

Write a program that fulfills the specification:

1. Ask the user for a word
2. Print the word x times, where x = len(word). i.e if the word is `hello` the program writes:

    ```text
    hello
    hello
    hello
    hello
    hello
    ```

Solution

```Python
word = input("Skriv ett ord: ")

for _ in range(len(word)):
    print(word)
```

<div class="page"/>

### `Exercise 4` Sum

Write a program that fulfills the specification:

1. Ask the user for a start and stop integer
2. Print every integer between start and stop. i.e. start = 1, stop = 5 would print:

    ```text
    1
    2
    3
    4  
    ```

3. Print the sum of all integers i.e

    ```text
    Sum: 10
    ```

Solution

```Python
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

total = 0
for i in range(start, stop):
    print(i)
    total += i

print(f"Sum: {total}")
```

<div class="page"/>

### `Exercise 5` Until stop

Write a program that fulfills the specification:

1. Create a while loop that runs forever
2. In each iteration, input a text
3. In each iteration, print a text "Enter `stop` to quit: "
4. If the text equals stop, break the while loop
5. If the text don't equals stop, print the text and the length of the text

Solution

```Python
while True:
    text = input("Enter text, or Enter stop to quit: ")
    if text == "stop":
        break
    print(f'{text} has length {len(text)}')
```

### `Extra exercise`

See studentportalen `Extra_övningar_4.pdf`
