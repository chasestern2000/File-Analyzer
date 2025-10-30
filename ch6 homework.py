# Chapter 6 homework
# Opening file
file = open('numbers8.txt', 'r')

# Read all lines in the file
# Stripping the numbers fixes problems with getting the smallest number
lines = [int(num.strip()) for num in file.readlines()]

# Variable for total sum
sumit = 0

# Variable for average
avg = 0

# Loop for all variables
for num in lines:
    # Converts numbers to int
    sumit += int(num)
    # Variable for total numbers
    total_nums = 8
    avg = sumit/total_nums
    # Finds largest and smallest numbers
    largest = max(lines)
    smallest = min(lines)

# Prints results
print('Sum of all numbers: ', sumit)
print()
print('Average of all numbers: ', avg)
print()
print('Total numbers in the list:', total_nums)
print()
print('Largest number in the list:', largest)
print()
print('Smallest number in the list:', smallest)
