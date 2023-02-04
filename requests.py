from urllib import request, parse
import json
import requests
from objects import Category, Meal, Recipe, Area, Random

def get_categories(): # This is involved with Command 1 for getting the categories to list
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
  
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for category_data in data["meals"]:
            category = Category(category_data["strCategory"])
            categories.append(category)
          
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories



def get_meals_by_category(category): # This is involved with Command 2 for getting the meals by category to list
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = request.urlopen(url)

    meals = []
    data = json.loads(f.read().decode("utf-8"))
  
    for meal_data in data["meals"]:
        ingredients = []
        for i in range(1, 21):
            ingredient_key = "strIngredient" + str(i)
          
            if ingredient_key in meal_data:
                ingredient = meal_data[ingredient_key]
                ingredients.append(ingredient)

        meal = Meal(meal_data["idMeal"],
                    meal_data["strMeal"],
                    meal_data["strMealThumb"],
                    ingredients)

        meals.append(meal)

    return meals






def get_meal_by_name(meal_name): # This is involved with Command 3 for getting a meal by its name to be searched
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(meal_name)

    f = request.urlopen(url)


    recipe = None
    try:
        data = json.loads(f.read().decode("utf-8"))

        for recipe_data in data["meals"]:
            ingredients = []

            for i in range(1, 21):
                ingredient_key = "strIngredient" + str(i)
                if ingredient_key in recipe_data:
                    ingredient = recipe_data[ingredient_key]
                    ingredients.append(ingredient)

            recipe = Recipe(recipe_data["idMeal"],
                            recipe_data["strMeal"],
                            recipe_data["strCategory"],
                            recipe_data["strInstructions"],
                            recipe_data["strMealThumb"],
                            ingredients)

    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return recipe



def get_random_meal(): # This is involved with Command 4 for getting a random meal
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    f = request.urlopen(url)
    response = f
    data = json.loads(response.read().decode("utf-8"))
    meal_data = data["meals"][0]
    ingredients = []

    for i in range(1, 21):
        ingredient = meal_data["strIngredient" + str(i)]
        if ingredient:
            ingredients.append(ingredient)

    random = Random(meal_data["idMeal"], meal_data["strMeal"], meal_data["strCategory"], meal_data["strInstructions"], meal_data["strMealThumb"], ingredients)
    return random


def get_areas(): # This is involved with Command 5 for getting the areas

    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
  
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for area_data in data["meals"]:
            area = Area(area_data["strArea"])
            areas.append(area)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return areas

def get_meals_by_area(area): # This is involved with Command 6 for getting the meals by the area
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + parse.quote(area)
  
    f = request.urlopen(url)

    meals = []
    data = json.loads(f.read().decode("utf-8"))
    for meal_data in data["meals"]:
        ingredients = []
        for i in range(1, 21):
            ingredient_key = "strIngredient" + str(i)
            if ingredient_key in meal_data:
                ingredient = meal_data[ingredient_key]
                ingredients.append(ingredient)

        meal = Meal(meal_data["idMeal"],
                    meal_data["strMeal"],
                    meal_data["strMealThumb"],
                    ingredients)

        meals.append(meal)

    return meals
