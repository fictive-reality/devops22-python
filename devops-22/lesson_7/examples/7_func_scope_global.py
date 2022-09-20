# global

z = 10


def global_outer():
    z = 5

    def global_inner():
        global z
        z = 7
        print(z)
    print(z)
    global_inner()
    print(z)


print(z)
global_outer()
print(z)
