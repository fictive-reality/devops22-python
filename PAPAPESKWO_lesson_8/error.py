""" 
try:
    num = int(input("Give a number: "))
except Exception:
    print("You need to give a number!")
    num = int(input("Give a number: "))
#frågar endast en extra gång
print(num*2) """

#import string
#string.ascii_lowercase

def get_number():
    try:
        num = int(input("Give a number: "))
    except Exception:
        raise Exception("User didn't input a number")
    return num

got_number = False
while not got_number:
    try:
        get_number()
        got_number = True
    except Exception:
        print("Enter a number!")
        got_number = False

#int(input("Give a number: "))
#endast ^ ger value error