from app.schemas.recipe import IngredientRecipe, RecipeCreate, IngredientDetail, RecipePublic

def test_ingredient_recipe_model():
    ing = IngredientRecipe(ingredient_name="Tomato", quantity="2", unit="pcs")
    assert ing.ingredient_name == "Tomato"
    assert ing.quantity == "2"
    assert ing.unit == "pcs"

def test_recipe_create_model():
    ing = IngredientRecipe(ingredient_name="Salt", quantity="1", unit="tsp")
    recipe = RecipeCreate(
        name="Salad",
        instructions="Mix all.",
        ingredients=[ing]
    )
    assert recipe.name == "Salad"
    assert recipe.instructions == "Mix all."
    assert recipe.ingredients[0].ingredient_name == "Salt"

def test_ingredient_detail_model():
    detail = IngredientDetail(name="Pepper")
    assert detail.name == "Pepper"

def test_recipe_public_model():
    detail = IngredientDetail(name="Egg")
    recipe = RecipePublic(
        id=1,
        name="Omelette",
        instructions="Beat eggs and cook.",
        ingredients=[detail]
    )
    assert recipe.id == 1
    assert recipe.name == "Omelette"
    assert recipe.instructions == "Beat eggs and cook."
    assert recipe.ingredients[0].name == "Egg"