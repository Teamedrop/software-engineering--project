details = {}
names = []

quest_1 = input('Which operaton do you want to perform? ')

if quest_1.strip().lower() == 'add student':

 def add_student():
  quest_2 = int(input('How many students details do you want to add? '))
  for i in range (1, quest_2 + 1):
   quest_3 = input(f'Enter your {i} student name: ').capitalize()
   quest_4 = input(f'Enter your {i} student position: ')
   quest_5 = input(f'Enter your {i} student score: ')
   student = {
    'Name': quest_3,
    'Grade': quest_4,
    'Score': quest_5
   }
   details[i] = student

  sorted_data = sorted(details.values(), key = lambda x: x['Name'])

  for student in sorted_data:
   
    print(f'Your student grade is:')
    print(f'Name: {student['Name']}')
    print(f'Postion: {student['Grade']}')
    print(f'Score: {student['Score']}')
    print()

  print('Do you want to find the highest score among the students? ')
  quest_7 = input('If YES, press Y \n If NO, press N')
    
  if quest_7.strip().lower() == 'y':
         top_student = sorted(details.values(), key = lambda x: x['Score'], reverse = True)
         for student in top_student:
          print('The highest student to the lowest ')
          print(f'Name: {student['Name']}')
          print(f'Position: {student['Grade']}')
          print(f'Score: {student['Score']}')

  elif quest_7.strip().lower() == 'n':
    print('Operation ended, thank you')        

   







  

 


  

add_student()   
