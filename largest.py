# Write a function that accepts a list of numbers as an argument.
# It should return the largest number in the list.

def largest(list_of_numbers):
    maximum = 0
    for number in list_of_numbers:
        if number > maximum:
            maximum = number

    return maximum

numbers = [7, 21, 4, 33, -456, 8, 99, 1, -12340, 2, 79, 88, 124, 90]

print(" ")
print(f"Original List: {numbers}")
print(" ")
print(f"Largest Number: {largest(numbers)}")
print(" ")