from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    return [dish_name, dish_ingredients]

def check_drinks(drink_name, drink_ingredients):
    for ing in drink_ingredients:
        ing = drink_ingredients[0]
        if ing in ALCOHOLS:
            tail_type = 'Cocktail'
            break
        else:
            drink_ingredients.pop(drink_ingredients.index(ing))
            tail_type = 'Mocktail'
            if len(drink_ingredients)-1 > 0 :
                next
            else:
                break
    return drink_name +' '+ tail_type
