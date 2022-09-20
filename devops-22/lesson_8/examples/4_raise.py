
# ValueError

try:
    txt = input("Input a string longer than 3: ")
    if len(txt) < 4:
        raise ValueError("The input should be longer than 3")
except ValueError as v:
    print(v)
finally:
    print("Do something always")

 # Custom exceptions hierarchy


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
