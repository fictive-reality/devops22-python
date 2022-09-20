import csv

cars = [
    {
        "Manufacturer": "Tesla",
        "Model": "Model 3",
        "Year": "2019",
        "Price": "523800"
    },
    {
        "Manufacturer": "Volvo",
        "Model": "XC60",
        "Year": "2018",
        "Price": "313000"
    },
    {
        "Manufacturer": "Saab",
        "Model": "900",
        "Year": "1994",
        "Price": "3000"
    }
]

# https://docs.python.org/3/library/csv.html
with open('lesson_11/examples/data/cars.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=cars[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(cars)
