tasks = []

print('Which task or tasks do you want to perform? ')
print()

mod_1 = input('If it is add_task, read_task and update_task, Enter A...... ' \
'If it is add_task, read_task and delete_task, Enter B  ')

a = 'add_task, read_task and update_task'
b = 'add_task, read_task and delete_task'

quest_0 = int(input('How many task or tasks do you want to perform? '))


def add_tasks():
    for i in range(1, quest_0 + 1):
      quest_1 = input('Which task or tasks do you want to perform? ')
      tasks.append(quest_1)

def read_tasks():
    print(', ' .join(tasks))

def update_tasks():
    quest_2 = int(input('Which number of task do you want update? '))
    index = quest_2 - 1
    quest_3 = input('What do you want to update it to? ')
    if 0 <= index < len(tasks):
     tasks[index] = quest_3


def delete_task():
   quest_4 = int(input('Which number of task do you want to delete? '))
   index_1 = quest_4 - 1
   if 0 <= index_1 < len(tasks):
      delete = tasks.pop(index_1)


choice = mod_1.strip().upper()

if choice == 'A':
   add_tasks()
   read_tasks()
   update_tasks()
   read_tasks()
   print('Added succesfully')     


elif choice == 'B':
   add_tasks()
   read_tasks()
   delete_task()
   read_tasks()
   print('Deleted successfully')

else:
   print('Invalid character selected.') 

