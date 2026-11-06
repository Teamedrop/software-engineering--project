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

cooking = {}

def save_recipe():
    with open('recipes.json', 'w') as file:
        json.dump(cooking, file, indent=4)

# Read in JSON
with open('recipes.json', 'r') as file:
    json.load(file)

def add_recipe():
    recipe = {
        'Name': 'Fried rice',
        'Ingredient': ['Pepper', 'Rice', 'Salt'],
        'Instructions': 'Cook it very well'
    }
    

    cooking = recipe
    print(cooking)

add_recipe()
save_recipe()    