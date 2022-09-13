# scope

x = 10


def outer_scope():
    x = 5

    def inner_scope(x):
        print(x)  # 5
        x = 7
        print(x)  # 7
    print(x)  # 5
    inner_scope(x)
    print(x)  # 5


print(x)  # 10
outer_scope()
print(x)  # 10
