userName = input('Enter your name: ')

print("Hello", userName)

hoursString = input("Enter Hours: ")
rateString = input("Enter rate: ")

try:
    hours = float(hoursString)
    rate = float(rateString)
except:
    print("Error, please enter numeric input")
    quit()

print(hours, rate)

if hours > 40:
    print("Overtime")
    regular = rate * hours
    overtime = (hours - 40.0) * (rate * 0.5)
    print (regular, overtime)
    pay = regular + overtime
else:
    print("Regular")
    pay = hours * rate

print(userName, "Pay: ", pay)
