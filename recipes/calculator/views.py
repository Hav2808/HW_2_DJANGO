from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
#
# def home_view(request):
#
#     all_recipes = list(DATA.keys())
#     context = {'all_recipes': all_recipes}
#
#     return render(request, template_name='home/home.html', context=context)

def calculate_recipe_view(request, recipe):
    if recipe in DATA.keys():
        servings = request.GET.get('servings', 1)
        name_ingridients = {}
        for ing in DATA[recipe]:
            name_ingridients[ing] = round(DATA[recipe][ing] * int(servings), 3)
        context = {
            'recipe': name_ingridients
        }
    else:
        context = {}
    return render(request, 'calculator/index.html', context)

    # return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
