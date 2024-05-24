from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    return [dish_name, dish_ingredients]

def check_drinks(drink_name, drink_ingredients):
    ing_set = set(drink_ingredients)

    if ing_set.intersection(ALCOHOLS) != set():
        tail_type = 'Cocktail'
        return drink_name +' '+ tail_type
    else:
        tail_type = 'Mocktail'
        return drink_name +' '+ tail_type
