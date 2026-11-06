cooking = {}

quest_0 = input(
  "If you want to Add Recipe, press 'Add'\n" \
  "If you want to View Recipe, pres 'View' "
)
print()

# Add receipe
def add_food():
    quest_1 = int(input('How many food do you want to prepare? '))
    for i in range(1, quest_1 + 1):
        quest_2 = input(f'What is the name of the {i} food? ').capitalize()
        quest_3 = input(f'Wkhat are the ingredinet used in preparing the {i} food? ')
        quest_4 = input(f'Instructions for cooking the {i} food? ')

        food = {
        'Name': quest_2,
        'Ingredient':  quest_3, 
        'Instructions':  quest_4
                }
        print()
        cooking[i] = food

    for key, values in cooking.items():
        print(f'Name: {values['Name']}')
        print(f'Ingredient: {values['Ingredient']}')
        print(f'Instructions: {values['Instructions']}')
        print()

# View receipe
def view_recipe():
    if not cooking:
       print('No recipe avaliable')
       return
    
    for key, items in cooking.items():
      print(f'Name: {items['Name']}')
      print(f'Ingredient: {items['Ingredient']}')
      print(f'Instructions: {items['Instructions']}')
      print()


final = quest_0.strip().lower()

if final == 'add':
 add_food()

elif final == 'view':
 view_recipe()

