from sqlite3 import converters
import time
import datetime

hour = 1
minutes = 60
seconds = 3600

user_input_seconds = int(input("Please input a number of seconds and i'll calculate how many days, hours, minutes and seconds it is: "))

print(datetime.timedelta(seconds=user_input_seconds))