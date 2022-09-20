
# https://docs.python.org/3/library/stdtypes.html#string-methods

# str.center(width[, fillchar])
# https://docs.python.org/3/library/stdtypes.html#str.center
print(f'{"pelle svensson".center(19, "*")}')


# str.count(sub[, start[, end]])
# https://docs.python.org/3/library/stdtypes.html#str.count
lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(lorem.count('ut'))


# str.endswith(suffix[, start[, end]])¶
# https://docs.python.org/3/library/stdtypes.html#str.endswith

text_one = "I went to the supermarket"
text_two = "I went to the woods"
print(text_one.endswith(('woods', 'supermarket')))

# str.expandtabs(tabsize=8)¶
# https://docs.python.org/3/library/stdtypes.html#str.expandtabs

# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.
# https://docs.python.org/3/library/stdtypes.html#str.index

some_text = "hello world is a common first program to write, python is probably the best programming language to start with"
print(some_text.index('is'))

# str.isalnum()
# https://docs.python.org/3/library/stdtypes.html#str.isalnum

# str.isalpha()
# https://docs.python.org/3/library/stdtypes.html#str.isalpha


# str.isascii()
# https://docs.python.org/3/library/stdtypes.html#str.isascii
# https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)

# str.isdecimal()
# https://docs.python.org/3/library/stdtypes.html#str.isdecimal
# Unicode General Category “Nd”.

digit = "\u06F0"
print(digit)
print(digit.isdecimal())

# Roman 4 Ⅳ
c = '\u2163'
print(c)
print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())


# str.islower()
# https://docs.python.org/3/library/stdtypes.html#str.islower


# str.isnumeric()
# https://docs.python.org/3/library/stdtypes.html#str.isnumeric


# str.isspace()
# https://docs.python.org/3/library/stdtypes.html#str.isspace

# str.isspace()
# https://docs.python.org/3/library/stdtypes.html#str.isspace

space = "    \t\n\n  "
print(space.isspace())


# str.join(iterable)
# https://docs.python.org/3/library/stdtypes.html#str.join

print(",".join(("hello", "world")))


# str.ljust(width[, fillchar])
# https://docs.python.org/3/library/stdtypes.html#str.ljust

print("hello world".ljust(20, '*'))

# str.lstrip([chars])
# https://docs.python.org/3/library/stdtypes.html#str.lstrip

print('   spacious   '.lstrip())
print('www.example.com'.lstrip('we'))


# str.partition(sep)
# https://docs.python.org/3/library/stdtypes.html#str.partition

some_text = "hello world is a common first program to write, python is probably the best programming language to start with"

print(some_text.partition("is"))


# str.removeprefix(prefix, /)
# https://docs.python.org/3/library/stdtypes.html#str.removeprefix

print('Text: hey you'.removeprefix('Text:'))

# str.removesuffix(suffix, /)
# https://docs.python.org/3/library/stdtypes.html#str.removesuffix

print('Text: hey you'.removesuffix('you'))


# str.replace(old, new[, count])
# https://docs.python.org/3/library/stdtypes.html#str.replace

print('Hello Sven, from Sven'.replace("Sven", "Petra", 1))


# str.split(sep=None, maxsplit=-1)
# https://docs.python.org/3/library/stdtypes.html#str.split

print('1,2,3'.split(','))


# str.splitlines([keepends])
# https://docs.python.org/3/library/stdtypes.html#str.splitlines

text = "one\ntwo\nthree".splitlines()
print(text)


# str.startswith(prefix[, start[, end]])
# https://docs.python.org/3/library/stdtypes.html#str.startswith


# str.strip([chars])
# https://docs.python.org/3/library/stdtypes.html#str.strip

print('   spacious   '.strip())


# str.zfill(width)
# https://docs.python.org/3/library/stdtypes.html#str.zfill

print("1234".zfill(5))
print("-1234".zfill(5))
