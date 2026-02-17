# Challenge: Make a program that lets a user input a series of names into a list.
# The program should then ask the user whether they want to print out the list in the original order, or in reverse.

# A list to store the names as mentioned in the questions.
name_list = []
name_inputs = int(input("Enter the number of names you would like to add. "))

# Repeated prompt to allow a series of names to be inputted.
for i in range(name_inputs):
    name = input(f"Enter a name {i + 1}:")
    name_list.append(name)
    
# Following the repeated input of names
# Prompt whether the list should be printed in the original or reverse order.
list_order_int = input("Should the list be printed in the 'original order' or 'reverse order'. ")

# Handle the capture of the print order based on the user's input.
if list_order_int.lower() == "original order": # I did have to look up the .lower()
    print("original list:", name_list)

elif list_order_int.lower() == "reverse order": 
    print("reverse order list:", name_list[::-1]) # I also had to look up how to put the list in reverse

# Does the list need to be transformed before printing?
# Consider handling the case where the user might inputs any CAPS.


# Is the print going to be the whole list in one or each name on a new line?


