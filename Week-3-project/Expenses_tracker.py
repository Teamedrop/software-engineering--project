task = []
amt = []
cat = []

a_1 = int(input('How many things did you buy? '))
print()

a_12 = input('If you want to add, read, search and total expenses, type A ' \
' If you want to add, read, search and delete expenses, type B ' \
'If you want to add, read and total expenses, type C ' \
'If you want to add, read and categorize expenses, type D ')
print()


for i in range(1, a_1 + 1):
    a_2 = input('What did you buy? ')
    task.append(a_2)

    a_22 = input('Which category is it under? ')
    cat.append(a_22)
print()

def add_expenses():
    for i in range(len(task)):
     q_1 = int(input(f'How many naria do you spend on {task[i]}? '))
     amt.append(q_1) 
     print()

def read_expenses():
    for item, amount in zip(task, amt): 
     print(f'Your {item} is {amount} naria ')
     print()

def category_expenses():
   for item, catego in zip(task, cat):
    print(f'Your {item} is under {catego} category ')  
print()


def search_expenses():
   q_4 = int(input('How many items are you looking for? '))

   for i in range(q_4):
      q_3 = input('Which item are you looking for? ')
      q_3a = q_3.strip().lower()    
      print() 

      found = False
      for item, amount in zip(task, amt):
         if item.strip().lower() == q_3a:
          print(f'What you are looking for is {item}, which amount to {amount} naira ')
          found = True
          print()

   if not found:
         print(f'Item {q_3} is not found')
         print()

def total_expenses():
  print(f'The total sum of yout items is {sum(amt)}')     

def delete_expenses():
   q_5 = input('Which item do you want to delete? ')   
   q_5a = q_5.strip().lower()

   print('Before deletion:', task)

   for i in range(len(task)):
         if task[i].strip().lower() == q_5a:
          task.pop(i)
          amt.pop(i)
         break    
   print('After deletion:', task) 

choice = a_12.strip().upper()

if choice == 'A':
      add_expenses()
      read_expenses()
      total_expenses()

elif choice == 'B':
   add_expenses()
   read_expenses()
   delete_expenses()

elif choice == 'C':
     add_expenses()
     read_expenses()
     search_expenses()

elif choice == 'D':
     add_expenses()
     read_expenses()
     category_expenses()

