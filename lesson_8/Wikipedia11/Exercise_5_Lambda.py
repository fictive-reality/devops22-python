# 1. Create a list with numbers from 1 - 10
# 2. Create a lambda expression that add 1 to each element: `lambda x: x + 1`
# 3. Apply the lambda on each element in the list with map(your_lambda, your_list)
# 4. Print a list from 3


# ------------------------------------EXERCISE 1------------------------------------

num_list = list(range(1, 11))

# ------------------------------------EXERCISE 2------------------------------------

l1 = lambda x: x + 1

# ------------------------------------EXERCISE 3------------------------------------

new_new_list = map(l1, num_list)

# ------------------------------------EXERCISE 4------------------------------------
# It seems like its important to print it as a list. Otherwise it does not work as intended
print(list(new_new_list))