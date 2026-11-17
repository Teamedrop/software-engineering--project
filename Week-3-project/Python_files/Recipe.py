import json

Recipe = {
    1: {'Name': 'Jollof rice', 'Ingredients': ['Rice', 'Water', 'Salt', 'Curry'], 'Instructions': 'Cook it very well'},
    2: {'Name': 'Fried rice', 'Ingredients': ['Rice', 'Beef', 'Colouring', 'Green peas'], 'Instructions': 'Cook in a neat environment' }
}



# Save in Json
def save_recipe():
 with open('Recipe_book.json', 'w') as file:
    json.dump(Recipe, file, indent = 4 )

# Add and save in Json
def add_recipe():
 quest_1 = input('What is the name of the food? ').capitalize()
 quest_2 = input('What are the ingredients used in preparing the food? ').capitalize()
 quest_2_1 = quest_2.split(',')
 quest_3 = input('What are the instructions you need to follow to cook the food? ').capitalize()
 quest_3_1 = quest_3.split(',')

 Recipes = {
   'Name': quest_1,
   'Ingredients': quest_2_1,
   'Instructions': quest_3_1
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

  found = False 
  
 for i in info.values():
     if quest_4 == i['Name'].lower():
      print('Name:', i['Name'])
      print('Ingredients:', i['Ingredients'])
      print('Instructions:', i['Instructions'])
      found = True
      break 
     
 if not found: 
      print('\n')
      print('Food recipe not found')


# Edit recipe
def edit_recipe():
  quest_6 = input('Which food recipe do you want to edit? ')

  for values in Recipe.values():
    if values['Name'].lower() == quest_6:

      quest_7 = input('Enter your new food name: ')
      quest_8 = input('Enter your new food ingredient(s): ')
      quest_9 = input('Enter your new foood instructions: ')

      values['Name'] = quest_7
      values['Ingredients'] = quest_8

      save_recipe()

  else: 
      print('Food recipe not found')
           



while True:
  print("\n Recipe Book: ")
  print('1. Add recipe ')
  print('2. View recipe ')
  print('3. Search recipe ')
  print('4. Edit recipe ')
  print('0. Exist ')

  quest_5 = input('Type the function you want to use or use the number: ').strip().lower().capitalize()

  if quest_5 == '1' or quest_5 in ['add recipe', 'add']:
    add_recipe()
    save_recipe()

  elif quest_5 == '2' or quest_5 in ['view recipe', 'view']:
    view_recipe()

  elif quest_5 == '3' or quest_5 in ['search recipe', 'search']:
    search_recipe()

  elif quest_5 == '4' or quest_5 in ['edit', 'edit recipe']:
    edit_recipe()  

  elif quest_5 == '0' or quest_5 == 'exist':
    print('Goodbye your recipe are saved! ')
    break 

  else:
    print('Invalid selection, please enter 1, 2, 3, 4 or 0')   



