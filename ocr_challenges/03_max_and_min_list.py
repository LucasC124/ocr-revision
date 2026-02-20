# Challenge: Write a program that lets the user input a list of numbers.
# Every time they input a new number, the program should give a message about what the maximum and minimum numbers in the list are.

# Should you consider if or what to output when there is only a single number in the list?
# Where will the numbers be stored?
number_list = []


# Handle the repeated input of numbers.
number_count = int(input("Please enter as many numbers as you want: "))

for i in range(number_count):
    number = int(input(f"enter number {i + 1}: "))
    number_list.append(number)

# Do you want to only display max and min numbers once there are two or more numbers in the list?
if len(number_list) > 1: # I had to look up how to use min and max for the list
    print("maximum number", max(number_list)) # prints maximum number
    print("minimum number", min(number_list)) # prints minimum number
else:
    print("Not enough numbers entered. ")
    
# Consider how to stop the program.
quit ()
