# Write a program that examines three variables - x, y & z -
# and prints the largest odd number among them. If none of them are odd,
# it should print a message to that effect.
x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
z = int(input("Enter the value of z : "))

'''
Takes a number and determines if it is odd.
Returns True is it is odd
Returns False if it is not odd
'''


def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True


# No odd numbers
if not is_odd(x):
    if not is_odd(y):
        if not is_odd(z):
            print("No odd number to play with!.")

# All three are odd
if is_odd(x):
    if is_odd(y):
        if is_odd(z):
            if x > y and x > z:
                print(str(x) + " x is the largest")
            if y > x and y > z:
                print(str(y) + " y is the largest")
            if z > x and z > y:
                print(str(z) + " z is the largest")

# x & y are odd
if is_odd(x):
    if is_odd(y):
        if x > y:
            print(str(x) + " x is the largest")
        else:
            print(str(y) + " y is the largest")

# x & z are odd
if is_odd(x):
    if is_odd(z):
        if x > z:
            print(str(x) + " x is the largest")
        else:
            print(str(z) + " z is the largest")

# y & z are odd
if is_odd(y):
    if is_odd(z):
        if y > z:
            print(str(y) + " y is the largest")
        else:
            print(str(z) + " z is the largest")

# Only x is odd
if is_odd(x):
    if not is_odd(y):
        if not is_odd(z):
            print(str(x) + " Only x is odd")

# Only y is odd
if is_odd(y):
    if not is_odd(x):
        if not is_odd(z):
            print(str(y) + " Only y is odd")

# Only z is odd
if is_odd(z):
    if not is_odd(x):
        if not is_odd(y):
            print(str(z) + " Only z is odd")




