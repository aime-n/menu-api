#!/usr/bin/env python3
"""Seed the database with initial ingredients and recipes."""

from app.db.session import engine
from app.db.models import Ingredient, Recipe, RecipeIngredientLink
from app.schemas.recipe import RecipeCreate, IngredientDetail
from sqlmodel import Session, select

# Common ingredients to add
INITIAL_INGREDIENTS = [
    "Salt",
    "Black Pepper",
    "Olive Oil",
    "Garlic",
    "Onion",
    "Tomato",
    "Chicken Breast",
    "Ground Beef",
    "Rice",
    "Pasta",
    "Eggs",
    "Milk",
    "Butter",
    "Flour",
    "Sugar",
    "Lemon",
    "Basil",
    "Oregano",
    "Thyme",
    "Rosemary",
    "Carrot",
    "Potato",
    "Bell Pepper",
    "Mushroom",
    "Spinach",
    "Cheese",
    "Bread",
    "Bacon",
    "Salmon",
    "Shrimp",
]

# Sample recipes with ingredients
SAMPLE_RECIPES = [
    {
        "name": "Spaghetti Carbonara",
        "instructions": "1. Cook pasta according to package directions\n2. Cook bacon until crispy\n3. Beat eggs with cheese and pepper\n4. Mix hot pasta with egg mixture\n5. Add bacon and serve immediately",
        "ingredients": [
            {"name": "Pasta", "quantity": "200g", "unit": "grams"},
            {"name": "Bacon", "quantity": "100g", "unit": "grams"},
            {"name": "Eggs", "quantity": "2", "unit": "pieces"},
            {"name": "Cheese", "quantity": "50g", "unit": "grams"},
            {"name": "Black Pepper", "quantity": "1", "unit": "tsp"},
            {"name": "Salt", "quantity": "1", "unit": "tsp"},
        ]
    },
    {
        "name": "Chicken Stir Fry",
        "instructions": "1. Cut chicken into small pieces\n2. Heat oil in wok\n3. Stir fry chicken until golden\n4. Add vegetables and stir fry\n5. Add sauce and serve with rice",
        "ingredients": [
            {"name": "Chicken Breast", "quantity": "300g", "unit": "grams"},
            {"name": "Rice", "quantity": "200g", "unit": "grams"},
            {"name": "Bell Pepper", "quantity": "1", "unit": "piece"},
            {"name": "Carrot", "quantity": "2", "unit": "pieces"},
            {"name": "Garlic", "quantity": "3", "unit": "cloves"},
            {"name": "Olive Oil", "quantity": "2", "unit": "tbsp"},
            {"name": "Salt", "quantity": "1", "unit": "tsp"},
        ]
    },
    {
        "name": "Grilled Salmon",
        "instructions": "1. Season salmon with salt and pepper\n2. Heat grill to medium-high\n3. Grill salmon 4-5 minutes per side\n4. Serve with lemon wedges",
        "ingredients": [
            {"name": "Salmon", "quantity": "200g", "unit": "grams"},
            {"name": "Lemon", "quantity": "1", "unit": "piece"},
            {"name": "Olive Oil", "quantity": "1", "unit": "tbsp"},
            {"name": "Salt", "quantity": "1", "unit": "tsp"},
            {"name": "Black Pepper", "quantity": "1", "unit": "tsp"},
        ]
    },
    {
        "name": "Tomato Basil Pasta",
        "instructions": "1. Cook pasta al dente\n2. Sauté garlic in olive oil\n3. Add chopped tomatoes\n4. Add basil and season\n5. Toss with pasta and serve",
        "ingredients": [
            {"name": "Pasta", "quantity": "250g", "unit": "grams"},
            {"name": "Tomato", "quantity": "4", "unit": "pieces"},
            {"name": "Basil", "quantity": "1/2", "unit": "cup"},
            {"name": "Garlic", "quantity": "4", "unit": "cloves"},
            {"name": "Olive Oil", "quantity": "3", "unit": "tbsp"},
            {"name": "Salt", "quantity": "1", "unit": "tsp"},
        ]
    },
    {
        "name": "Scrambled Eggs",
        "instructions": "1. Beat eggs with salt and pepper\n2. Heat butter in pan\n3. Pour eggs and stir gently\n4. Cook until just set\n5. Serve immediately",
        "ingredients": [
            {"name": "Eggs", "quantity": "3", "unit": "pieces"},
            {"name": "Butter", "quantity": "1", "unit": "tbsp"},
            {"name": "Salt", "quantity": "1/4", "unit": "tsp"},
            {"name": "Black Pepper", "quantity": "1/4", "unit": "tsp"},
        ]
    }
]

