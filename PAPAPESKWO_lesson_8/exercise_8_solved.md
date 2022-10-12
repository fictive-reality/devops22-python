```Python
#1
def get_number():
    try:
        num = float(input("Input float: "))
    except Exception:
        raise Exception("User didn't input a float")
    return num
got_number = False
while not got_number:
    try:
        get_number()
        got_number = True
    except Exception:
        print("Enter a float!")
        got_number = False

#2
def get_number():
    try:
        num = int(input("Give a number: "))
        if num % 2 == 0:
            print("Even numbers are not allowed.")
            #byt ut till except raise
            # return num
    except Exception:
        raise Exception("User didn't input a number")
        #byt ut till value error säger martin
    return num

got_number = False
while not got_number:
    try:
        get_number()
        got_number = True
    except Exception:
        print("Enter a number!")
        got_number = False
