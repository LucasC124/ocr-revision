# Challenge: Write a program that lets a user choose a letter.
# The program will then find all the words beginning with that letter in a list and print them out.
# It should also say how many words it found.

food_list = [
    "Apple", "Avocado", "Almond", 
    "Banana", "Bacon", "Broccoli", "Blueberry", "Bagel", 
    "Carrot", "Cucumber", "Chicken", "Cheese", "Cabbage", 
    "Doughnut", "Date", "Durian", 
    "Eggplant", "Edamame", "Eclair", 
    "Fig", "French fries", "Feta", 
    "Grapes", "Garlic", "Ginger", "Goat cheese", 
    "Honeydew", "Hamburger", "Hummus", 
    "Ice cream", "Indian curry", "Iced tea", 
    "Jackfruit", "Jalapeno", "Jam", 
    "Kale", "Kiwi", "Ketchup", "Kebabs", 
    "Lemon", "Lettuce", "Lasagna", "Lamb", "Lime", 
    "Mango", "Mushroom", "Macaroni", "Milk", "Muffin", 
    "Noodles", "Nachos", "Nectarine", 
    "Olives", "Onion", "Oatmeal", 
    "Pineapple", "Peach", "Potato", "Pasta", "Pomegranate", 
    "Quinoa", "Quail", "Quiche", 
    "Raspberry", "Rice", "Radish", "Ramen", "Ravioli", 
    "Strawberry", "Spinach", "Steak", "Salmon", "Sweet potato", 
    "Tangerine", "Tomato", "Tofu", "Tacos", "Turmeric", 
    "Udon", "Ugni", "Uva", 
    "Vanilla", "Vegetables", "Vegan burger", 
    "Watermelon", "Waffles", "Walnut", 
    "Xigua", "Xmas pudding", 
    "Yogurt", "Yam", "Yogurt parfait", 
    "Zucchini", "Ziti", "Zander"
]

# How can we get input from the user?
# Think about making the input consistent (upper/lower case)
letter = input("Please enter a letter")

# Where will we store the matching words?
selected_food_list = []

# How can we check each food in the list?
# Think about:
# - How to loop through the food list
# - How to check if a word starts with our letter
# - What to do with matching words
for food in food_list: # I had to look up which to use the for loop
    if food.lower().startswith(letter) or food.upper().startswith(letter):
        selected_food_list.append(food)


# How can we output our results?
# Consider:
# - How many matches were found
# - How to display each matching food
print("Matching foods are:")
for food in selected_food_list:
    print(food)

print(f"\nFound {len(selected_food_list)} matching foods") # I had to search up the 'f"\nFound {len' part as I couldnt get the list to print
# prints how many words were found from the list and the number using the length

