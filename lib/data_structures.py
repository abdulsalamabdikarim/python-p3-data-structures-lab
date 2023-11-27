spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = list()
    for food in spicy_foods:
        food_names.append(food["name"])
    return food_names

print(get_names(spicy_foods))

# def get_spiciest_foods(spicy_foods):
#     spiciest_foods = list()
#     for food in spicy_foods:
#         if food["heat_level"] > 5:
#             spiciest_foods.append(food)
#     return spiciest_foods

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' *food['heat_level']}", end = "\n")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:   
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' *food['heat_level']}", end = "\n")

print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    heat = []
    for food in spicy_foods:
        heat.append(food["heat_level"])
    average_heat_level = sum(heat)/len(heat)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

