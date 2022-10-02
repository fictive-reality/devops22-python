#Data Structure - List

color = []

red = "red"

color.append("red")

print(color[0])

color.extend(["blue", "green"])

print("blue" in color)

print ("white" not in color)

color_2 = ["purple", "cyan", "orange"]

print(color + color_2)

color_3 = ["red", "yellow"]

color_3 *= 3

print(color_3[0:4])

color_3.count("red")

print(color_3.index("yellow"))

print(len("red"))
print(len("yellow"))

number = ["10", "20", "30", "40", "50", "60", "70"]

print(min(number))
print(max(number))