number_list = []
number_list1 =[]
quest_0 = input('Which operation do you want to perform? ')

#For cube root
if quest_0.lower().strip() == 'cube root':
    def cube_root():
        quest_1 = int(input('Which number do you want to find the cube root of? '))
        return quest_1 **(1/3)
    print(f'Your answer is {cube_root()}')
    print()
    quest_2 = input('Do you want to continue the operation? \n If YES, press Y \n If NO, press N ')
    if quest_2.lower().strip() == 'y':
        quest_3 = int(input('Which number do you want to find the cube root of? '))
        total_1 = float(quest_3 **(1/3))
        print(f'Your answer is {total_1}')
    elif quest_2.lower().strip() == 'n':
        print('Operation ended, thank you')

#For addition
if quest_0.lower().strip() in ['add', 'addition', 'sum']:
    def add():
        quest_4 = int(input('How many numbers do you want to add? '))
        for i in range(quest_4):
            ans = int(input(f'Enter your {i+1} number '))
            number_list.append(ans)

        total_ans = sum(number_list)
        print(f'Your answer is {total_ans}')
        print()

        quest_5 = input('Do you want to continue the operation. \n If YES press Y \n If NO press N ')
        if quest_5.strip().lower() == 'y':
         quest_6 = int(input('How many number/s do you want to add? '))
         for i in range(quest_6):
            quest_7 = int(input(f'Enter your {i +1} number '))
            number_list1.append(quest_7)

            final_add = sum(number_list1)
            print(f'Your answer is {final_add}')
            
        elif quest_5.strip().lower() == 'n':
         print('Operation ended, thank you')   

#For Subtraction 
if quest_0.strip().lower() in ['subtract', 'sub', 'subtraction', 'minus']:
   def sub():
    quest_8 = int(input('How many numbers do you want to subtract? '))
    quest_9 = int(input('Enter your first number: '))
    for i in range(2, quest_8 +1):
      quest_10 = int(input(f'Enter your {i} number: '))
      quest_9 -= quest_10
    print(f'Your total answer is {quest_9}')      
    print()
    quest_11 = input('Do you want to continue the operation. \n If YES press Y \n If NO press N ')
    if quest_11.strip().lower() == 'y':
       quest_12 = int(input('How many numbers do you want to subtract? '))
       quest_13 = int(input('Enter your first number '))
       for i in range(2, quest_12 +1):
          quest_14 = int(input(f'Enter your {i} number '))
          quest_13 -= quest_14
          print(f'Your final answer is {quest_13}')
    elif quest_11.strip().lower() == 'n':
          print('Operation ended, thank you')

#For multiplication 
if quest_0.strip().lower() in ['multiply', 'times', 'multiplication']:
   def multiply():
    quest_13 = int(input('How many numbers do you want to multiply? '))
    quest_14 = int(input('Enter your first number? '))
    for i in range(2, quest_13 + 1):
      quest_15 = int(input(f'Enter your {i} number: '))
      quest_14 *= quest_15
      print(f'Your final answer is {quest_14:.2f}')
      print()
    quest_16 = input('Do you want to continue the operation. \n If YES press Y \n If NO press N ')
    if quest_16.strip().lower() == 'y':
     quest_17 = int(input('How many numbers do you want to multiply'))
     quest_18 = int(input('Enter your first number? '))
     for i in range(2, quest_17 + 1):
      quest_19 = int(input(f'Enter your {i} number: '))
      quest_18 *= quest_19
      print(f'Your final answer is {quest_18:.4f}')
    elif quest_16.strip().lower() == 'n':
       print('Operation ended, thank you')

#For Division
if quest_0.strip().lower() in ['divide', 'division']:
   def division():
    ask_1 = int(input('How many numbers do you want to divide? '))
    ask_2 = float(input('Enter your first number? '))
    for i in range(2, ask_1 + 1):
      ask_3 = float(input(f'Enter your {i} number: '))
      ask_2 /= ask_3
      print(f'Your final answer is {ask_2:.4f}')
      print()
      ask_4 = input('Do you want to continue the operation. \n If YES press Y \n If NO press N ')
      if ask_4.strip().lower() == 'y':
         ask_5 = int(input('How many numbers do you want to divide? '))
         ask_6 = float(input('Enter your first number? '))
         for i in range(2, ask_5 + 1):
          ask_7 = float(input(f'Enter your {i} number: '))
          ask_6 /= ask_7
          print(f'Your final answer is {ask_6:.4f}')
      elif ask_4.strip().lower() == 'n':
         print('Operation ended, thank you') 


         
choice = quest_0.strip().lower()
if choice in ['add', 'addition', 'sum']:
   add()

if choice in ['subtract', 'sub', 'subtraction', 'minus']:
   sub()

if choice == 'cube root':
   cube_root()

if choice in ['multiply', 'times', 'multiplication']:
   multiply()

if choice in ['divide', 'division']:
   division()

else:
   print('Invalid character! ')
       