def get_or_create_ingredient(session: Session, name: str) -> Ingredient:
    """Get existing ingredient or create new one."""
    statement = select(Ingredient).where(Ingredient.name == name)
    ingredient = session.exec(statement).first()
    
    if not ingredient:
        ingredient = Ingredient(name=name)
        session.add(ingredient)
        session.commit()
        session.refresh(ingredient)
        print(f"  Created ingredient: {name}")
    
    return ingredient

def seed_ingredients(session: Session):
    """Add initial ingredients to the database."""
    print("Adding initial ingredients...")
    
    added_count = 0
    skipped_count = 0
    
    for ingredient_name in INITIAL_INGREDIENTS:
        statement = select(Ingredient).where(Ingredient.name == ingredient_name)
        existing = session.exec(statement).first()
        
        if existing:
            print(f"  Skipping '{ingredient_name}' (already exists)")
            skipped_count += 1
        else:
            ingredient = Ingredient(name=ingredient_name)
            session.add(ingredient)
            print(f"  Added '{ingredient_name}'")
            added_count += 1
    
    session.commit()
    print(f"  Added: {added_count} ingredients")
    print(f"  Skipped: {skipped_count} ingredients")

def seed_recipes(session: Session):
    """Add sample recipes to the database."""
    print("\nAdding sample recipes...")
    
    added_count = 0
    skipped_count = 0
    
    for recipe_data in SAMPLE_RECIPES:
        # Check if recipe already exists
        statement = select(Recipe).where(Recipe.name == recipe_data["name"])
        existing = session.exec(statement).first()
        
        if existing:
            print(f"  Skipping recipe '{recipe_data['name']}' (already exists)")
            skipped_count += 1
            continue
        
        # Create recipe
        recipe = Recipe(
            name=recipe_data["name"],
            instructions=recipe_data["instructions"]
        )
        session.add(recipe)
        session.commit()
        session.refresh(recipe)
        
        # Add ingredients to recipe
        for ingredient_data in recipe_data["ingredients"]:
            ingredient = get_or_create_ingredient(session, ingredient_data["name"])
            
            # Create recipe-ingredient link
            link = RecipeIngredientLink(
                recipe_id=recipe.id,
                ingredient_id=ingredient.id,
                quantity=ingredient_data["quantity"],
                unit=ingredient_data["unit"]
            )
            session.add(link)
        
        session.commit()
        print(f"  Added recipe '{recipe_data['name']}' with {len(recipe_data['ingredients'])} ingredients")
        added_count += 1
    
    print(f"  Added: {added_count} recipes")
    print(f"  Skipped: {skipped_count} recipes")

def seed_database():
    """Seed the database with initial data."""
    with Session(engine) as session:
        print("Starting database seeding...")
        
        # Seed ingredients first
        seed_ingredients(session)
        
        # Seed recipes
        seed_recipes(session)
        
        # Show final counts
        ingredient_count = session.exec(select(Ingredient)).all().__len__()
        recipe_count = session.exec(select(Recipe)).all().__len__()
        
        print(f"\nSeeding completed!")
        print(f"Total ingredients in database: {ingredient_count}")
        print(f"Total recipes in database: {recipe_count}")

if __name__ == "__main__":
    seed_database() 