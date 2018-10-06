numXs = int(input('How many times should I print the letter X ? '))
toPrint = 'x' * numXs
print(toPrint)


# Ask user to input ten numbers.
# If no odd numbers entered print a message that no odd number entered
# if odd numbers entered print out the larget odd number

# Create an empty list
chars = []
# This gives the numbers 0 - 9
for i in range(0, 10):
    # Add the numbers to a list and give a count of the numbers entered
    chars.append(input("Entry #" + str(i + 1) + ' '))

biggest = 0
for i in range(0, len(chars)):
    # Check if this is an odd number
    if int(chars[i])% 2 != 0:
        # If the int is bigger than the accumulator
        if int(chars[i]) > biggest:
            # Add the accumulator == the biggest
            biggest = int(chars[i])

# If no odds found, print a message
if biggest == 0:
    print('No odd numbers to process! ')
# If ints found print the biggest
if biggest > 0:
    print(str(biggest) + ' is the biggest odd number.')
