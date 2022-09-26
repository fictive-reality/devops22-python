try:
    with open("a_lost_file", "r") as f:
        print(f)
except FileNotFoundError:
    print("File not found")
