task_storage = {}

quest_1 = int(input('How many task do you want to crea'))

def create_task(title, description, deadline =None, status=None, ):
    task = {
        'title': title,
        'description': description, 
        'time limit': deadline,
        'status': status
    } 
    print(task)



def read_task():
    task_storage.append()

create_task('Food', 'Yam and egg')

    