import json

Recipe = {
    1: {'Name': 'Jollof rice', 'Ingredients': ['Rice', 'Water', 'Salt', 'Curry'], 'Instructions': 'Cook it very well'},
    2: {'Name': 'Fried rice', 'Ingredients': ['Rice', 'Beef', 'Colouring', 'Green peas'], 'Instructions': 'Cook in a neat environment' }
}

quest_0 = input('Do you want to View recipe or Add recipe or Search recipe? ')


# Save in Json
def save_recipe():
 with open('Recipe_book.json', 'w') as file:
    json.dump(Recipe, file, indent = 4 )

# Add and save in Json
def add_recipe():
 quest_1 = input('What is the name of the food? ').capitalize()
 quest_2 = input('What are the ingredients used in preparing the food? ').capitalize()
 quest_3 = input('What are the instructions you need to follow to cook the food? ').capitalize()

 Recipes = {
   'Name': quest_1,
   'Ingredients': quest_2,
   'Instructions': quest_3
 }
 new_recipe = len(Recipe) + 1 

 Recipe[new_recipe] = Recipes

# View recipe
def view_recipe():
  with open('Recipe_book.json','r') as file:
    content = json.load(file)
    print(content)


# Search recipe
def search_recipe():
 quest_4 = input("What's the name of the food you want to search for? ").strip().lower()

 with open('Recipe_book.json','r') as file:
  info = json.load(file)

  for i in info.values():
     if quest_4 == i['Name'].lower():
      print('Name:', i['Name'])
      print('Ingredients:', i['Ingredients'])
      print('Instructions:', i['Instructions'])
  else: 
       print('Food recipe not found')
           

choice = quest_0.strip().lower()

if choice in ['add', 'add recipe']:
 add_recipe()
 save_recipe()

elif choice in ['view', 'view recipe']:
  view_recipe()

elif choice in ['search', 'search recipe']:
  search_recipe()

else:
  print('Invalid request')  