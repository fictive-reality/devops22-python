
f = open("lesson_11/examples/data/text.txt")
try:
    print("".join(f))
finally:
    f.close()

with open("lesson_11/examples/data/text.txt") as f:
    print("".join(f))
