def get_cook_book():
    dishes = list()
    number_ingredients_list = list()
    cook_book = dict()
    with open('cook_book.txt', 'r') as f:
        for line in f:
            dish = line.strip()
            dishes.append(dish)
            number_ingredients = int(f.readline())
            number_ingredients_list.append(number_ingredients)
            ingredients_list = list()
            for line in f:
                if '|' in line:
                    ingredient = dict()
                    new_line = line.split('|')
                    ingredient['ingredient_name'] = new_line[0]
                    ingredient['quantity'] = int(new_line[1])
                    ingredient['measure'] = new_line[2].strip()
                    ingredients_list.append(ingredient)
                else:
                    break
            cook_book[dish] = ingredients_list
    return cook_book


def print_shopping_list(shopping_list):
    for ingredient, value in shopping_list.items():
        print(f'{ingredient} - {value["quantity"]} {value["measure"]}')


def get_shopping_list(dishes, person_count):
    cook_book = get_cook_book()
    shopping_list = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_ingredients_list = dict()
            if ingredient['ingredient_name'] not in shopping_list:
                new_ingredients_list['measure'] = ingredient['measure']
                new_ingredients_list['quantity'] = ingredient['quantity'] * person_count
                shopping_list[ingredient['ingredient_name']] = new_ingredients_list
            else:
                shopping_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    print(f'Для приготовления блюд на {person_count} персон потребуется:')
    print_shopping_list(shopping_list)


get_shopping_list(['Омлет', 'Фахитос'], 13)
