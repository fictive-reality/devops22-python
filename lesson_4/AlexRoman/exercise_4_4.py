###############################################################################################
#  Exercise 1 even or odd                                                                     #
#    Write a program that fulfills the specification:                                         #
#    1. Ask the user for a start and stop integer                                             #
#    2. Print every integer between start and stop. i.e. start = 1, stop = 5 would print:     #
#    3. Print the sum of all integers i.e                                                     #
###############################################################################################

print("We need a range of numbers")
start_range = int(input("Enter the number at the begining of the range: "))
end_range = int(input("Enter the last number in the range: "))
for i in range(start_range, end_range + 1): # added +1 because i want the include even the last number in the range
    print(i)

print(f"The sum of all the numbers in the range is {sum(range(start_range, end_range + 1))}")
    
