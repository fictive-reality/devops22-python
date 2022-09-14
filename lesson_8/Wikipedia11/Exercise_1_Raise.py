# 1. Create a function that check if a variable is a float, 
# if not it raises a TypeError("message")

# ------------------------------------EXERCISE 1------------------------------------

def is_num_float(f):
    if not isinstance(f, float): # will check is value A is true to value B. in this case it checks if f is float, if True prints float, if False, raises TypeError
        raise TypeError("Not a float")
    else:
        print("Float")