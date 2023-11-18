# Module 1 Part 1: Addition and Subtraction

# build a function to parse user input with basic error handling
def parse_integer(instance):
    while True:
        try:
            return int(input(f'Enter the {instance} number '))
        except ValueError:
            print('Numbers only. Please try again.')

# build the add, subtract, multiply, and divide functions
def add(first_input, second_input):
    print(f'Addition result: {first_input} + {second_input} = {first_input + second_input}')

def subtract(first_input, second_input):
    print(f'Subtraction result: {first_input} - {second_input} = {first_input - second_input}')

def multiply(first_input, second_input):
    print(f'Multiplication result: {first_input} * {second_input} = {first_input * second_input}')

def divide(first_input, second_input):
    try:
        result = first_input / second_input
        print(f'Division result: {first_input} / {second_input} = {result}')
    except ZeroDivisionError:
        print('Can\'t divide by zero. Try a non-zero number next time.')
        return None


# Part 1: Addition and Subtraction
print('Let\'s do some addition and subtraction. Pick any two numbers.')
first_number = parse_integer('first')
second_number = parse_integer('second')

add(first_number, second_number)
subtract(first_number, second_number)
print()

# Part 2: Multiplication and Division
print('Now we\'ll do multiplication and division.')
first_number = parse_integer('first')
second_number = parse_integer('second')

multiply(first_number, second_number)
divide(first_number, second_number)

print('All done! Restart to try again.')
print()