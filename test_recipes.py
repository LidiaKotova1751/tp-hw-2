# Тесты для класса Ingredient, задание 2.1
from Classes import Ingredient
def test_ingrefient_initialization():
    '''Проверка правильной инициализации атрибутов name, quantity, unit'''
    ing = Ingredient('Мука', 500, 'г')

    assert ing.name == 'Мука'
    assert ing.quantity == 500.0
    assert ing.unit == 'г'

def test_ingrefient_str():
    '''Проверка метода __str__'''
    ing = Ingredient('Мука', 500, 'г')

    assert str(ing) == 'Мука: 500.0 г'

def test_ingrefient_eq():
    '''Проверка метода __eq__'''
    ing_1 = Ingredient('Мука', 500, 'г')
    ing_2 = Ingredient('Мука', 400, 'г')

    assert ing_1 == ing_2

    ing_3 = Ingredient('Соль', 500, 'г')
    
    assert  ing_1 != ing_3

    ing_4 = Ingredient('Мука', 500, 'кг')

    assert  ing_1 != ing_4


# Тесты для  класса Recipe, задание 2.2
import pytest
from Classes import Recipe
def test_recipe_initialization():
    '''Проверка правильной инициализации атрибутов title, ingredients'''
    ing = Ingredient('Мука', 500, 'г')
    recipe = Recipe('Тесто', [ing])

    assert recipe.title == 'Тесто'
    assert recipe.ingredients[0].name == 'Мука'

def test_recipe_add_ingredient_new():
    '''Проверка метода add_ingredient на добавления нового ингредиента'''
    recipe = Recipe('Яичница', [])
    egg = Ingredient('Яйцо', 2, 'шт')

    recipe.add_ingredient(egg)

    assert recipe.ingredients[0].name == 'Яйцо'
    assert recipe.ingredients[0].quantity == 2

def test_recipe_add_ingredient_dublicate():
    '''Проверка метода add_ingredient на добавление дубликата'''
    recipe = Recipe('Тесто', [Ingredient('Мука', 500.0, 'г')])

    recipe.add_ingredient(Ingredient('Мука', 200.0, 'г'))

    assert recipe.ingredients[0].name == 'Мука'
    assert recipe.ingredients[0].quantity == 700

def test_recipe_scale_returns_new_object():
    '''Проверка метода scale на возвращение нового объекта'''
    ing = Ingredient('Мука', 500, 'г')

    recipe = Recipe('Тесто', [ing])

    scaled_recipe = recipe.scale(2)

    assert scaled_recipe is not recipe
    assert recipe.ingredients[0].quantity == 500

def test_recipe_scale_mult():
    '''Проверка метода scale на правильное умножение каждого ингредиента'''
    recipe = Recipe('Тесто', [Ingredient('Мука', 500, 'г')])

    scaled = recipe.scale(0.5)

    assert scaled.ingredients[0].quantity == 250

def test_recipe_scale_neg_ratio():
    '''Проверка метода scale на выбрасывание ValueError при ratio <= 0'''
    recipe = Recipe('Омлет', [Ingredient('Яйцо', 2, 'шт')])

    with pytest.raises(ValueError):
        recipe.scale(-1)
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_recipe_len():
    '''Проверка метода __len__ на возвращение количества уникальных ингредиентов в рецепте'''
    recipe = Recipe('Омлет', [])
    
    recipe.add_ingredient(Ingredient('Соль', 10, 'г'))
    recipe.add_ingredient(Ingredient('Яйцо', 2, 'шт'))
    recipe.add_ingredient(Ingredient('Соль', 5, 'г'))

    assert len(recipe) == 2

