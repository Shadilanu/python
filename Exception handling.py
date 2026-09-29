try:
    a=int(input("enter a number: "))
    x = 10 / a
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(x)
finally