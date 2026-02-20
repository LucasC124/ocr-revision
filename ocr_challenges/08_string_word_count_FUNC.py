# Challenge: Counts the number of individual words in a string.
# For added complexity, the program could read these strings in from a text file and generate a summary.

# How do we get the input?
# Consider:
# - Getting text from user input
# - Creating a function to count words - YES CREATE A FUNCTION TO DO THIS



# How do we count the words?
# Think about:
# - Splitting the text into words
# - Handling punctuation
# - Counting the resulting words
def word_checker(text):
    # removes punctuation
    cleaned_text = ''.join(
        char for char in text 
        if char.isalnum() or char.isspace() # keeps letters, numbers and spaces
    )

    words = cleaned_text.split() # splits text into words

    return len(words) # returns word count

word_count = str(input("Please enter a text of words"))

total_words = word_checker(word_count)

print(f"\nTotal number of words: {total_words}") # prints total number of words


# Optional: How can we read from a file?
# Consider:
# - Opening and reading a file
# - Handling file not found errors
# - Processing the file contents


