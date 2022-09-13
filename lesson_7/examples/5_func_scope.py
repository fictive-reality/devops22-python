
# Function that print a name in reverse

def rewrite_name(name):
    print(name[::-1])


rewrite_name("Pelle")
print("Pelle")


# Scope & Order

x = 10


def outer_scope():
    x = 5

    def inner_scope(x):
        print(x)
        x = 7
        print(x)
    print(x)
    inner_scope(x)
    print(x)


print(x)
outer_scope()
print(x)
