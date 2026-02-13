# Exercise 1: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if (hour >= 0 and hour < 12):
    print("Good Morning")
elif (hour >= 12 and hour < 17):
    print("Good Afternoon")
elif (hour >= 17 and hour < 0):
    print("Good Evening")
