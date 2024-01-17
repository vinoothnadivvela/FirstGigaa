def order_food(lst): 
    meal_count = {}
    for developer in lst:
        meal_option = developer['meal']
        meal_count[meal_option] = meal_count.get(meal_option, 0) + 1

    return meal_count
