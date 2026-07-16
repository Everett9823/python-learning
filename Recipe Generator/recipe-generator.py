staples_recipe_list = {
    "Chicken, Rice, and Vegetables": {
        "ingredients": ["chicken breasts", "jasmine rice", "mixed frozen vegetables", "oil"],
        "supplies": ["pan", "rice cooker", "oven"],
        "cook_time": 40,
        "instructions": "Cook chicken in a pan. Cook rice. Bake or sauté vegetables, then serve."
    },
    "Salmon, Rice, and Vegetables": {
        "ingredients": ["salmon fillets", "jasmine rice", "mixed frozen vegetables", "oil"],
        "supplies": ["rice cooker", "oven"],
        "cook_time": 35,
        "instructions": "Bake salmon and vegetables. Cook rice, then serve together."
    },
    "Chicken Fried Rice": {
        "ingredients": ["chicken breasts", "jasmine rice", "mixed frozen vegetables", "eggs", "soy sauce", "oil"],
        "supplies": ["pan", "rice cooker", "stove"],
        "cook_time": 30,
        "instructions": "Cook chicken and vegetables. Stir-fry cooked rice with egg, soy sauce, and oil."
    },
    "Chicken Pasta": {
        "ingredients": ["chicken breasts", "pasta", "mixed frozen vegetables", "oil", "pasta sauce"],
        "supplies": ["pan", "pot", "stove"],
        "cook_time": 30,
        "instructions": "Cook pasta. Cook chicken and vegetables, then mix with pasta sauce."
    },
    "Salmon Pasta": {
        "ingredients": ["salmon fillets", "pasta", "mixed frozen vegetables", "oil", "pasta sauce"],
        "supplies": ["oven", "pot", "stove"],
        "cook_time": 35,
        "instructions": "Cook pasta. Bake salmon and vegetables, then combine with pasta sauce."
    }
}


ingredients = input("Enter your ingredients: ").lower().split(",")
ingredients = [ingredient.strip() for ingredient in ingredients]

dietary_preference = input("Enter dietary preference (or none): ").lower()

cooking_time = int(input("How many minutes do you have? "))

supplies = input("Enter your kitchen supplies: ").lower().split(",")
supplies = [supply.strip() for supply in supplies]


def cooking_factors(recipe):
    has_ingredients = all(
        ingredient in ingredients
        for ingredient in recipe["ingredients"]
    )

    has_supplies = all(
        supply in supplies
        for supply in recipe["supplies"]
    )

    enough_time = cooking_time >= recipe["cook_time"]

    is_vegetarian = dietary_preference in ["vegetarian", "vegan"]
    contains_meat = "chicken breasts" in recipe["ingredients"] or "salmon fillets" in recipe["ingredients"]

    if is_vegetarian and contains_meat:
        return False

    return has_ingredients and has_supplies and enough_time


recipe_found = False

for recipe_name, recipe in staples_recipe_list.items():
    if cooking_factors(recipe):
        print(f"\nYou can make: {recipe_name}")
        print(recipe["instructions"])
        recipe_found = True

if not recipe_found:
    print("\nNo matching recipes found.")








    
    

