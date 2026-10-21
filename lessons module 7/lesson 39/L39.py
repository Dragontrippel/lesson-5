city = input("Enter your city name: ")
temp = float(input("Enter today's temperature in C: "))

print("City:", city)
print("temperature:", temp)

if temp > 35:
    print("Warning it is very hot today!")


if temp > 25:
        print("Great day to go outside!")
else:
      print("grab a jacket before you go out!")



if temp > 35:
      print("Weather: Scorching hot")
elif temp > 25:
      print("weather: Warm and sunny")
elif temp > 15:
      print("Weather: Cool and Breezy")
else: 
      print("Weather: Cold - stay warm!")


import datetime
import calendar


now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(2027))