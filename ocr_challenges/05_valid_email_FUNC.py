# Challenge: Make a program to check whether an email address is valid or not.
# For instance, you could make sure that there are no spaces, that there is an @ symbol and a dot somewhere after it.
# Also check the length of the parts at the start, and that the end parts of the address are not blank.

# I need to check if the email address is valid, through a series of checks.
# Create a function that can be passed the email address in the parameter which then goes through all of the checks required.
# When a check fails, print an explanation as to why it failed.



def email_check():
# Welcome the user to the email address validator with a message
    print("Welcome to the email address validator.")


# If using a loop below, do you need a variable to trigger the condition first of all? (true/false)
# Come back to this after thinking about the next section

# I didn't choose to do a loop but if I was would you have to do something like email_valid == False 
# Then run a while loop. Example: while email_vaild == false ...


# I need to ask the user to input an email address.
# If calling a function you might want to have a loop here to keep asking and calling the function until a valid address format is entered.
# Once valid print out a message confirming the format is valid.
    new_email = input("Please enter a new email address: ")

    if " " in new_email:
        print("Email must not contain any spaces. ") # checks for any spaces

    elif new_email.count("@") != 1:
        print("Email can only contain one '@' symbol. ") # checks how many @ symboles are used

    else:
        email_user, email_domain = new_email.split("@") # I had to search up how to split the two email parts up

        if len(email_user) == 0:
            print("Email user before '@' cannot be empty. ") # checks if first part of the email is filled

        elif "." not in email_domain:
            print("Domain must contain a '.' symbol. ") # checks for a . in the email

        else:
            print("Email is valid. ")
    
# Print a message saying thanks for using the email address validator
    print("Thanks for using the email validator. ")

email_check()


