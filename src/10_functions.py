# Write a function is_even that will return true if the passed-in number is even.

number = 15


def is_even(num):
    return num % 2 == 0


print(is_even(number))


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if num % 2 == 0:
    print("Even!")
else:
    print("Odd")
