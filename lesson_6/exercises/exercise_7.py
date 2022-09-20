from copy import deepcopy

# Deep Copy

# 1.
these_names = ["Kalle", "Benny", "Leif", "Lisa", "Klara", "Tina"]

# 2.
x = these_names

# 3.
shallow_copy = these_names.copy()
deep_copy = deepcopy(these_names)

# 4.
these_names.pop()
these_names.append("Karl")

# 5.
print(these_names)
"\n"
print(shallow_copy)
"\n"
print(deep_copy)