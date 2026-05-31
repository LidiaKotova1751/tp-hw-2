# Тесты для Ingredient, задание 2.1
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