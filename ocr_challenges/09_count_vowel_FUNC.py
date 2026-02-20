# Challenge: Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

# What vowels are we looking for?
# Consider creating a collection of vowels to check against


# How do we store individual vowel counts?
# Think about:
# - Using a dictionary to track each vowel
# - Initializing counts to zero
# created a dictionary to store each vowel and count 
vowel_count = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}


# How do we get and process the input?
# Consider:
# - Getting text from the user
# - Converting to consistent case
vowel_checker = str(input("Please enter some text"))
vowel_checker_lower = vowel_checker.lower()
vowel_checker_cleaned = ''.join(
    char for char in vowel_checker_lower
    if char.isalnum() # keeps only letters and numbers
) # used this from previous code 


# How do we count the vowels?
# Think about:
# - Looping through the text
# - Checking each character
# - Updating counts
for char in vowel_checker_cleaned:
    if char in vowel_count:
        vowel_count[char] += 1 # counts each vowel 


# How do we display the results?
# Consider:
# - Showing total vowel count
# - Showing individual vowel counts
print("\nVowel Count") # displays the result

for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}") # prints the count for each vowel

total_vowels = sum(vowel_count.values())
print(f"\nTotal vowels found: {total_vowels}") # prints out the total vowels



