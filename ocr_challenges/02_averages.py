# Challenge: Make a program that asks the user for a series of numbers until they either want to output the average or quit the program.

# I need the user to input a series of numbers until they want to output the average or quit the program.
num_input = []

number_count = int(input("How many numbers would you like to enter. "))

# Where will the numbers be stored?
for i in range(number_count):
    number = float(input(f"enter number {i + 1}: ")) # I had to make the fix from int to float as this was causing most of my problems
    num_input.append(number)


# How can we get the user to repeatedly input numbers?
# Consider handling the case where the user might inputs any CAPS.
# Consider the data type being input, does this need to be transformed (cast)?


# How can we calculate the average? - sum of the numbers divided by the count of numbers
average_of_num = input("Type 'average of the numbers' to calculate the average or type 'quit' to end the program: ")
    
# Output the average

if average_of_num.lower() == 'average of the numbers':
    average = sum(num_input) / len(num_input) # I had to look up how to do the average 
    print("average:", average)

elif average_of_num.lower() == 'quit':
    quit()



