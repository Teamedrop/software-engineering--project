import math

Operations = input('What operations do you want to perform on? ')

if Operations.strip().lower() in ['addition', 'add', 'sum', 'plus']:
        Add = 'add'

elif Operations.strip().lower() in ['subtraction', 'minus', 'subtract']:
        Sub = 'subtract'

elif Operations.strip().lower() in ['division', 'divide', 'take away']:
        Div = 'divide'

elif Operations.strip().lower() in ['multiplication', 'multiply', 'times']:
        Mul = 'multiply'

elif Operations.strip().lower() == 'modulus':
        Mod = 'Module'

elif Operations.strip().lower() in ['raise to power', 'power of', 'power', 'cube']:
        Pow = 'Power'

elif Operations.strip().lower() in ['square of', 'square']:
        Squ = 'Square'

if Operations.strip().lower() in ['addition', 'add', 'sum', 'plus']:
        no = int(input(f'How many numbers do you want to {Add}? '))

elif Operations.strip().lower() in ['subtraction', 'minus', 'subtract']:
        n = int(input(f'How many numbers do you want to {Sub}? '))

elif Operations.strip().lower() in ['division', 'divide', 'take away']:
        n = int(input(f'How many numbers do you want to {Div}? '))

elif Operations.strip().lower() in ['multiplication', 'multiply', 'times']:
        n = int(input(f'How many numbers do you want to {Mul}? '))

elif Operations.strip().lower() == 'modulus':
            n = int(input(f'How many numbers do you want to {Mod}? '))        

elif Operations.strip().lower() in ['raise to power', 'power of', 'power']:
        n  = int(input(f'How many numbers do you want to {Pow}? '))


# For Addition
value = []
if Operations.strip().lower() in ['addition', 'add', 'sum', 'plus']:
            for _ in range(no):
                    val = int(input("Enter your number: "))
                    value.append(val)
            Addition = sum(value)

            print(f"Your final answer is {Addition}")      


 # For Subtraction           
elif Operations.strip().lower() in ['subtraction', 'minus', 'subtract']:
        First_sub = int(input('Enter the first number: '))

        for i in range(2, n + 1):
                number_sub = int(input(f'Enter your {i} number: '))
                First_sub -= number_sub

        print(f'Your final answer is {First_sub}')                


# For Division
elif Operations.strip().lower() in ['division', 'divide', 'take away']:
        First_div = int(input('Enter your first number: '))

        for i in range(2, n + 1):
                number_div = int(input(f'Enter your {i} number: '))
                First_div /= number_div

        print(f'Your final answer is {First_div}')          


# For Multiplication
elif Operations.strip().lower() in ['multiplication', 'multiply', 'times']:
        First_mul = int(input('Enter your first number: '))

        for i in range(2, n + 1):
                number_mul = int(input(f'Enter your {i} number: '))
                First_mul *= number_mul

        print(f'Your final answer is {First_mul}')       


# For Modulus
elif Operations.strip().lower() == 'modulus':
        first_mod = int(input('Enter your first number: '))

        for i in range (2, n + 1):
                number_mod = int(input(f'Enter your {i} number: '))
                total_mod = first_mod % number_mod

        print(f'Your final answer is {total_mod}')        


# For Power
elif Operations.strip().lower() in ['raise to power', 'power of', 'power']:
        first_pow = int(input('Enter your first number: '))

        for i in range(2, n + 1):
                number_pow = int(input(f'Enter your {i} number: '))
                first_pow **= number_pow

        print(f'Your final answer is {first_pow}')   


# For Square and Cube
elif Operations.strip().lower() in ['square of', 'square', 'cube']:
        first_squ = int(input('Enter your base number: '))
        second_squ = int(input('Enter your power number: '))
        total_squ = first_squ ** second_squ
        print(f'Your final answer is {total_squ}')        


# For Square root
elif Operations.strip().lower() == 'square root':
        first_sqr = int(input('Enter your number: '))
        total_sqr = first_sqr ** 0.5
        print(f'Your final answer is {total_sqr}')


 # For Cube root
elif Operations.strip().lower() == 'cube root':
        first_cub = int(input('Enter your number: '))
        total_cub = round(first_cub ** (1/3), 2)
        print(f'Your final answer is {total_cub}')


# For absolute value
elif Operations.strip().lower() == 'absolute value':
        first_abs = int(input('Enter your number: '))
        total_abs = abs(first_abs)
        print(f'Your final answer is {total_abs}')       


# For reciprocal
elif Operations.strip().lower() == 'reciprocal':
        first_rec = int(input('Enter your number: '))
        total_rec = round(1 / (first_rec), 4)
        print(f'Your final answer is {total_rec}')


# For percentage
elif Operations.strip().lower() == 'percentage':
        first_per = int(input('Enter your number: '))
        second_per = int(input('Enter your percentage: '))
        total_per = first_per * (second_per / 100)
        print(f'Your final answer is {total_per}')


# For logarithm
elif Operations.strip().lower() == 'logarithm':
        first_log = int(input('Enter your number: '))
        second_log = int(input('Enter your base number: '))
        total_log = math.log(first_log , second_log)
        print(f'Your final answer is {total_log}') 
