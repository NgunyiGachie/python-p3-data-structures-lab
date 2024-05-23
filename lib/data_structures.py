
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
    foods_name = [d['name'] for d in spicy_foods]
    return foods_name
names = get_names(spicy_foods)
print(names)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food ['heat_level'] > 5]
spiciest_foods_list = get_spiciest_foods(spicy_foods)
print(spiciest_foods_list)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}')
print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)
            return food
get_spicy_food_by_cuisine(spicy_foods, "Sichuan")

def print_spiciest_foods(spicy_foods):
    def heat_level_emojis(heat_level_emoji):
         '''
         Convert heat level to chili pepper emojis.
         '''
         return '🌶' * heat_level_emoji 
    
    spiciest_foods = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest_foods.append(food)
            emojis = heat_level_emojis(food['heat_level'])
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emojis}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    foods = [d['heat_level'] for d in spicy_foods]
    total_sum = sum(foods)
    count = len(foods)
    average = total_sum / count
    return average
average_foods = get_average_heat_level(spicy_foods)
print(average_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

