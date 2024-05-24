from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    return [dish_name, dish_ingredients]

def check_drinks(drink_name, drink_ingredients):
    x = 0
    ing = drink_ingredients[0+x]
    while ing not in ALCOHOLS:
        x += 1
        return f'{drink_name} Mocktail'
    else:
        return f'{drink_name} Cocktail'
