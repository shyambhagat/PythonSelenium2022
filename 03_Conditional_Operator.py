import datetime

currentHour = datetime.datetime.now().hour
name = input("Enter your name: ")

if currentHour < 12:
    print("Good Morning,", name)
    print("Have Nice Day")
elif currentHour < 15:
    print("Good Afternoon,", name)
elif currentHour < 19:
    print("Good Evening,", name)
else:
    print("Good Day,", name)

print(currentHour)

