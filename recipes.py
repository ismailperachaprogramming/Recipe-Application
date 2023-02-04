import requests

# Main Menu as well as Command 7
def show_menu():
    # This function shows the menu
    print("\nCOMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name") 
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area") 
    print("7 - Menu")
    print("0 - Exit the Program")
    print()



# Command 1
# This function displays the list of categories to view
def list_all_categories(categories):
    print("\nCATEGORIES:")
  
    for i in range(len(categories)):
        category = categories[i]
        print(" ", category.get_category())
      
    print()


  
# Second Part of Command 2
# This function displays the list of meals for a category. It is accessed if the category entered under Command 2 is found.
def meals_by_category(category, meals):
    print("\n" + category.upper() + " MEALS")
  
    for i in range(len(meals)):
        meal = meals[i]
        print(" ", meal.get_meal())
      
    print()


  
# First Part of Command 2
# This function searches for a meal by category
def search_meal_by_category(categories):
    searchCategory = input("Enter a Category: ")
    isFound = False

    # This for loop searches for the category
    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == searchCategory.lower():
            isFound = True
            break

    # If the category entered is found then it goes to the meals_by_category() function
    if isFound:
        meals = requests.get_meals_by_category(searchCategory)
        meals_by_category(searchCategory, meals) # Go-to function if the category is found.
    else:
        print("Not a valid category.\n")



# Second Part of Command 3 and Second Part of Command 4
# This function is used to display a meal and its recipe which includes its instructions and ingredients
def display_meal(recipe):
    print()
    print("Recipe:", recipe.get_meal())
    print("\nInstructions:", recipe.get_instructions())
    print("\nIngredients:", recipe.get_ingredients())
    print()


  
  # First Part of Command 3
# This function is used to search for a meal by its name
def search_meal_by_name(): 
    searchMeal = input("Enter Meal Name: ")
    meal = requests.get_meal_by_name(searchMeal)
    if meal:
        display_meal(meal)
    else:
        print("A recipe for this meal was not found.\n")


      
# First Part of Command 4
# This function is used to display a  random meal and its recipe with its instructions, and ingredients.
def random_meal():
    print("A random meal was selected just for you!")
    meal = requests.get_random_meal()
    # If the input is indeed a meal then display the meal's contents in display_meal() 
    if meal:
        display_meal(meal)
    else:
        print("Could not find a random meal.\n")


      
# Command 5
# This function lists all the areas that each have food
def list_areas():
  areas = requests.get_areas()

  print("\nAREAS OF FOOD:")
  
  for i in range(len(areas)):
    area = areas[i]
    print(" ", area.get_area())
    
  print()


  
# Command 6
# This function searches for meals based on an area inputted
def search_meals_by_area():
    search_area = input("Enter an area: ")

    meals = requests.get_meals_by_area(search_area)

    print("\n" + search_area.upper() + " MEALS")
  
    for i in range(len(meals)):
        meal = meals[i]
        print(" ", meal.get_meal())
      
    print()


def main():
    categories = requests.get_categories()

  
    print("My Recipes Program")
  
    show_menu()

    # Where to go for each command's selection.
    while True:
        command = input("Command: ")
        if command == "1":
            list_all_categories(categories)
        elif command == "2":
            search_meal_by_category(categories)
        elif command == "3":
            search_meal_by_name()
        elif command == "4":
            random_meal()
        elif command == "5":
            list_areas()
        elif command == "6":
            search_meals_by_area()
        elif command == "7":
            show_menu()
        elif command == "0": 
            print("Thank you for dining with us!")
            break
        else:
            print("Not a valid command.\n")



if __name__ == "__main__":
    main()
