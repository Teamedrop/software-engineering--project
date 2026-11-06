import json
recipe_storage = {
    "Pancakes": {
        "ingredients": ["flour", "milk", "eggs", "sugar"],
        "instructions": "Mix ingredients together and cook on a hot pan until golden brown."
    },
    "Tea": {
        "ingredients": ["milk", "sugar", "lipton", "milo or bournvita"],
        "instructions": ("pour preferred amount of water in pot and cover it until it boils,"
        " pour the water in a cup and add your torn lipton bag,"
        "remove the bag and mix the remaining ingredients."),
    }
}
FILENAME = "recipes.json"
def load_recipes():
    try:
        with open(FILENAME, "r") as file:
           return json.load(file)
    except FileNotFoundError:
       return recipe_storage

def save_recipes(data):
   with open(FILENAME, "w") as file:
      json.dump(data, file, indent=4)


def view_all_recipes():
    if not recipe_storage:
      print("No recipes found.")
    else:
     counter = 1
    for recipe_name in recipe_storage:
        print(f"{counter}. {recipe_name}")
        counter += 1
def view_recipe_details():
   view_all_recipes()
   user_input = input("What are you looking for? ") 
   if user_input not in recipe_storage:
      print("Error Found.")
   else:
      recipe = (recipe_storage[user_input])
      print("Ingredients:", recipe["ingredients"])
      print("Instructions:", recipe["instructions"])
def add_recipe(recipe_storage):
   print("CURRENT STORAGE KEYS:", list(recipe_storage.keys()))
   new_recipe = input("What recipe do you want to add? ").strip().capitalize()

   if any(existing.lower() == new_recipe.lower() for existing in recipe_storage):
      print("Recipe already exists.")
   else:
      new_ingredients = input("What are the ingredients for the new recipe?").split(",")
      new_instructions = input("What are the instructions for the new recipe?")

      recipe_storage[new_recipe] = {
         "ingredients": new_ingredients,
         "instructions": new_instructions,
      }
      save_recipes(recipe_storage)
      print(f"'{new_recipe}' has been added successfully!")
def main():
  global recipe_storage
  recipe_storage = load_recipes()
  while True:
       print("""menu options: 
         1. View all recipes"
          2. View recipe details"
           3. Add a recipe "
            4. Exit""")

       user_menu_choice = input("What do you want to do? " )

       if user_menu_choice == "1":
        view_all_recipes()

       elif user_menu_choice == "2":
        view_recipe_details()

       elif user_menu_choice == "3":
        add_recipe(recipe_storage)

       elif user_menu_choice == "4":
        print("GOODBYE!")
       break
  else:
   print("Invalid choice, please select between 1 and 4.")
main()
   