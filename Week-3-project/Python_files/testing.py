task_storage = {}

def create_task(title, description, deadline, status ):
     task ={
     'title': title,
     'description': description,
     'deadline': deadline, 
     'status': status
     }      
     task_ID = max(task_storage.keys(), default=0)+ 1
     task_storage[task_ID] = task

def read_task():
      for task_ID, task in task_storage.items():
          print(f'task_ID: {task_ID}')
          print(f'title: {task['title']}')
          print(f'description: {task['description']}')
          print(f'deadline: {task['deadline']}')
          print(f'status: {task['status']}')
     
      quest_1 = int(input('How many task do you want to create? '))

      for i in range(quest_1):
          print(f'Enter the task for {i +1}')
          tit = input('Enter your task title- ')
          des = input('Enter your task description- ')
          deadli = input('Enter your task deadline- ') 
          sta = input('Enter your task status- ')    
          create_task(tit, des, deadli, sta)
          print(f'{tit}, {des}, {deadli}, {sta}')  






def update_task(title, description, deadline=None, status=None):
     quest_1 = int(input('Which task_ID do you want to update? '))
     task_storage[quest_1] = task_storage
     print(f'task ID: {quest_1}')
     print(f'title: {title}')
     print(f'description: {description}')
     print(f'deadline: {deadline}')
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

               

     
read_task()
update_task('Ounje', 'Rice and egg', 'done', 'completed')
read_task()
#delete_task()

    