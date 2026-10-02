task_storage = {}

def create_task (day, week, month, year):
    task ={
 'day': day, 
 'week': week,
 'month': month,
 'year': year
    }
    task_ID = max(task_storage.keys(), default = 0) + 1
    task_storage[task_ID] = task
    print(f'{task_ID}: {day}, {week}, {month}, {year}')
  
quest_1 = int(input('How many task do you want to create? '))

for i in range(quest_1):
    print(f'\n--- Enter details for task {i + 1}---')
    day = input('Enter any day- ' )
    week = input('Enter any week (e.g ...2nd):- ' )
    month = input('Enter any month- ' )
    year = int(input('Enter any year- '  ))
    create_task(day, week, month, year) 



