# Challenge: Create a program which will produce the times table for a number entered by the user
# eg if the user enters '2' it should produce:
# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6

# How do we get the number to create times table for?
# Think about:
# - Getting user input
# - Converting to a number
times_table_input = int(input("Please enter a number"))


# How do we generate and display the times table?
# Consider:
# - Creating a loop for multipliers
# - Calculating each result
# - Formatting the output
for i in range(1, 11): # this is a loop from 1 to 10
    times_table_result = times_table_input * i
    print(f"{times_table_input} x {i} = {times_table_result}") # i did have to look up how to print each calculation out

