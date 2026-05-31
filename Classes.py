class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        float_val = float(value)
        if float_val <= 0:
            raise ValueError('Количество должно быть положительным')
        self._quantity = float_val

    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit}'
    
    def __repr__(self):
        return f'Ingredient({self.name!r}, {self.quantity}, {self.unit!r})'
    
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False



class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient] | None = None):
        self.title = title
        self.ingredients = []

        if ingredients is not None:
            for item in ingredients:
                self.add_ingredient(item)
    
    def add_ingredient(self, ingredient: Ingredient):
        for exis in self.ingredients:
            if exis == ingredient:
                exis.quantity += ingredient.quantity
                return

        self.ingredients.append(Ingredient(ingredient.name, ingredient.quantity, ingredient.unit))
    
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        scaled_ingredients = [Ingredient(ing.name, ing.quantity * ratio, ing.unit) for ing in self.ingredients]

        return Recipe(self.title, scaled_ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        lines = [f'Рецепт: {self.title}']
        for ing in self.ingredients:
            lines.append(f' - {ing}')
        return '\n'.join(lines)



class ShoppingList:
    def __init__(self):
        self._items = []
    
    def add_recipe(self, recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self):
        summary = {}

        for ingredient, _ in self._items:
            key = (ingredient.name, ingredient.unit)

            if key in summary:
                summary[key] += ingredient.quantity
            else:
                summary[key] = ingredient.quantity
        
        res = []

        for (name, unit), quantity in summary.items():
            res.append(Ingredient(name, quantity, unit))

        res.sort(key=lambda ing: ing.name)

        return res
    
    def __add__(self, other: ShoppingList):
        if not isinstance(other, ShoppingList):
            return NotImplemented
        
        new_shoppinglist = ShoppingList()
        
        new_shoppinglist._items = self._items + other._items

        return new_shoppinglist




class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float):
        scaled_recipe = super().scale(ratio)

        return DietaryRecipe(scaled_recipe.title, self.diet_type, scaled_recipe.ingredients)
    
    def __str__(self):
        base_str = super().__str__()

        return base_str.replace('Рецепт:', f'Рецепт: [{self.diet_type}]', 1)
