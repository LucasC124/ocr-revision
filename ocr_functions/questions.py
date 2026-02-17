
# Write an algorithm, using pseudocode or program code, to call the function push() with the 
# value 15 and output a message saying "Added" if the value was successfully inserted onto the 
# stack or "Not Added" if the stack is full.

#def push(15):
#    result = 15
#if result == True:
#    print("Added")
#else:
#    print("Not Added")

#Octal is a base 8 number system.
#To convert a denary number to base 8:
#• the denary value is divided by 8 and the remainder is stored
#• the integer value after division is divided by 8 repeatedly until 0 is reached
#• the remainders are then displayed in reverse order.

#Example 1:
#Denary 38
#38 / 8 = 4 remainder 6 6
#4 / 8 = 0 remainder 4 4
#Octal = 46
#Example 2:
#Denary 57
#57 / 8 = 7 remainder 1 1
#7 / 8 = 0 remainder 7 7
#Octal = 71

#Write an algorithm to:
#• take a denary value as input from the user
#• convert the number to octal
#• output the octal value.
#You do not need to validate the input from the user.
#Write your algorithm using pseudocode or program code.

#def num_system():
#    denary_num = input("Please enter a number of your choice")
#    octo_num1 = denary_num // 8 
#    octo_num2 = octo_num1 // 8
#
#    octo_value = print(octo_num2)

#The method push() accepts an integer as a parameter and adds it to the top of the
#stack unless the stack is already full.
#If the push is successful the method returns true.
#If the push is unsuccessful due to the stack being full the method returns false.
#Write the method push() using either pseudocode or program code.

#def push(integer, stack):
#    integer = input("Please enter a number")
#    
#    if stack + integer == True
#    print("The push was successful")
#
#    if stack + integer == False
#    print("The push was unsuccessful")



name_list = []
name_inputs = int(input("Enter the number of names you would like to add"))

for i in range(name_inputs):
    name = input(f"Enter a name {i + 1}:")
    name_list.append(name)
    
list_order_int = input("Should the list be printed in the 'original order' or 'reverse order' ")

if list_order_int.lower() == "original order":
    print("original list:", name_list)

elif list_order_int.lower() == "reverse order":
    print("reverse order list:", name_list[::-1])
    