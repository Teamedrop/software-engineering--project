task_storage = {}

def create_task(title, description, deadline, status ):
     task = {
          'title': title,
          'description': description,
          'deadline': deadline,
          'status': status
     }
     task_ID = max(task_storage.keys(), default=0)+ 1
     task_storage[task_ID] = task 
     print(f'{task_ID}: {title}, {description}, {deadline}, {status}')

     quest_1 = int(input('How many task do you want to create? '))

     for i in range(quest_1):
          print(f'Enter your details for task {i + 1}')
          tit = input('Enter the title of your task- ')
          des = input('Enter the description of your task- ')
          deadli = input('Enter the deadline of your task- ')
          sta = input('Enter the status of your task- ')
          create_task(tit, des, deadli,sta)        
          





def read_task():
     for task_ID, task in task_storage.items():
          print(f'task_ID: {task_ID}')
          print(f'title: {task['title']}')
          print(f'description: {task['description']}')
          print(f'deadline: {task['deadline']}')
          print(f'status: {task['status']}')

def update_task(title, description, deadline=None, status=None):
     quest_1 = int(input('Which task_ID do you want to update? '))
     task_storage[quest_1] = task_storage
     print(f'Task ID: {quest_1}')
     print(f'Title: {title}')
     print(f'Description: {description}')
     print(f'Deadline: {deadline}')
     print(f'status: {status}')

def delete_task():
     quest_2 = int(input('Which task ID do you want to delete '))
     try:
          if quest_2 in task_storage:
               task_storage.pop(quest_2)
               print('After deletion:', task_storage)
          else:
               print('Task ID does not exist')    

     except ValueError:
          print('Invalid input: Please enter a number')          

               


#read_task()
#update_task('Ounje', 'Rice and egg', 'done', 'completed')
#delete_task()

    