print(f'{"pelle svensson".center(19, "*")}')

lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(lorem.count('ut'))

text_one = "I went to the supermarket"
text_two = "I went to the woods"
print(text_one.endswith(('woods', 'supermarket')))

some_text = "hello world is a common first program to write, python is probably the best programming language to start with"
print(some_text.index('is'))

digit = "\u06F0"
print(digit)
print(digit.isdecimal())

c = '\u2163'
print(c)
print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())

space = "   \t\n\n"
print(space.isspace())

print(",".join(("Hello", "world")))

print("Hello world".ljust(20, '*'))

print('   spacious   '.lstrip())
print('www.example.com'.lstrip('we'))

some_text = "hello world is a common first program to write, python is probably the best programming language to start with"
print(some_text.partition("is"))

print('Text: hey you'.removeprefix('Text:'))

print('Text: hey you'.removesuffix('you'))

print('Hello Sven, from Sven'.replace("Sven", "Petra", 1))

text = "one\ntwo\nthree".splitlines()
print(text)

print('   spacious   '.strip())

print("1234".zfill(5))
print("-1234".zfill(5))