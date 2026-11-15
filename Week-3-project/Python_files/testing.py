#with open('reading', 'w') as file:
 #file.write('I am learning c')
 

#with open('reading', 'r') as file:
 #content = file.read()
 #print(content)

#rewrite = content.replace('c', 'python')

#with open('reading', 'w') as file:
 #file.write(rewrite)

#print('Edited successfully')

#import json

# with open ('recipe.json', 'r') as file:
     # json.dump(cooking, file, indent=4)

#with open('recipe.json', 'r') as file:
    #content = json.load(file)
    #print(content['Name'])
    #for i in content['Ingredient']:
        #print(i)
    #print(content['Instructions'])    
import json

cooking = {
    1 : {'Name': 'Fried rice', 'Ingredients': ['rice', 'salt', 'pepper']},
    2 : {'Name': 'Beans', 'Ingredients': ['beans', 'onions', 'oil']}
}

quest_1 = input('Which food recipe do you want to edit? ').strip().lower()

found = False

for keys, values in cooking.items():
    if values['Name'].lower() == quest_1:
        quest_2 = input('What is the name of the new food? ')
        quest_3 = input('What is/are the ingredient(s) of the new food? ').split(',')

        values['Name'] = quest_2
        values['Ingredients'] = quest_3

        

        with open('testing.json','w') as file:
             json.dump(cooking, file, indent= 4)
             print('Recipe updated sucessfully! ')


        found = True
        break
    
else:
        print(' Recipe not found')