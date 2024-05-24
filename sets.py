from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    return [dish_name, dish_ingredients]

def check_drinks(drink_name, drink_ingredients):
    x = 0
    for ing in ALCOHOLS:
        ing = drink_ingredients[0+x]
        if ing in ALCOHOLS:
            tail_type = 'Cocktail'
            break
        else:
            tail_type = 'Mocktail'
            if x < len(drink_ingredients)-1:
                x += 1
            else:
                break
    return drink_name +' '+ tail_type
