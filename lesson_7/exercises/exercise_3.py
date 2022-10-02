# Return
# 1.
def my_integer():
  return 1
# 2.
def my_tuple(x,y):
  return x, y
# 3.
def my_boolean():
  return True
# 4.
def my_float():
  return 10.0
# 5.
def full_name(first_name, last_name):
  return f'{first_name} {last_name}'
# 6.
def rectangle_area(length, width):
  return length*width
# 7.
def sum_list(values):
  return sum(values)
# 8.
def this_repeater(word, repeat):
  for r in range(repeat):
      print(word)
      
this_repeater("Hello", 3)

