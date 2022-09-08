# Exercise 5

## Instructions

Todays exercises focus on String and it's built-in methods.

```Python
firstname = "john"
lastname = "smith"
tele = "00468123456789"
```

### `Exercise 1` Basic usage

1. Print first, lastname and tele on the same line
2. Create a variable fullname
3. Assign to the new variable fullname, firstname and lastname separated with a space.
4. Print the length `len()` of fullname, firstname and lastname
5. Print a escape sequence `\n` so the first line contains fullname, and the second line tele.
6. Write the fullname and tele with the four different methods:
   1. Only using print() and string concatenation i.e "firstname" + " " ..
   2. Using f-string
   3. Using format, i.e print('{}'.format(firstname))
   4. Using printf (%) syntax, i.e print('A name %s' % firstname)

### `Exercise 2` Slice

Slice can be used to get a substring, i.e to get all but last letter my_string[:-1], to get all except the first letter my_string[1:], to get three first letters my_string[:3]

Docs about [slice](https://docs.python.org/3/library/functions.html#slice)

1. Use slice to get the first 5 characters i fullname
2. Use slice to get all characters except the first and last one
3. Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
4. Use slice to print a word backwards.
5. Use slice to get the 5th character

<div class="page"/>

### `Exercise 3` Unicode

How to write a euro sign can be found at [Currency Symbols](https://www.unicode.org/charts/PDF/U20A0.pdf). How to write emoji can be found at [emoji](https://unicode.org/emoji/charts/full-emoji-list.html), you can also check the formal charts for [symbols](https://www.unicode.org/charts/#symbols) you use either name or code: \N{money-mouth face}, or code \U0001F911

Write a program that fulfills the specification

1. Let the user input a price, i.e Your new car cost: 1000000
2. Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
3. Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one

### `Exercise 4` Extra

Write a program that handles salary negotiations. The user is the employee and the boss is your program.

1. The boss tells the user it's current salary and currency
2. The employee ask for more money with an input. I.e 2000 more
3. The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
4. The employee ask again for another amount i.e 1800
5. The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 4 and 5 iterates in a loop until the employee quit or the boss accept the amount.

### `Exercise 5` Extra Extra

Check studentportalen for extra_string_lab.pdf
