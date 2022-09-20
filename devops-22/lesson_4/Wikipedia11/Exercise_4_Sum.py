



start_int = int(input("Please give me a start number: "))
stop_int = int(input("Please give me a end number: "))
step_int = 1

for i in range(start_int, stop_int, step_int):
    print(i)

sum = sum(range(start_int, stop_int, step_int))
print(f"Sum: {sum}")