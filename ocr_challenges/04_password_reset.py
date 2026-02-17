# Challenge: Create a password reset program that only accepts a new password if the following conditions are met:
# 1. At least eight characters long
# 2. Has lower case and upper case letters.
# The password reset program should also make the user input their new password twice to validate that they have entered it correctly.

# Output instructions to the user
password_conditions = input("If you want to reset your password the following conditions need to be met: " \
"At least 8 characters long, needs both lower and upper case letters and please enter the same password twice. ")

# Do you want to automatically continue with the program until the user enters a valid password?
# If yes, you need to control the condition
new_password = str(input("Please enter a new password that meets the conditions. "))

# Capture the user's input
new_password = []

# Check if the password is at least 8 characters long
# Then check if the password has both lower and upper case letters
# Finally, check if the password entered the second time is the same as the first time
new_password = input("Enter a new password: ")

if len(new_password) < 8:
    print("Password isn't long enough.")

# I had to search up how to check for lowercase and uppercase characters
elif not any(char.islower() for char in new_password):
    print("Password must contain at least one lowercase letter.")

elif not any(char.isupper() for char in new_password):
    print("Password must contain at least one uppercase letter.")
# If the password meets all the conditions, print a success message and end the program
else:
    confirm_new_password = input("Please re-enter your new password: ")

    if new_password == confirm_new_password:
        print("Password was successfully changed.")
    else:
        print("Passwords do not match.")




