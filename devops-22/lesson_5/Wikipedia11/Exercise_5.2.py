# See PDF for instructions https://studentportal.nackademin.se/pluginfile.php/282644/mod_resource/content/1/extra_string_lab.pdf

# ------------------------------------EXERCISE 5.2------------------------------------

num_one = int(input("Give me an integer: "))
num_two = int(input("Give me a second integer: "))

sum = num_one + num_two

diff2 = num_one % num_two
if num_one > num_two:
    diff = num_one - num_two
else:
    diff = num_two - num_one

multiplication = num_one * num_two
quota = num_one / num_two

print_1 = print(f"""You choose the numbers {num_one} & {num_two} and the sum of the two numbers is {sum},
the diff is {diff}, the numbers times eachother is {multiplication} and divided the result is {round(quota, 2)}.""")