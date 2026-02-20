# Challenge: Checks if the string entered by the user is a palindrome.
# A palindrome is a word that reads the same forwards as it does backwards like "racecar".

# How do we get the input string?
# Consider converting to lowercase for consistency
palindrome_check = str(input("Please enter a word"))
palindrome_converted = palindrome_check.lower() # changes word to all lowercase

# How can we clean the input?
# Think about:
# - Removing spaces
# - Removing punctuation
# - Handling special characters

# removes spaces and punctuations
palindrome_cleaned = ''.join(
    char for char in palindrome_converted
    if char.isalnum() # keeps only letters and numbers
)
# I got confused with this section so did I have to look up how to remove spaces/punctuation and handle special characters



# How do we check if it's a palindrome?
# Consider:
# - Comparing the string forwards and backwards
# - Using string slicing or reversal
if palindrome_cleaned == palindrome_cleaned[::-1]: # checks if word is a palindrome



# How do we display the result?
# Think about clear output formatting
    print(f' {palindrome_check} is a palindrome' )
else:
    print(f' {palindrome_check} is not a palindrome')
