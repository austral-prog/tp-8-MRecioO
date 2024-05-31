from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    menu = dish_name,  set(dish_ingredients)
    return menu

def check_drinks(drink_name, drink_ingredients):
    for ing in drink_ingredients:
        x = 0
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
