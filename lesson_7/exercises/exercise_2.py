#Default Arguments

# 1.
def number_printer(start=1, stop=11):
    print(list(range(start, stop)))
# 2.
def this_string(word, reverse=False):
    if reverse:
        word = word[::-1]
        print(word)
# 3.
this_string("Hello")
this_string("Hello", reverse=True)