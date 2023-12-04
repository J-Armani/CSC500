# Module 3 Assignment - Joseph Armani
import sys
# Part 1 - Calculate a restaurant bill

# build a function to accept user-entered items. Perform basic validation.
# Get the item name, quantity, and price. Confirm the entry. Then build a dictionary of confirmed items.
def enter_items():
    ordered_items = {}

    while True:
        item_name = get_item_name()
        if item_name is None:
            break

        item_quantity = get_item_quantity(item_name)
        item_price = get_item_price(item_name)
        
        if confirm_item(item_name, item_quantity, item_price):
            item_total = item_quantity * item_price
            ordered_items[item_name] = [item_quantity, item_price, item_total]

    return ordered_items

def get_item_name():
    while True:
        item_name = input('Enter the item name. Type \'done\' or \'quit\' when finished: ')
        if (item_name.lower() in ['done', 'quit']):
            return None
        if not item_name:
            print('Please enter an item name. Type \'done\' or \'quit\' when finished.')
            continue
        return item_name

def get_item_quantity(item_name):
    while True:
        try:    
            return int(input(f'Enter the quantity for {item_name} '))
        except ValueError:
            print('Whole numbers only. Please enter a valid quantity.')

def get_item_price(item_name):
    while True:
        item_price_input = input(f'Enter the cost for {item_name} in the format XX.XX: ')
        item_price_cleaned = item_price_input.replace('$', '').replace(',', '')
        try:
            return float(item_price_cleaned)
        except ValueError:
            print('Numbers only. Please enter a valid price.')

def confirm_item(item_name, item_quantity, item_price):
    while True:
        confirmation = input(f'You entered {item_quantity} {item_name} at ${item_price} each. Is this correct? (y/n) ')
        if confirmation.lower() == 'y':
            print(f'{item_name} entry confirmed.')
            return True
        elif confirmation.lower() == 'n':
            print(f'{item_name} entry cancelled.')
            return False
        else:
            print('Please enter \'y\' or \'n\'.')

# build functions to calculate the tip, tax, and total
def calculate_tip(bill_amount):
    return bill_amount * .18

def calculate_tax(bill_amount):
    return bill_amount * .07

def calculate_total(bill_amount, tip_amount, tax_amount):
    return bill_amount + tip_amount + tax_amount


# run the program
billed_items = enter_items()

# exit if no items entered
if not billed_items:
    print('No items entered. Exiting.')
    sys.exit()

# lay out the bill    
left_width = max(len(item_name) for item_name in billed_items) + 20  # Width for item_name, item_quantity, item_price plus whitespace.
right_width = 15  # Width for total cost.

# header
print('\n' + '--- Your Bill ---'.center(left_width + right_width) + '\n')

# calculate and print the line items
billed_items_total = 0
for item_name, itemization in billed_items.items():
    billed_items_total += itemization[2]
    left_aligned = f'{item_name} x {itemization[0]} @ ${itemization[1]:.2f} ea.'
    right_aligned = f'${itemization[2]:.2f}'
    line_item = left_aligned.ljust(left_width) + right_aligned.rjust(right_width)
    print(line_item)

# tax, tip, total
tip = calculate_tip(billed_items_total)
tax = calculate_tax(billed_items_total)
grand_total = calculate_total(billed_items_total, tip, tax)

# print the bill totals
print('-' * (left_width + right_width))
print('Subtotal:'.ljust(left_width) + f'${billed_items_total:.2f}'.rjust(right_width))
print('Tax (7%):'.ljust(left_width) + f'${tax:.2f}'.rjust(right_width))
print('Tip (18%):'.ljust(left_width) + f'${tip:.2f}'.rjust(right_width))
print('-' * (left_width + right_width))
print('Total:'.ljust(left_width) + f'${grand_total:.2f}'.rjust(right_width))
print('\n' + '--- Thank You! ---'.center(left_width + right_width))


# Part 2 - Setting an alarm clock
# User enters the current time and the number of hours to wait. We use the modulo operator to calculate the alarm time (24 hour clock).
def get_time(time_type):
    while True:
        try:
            return int(input(f'Enter the {time_type}: '))
        except ValueError:
            print('Whole numbers only. Please enter a valid time.')

def get_am_pm(time):
    return 'A.M.' if time < 12 else 'P.M.'
    
def get_standard_time(input_time):
    standard_time = input_time % 12
    return 12 if standard_time == 0 else standard_time

# get the current time from the user, then calculate the standard time equivalent
current_continental_time = get_time('current continental time (24 hour clock) in hours') % 24
current_am_pm = get_am_pm(current_continental_time)
current_standard_time = get_standard_time(current_continental_time)

# get the number of hours to wait from the user and calculate the wait time in days and hours
alarm_wait_time = get_time('number of hours to wait for the alarm')
days_until_alarm = alarm_wait_time // 24
hours_until_alarm = alarm_wait_time % 24
hours_string = 'hour' if alarm_wait_time == 1 else 'hours'
days_string = 'day' if days_until_alarm == 1 else 'days'

# calculate the alarm time in continental and standard time
alarm_continental_time = (current_continental_time + alarm_wait_time) % 24
alarm_am_pm = get_am_pm(alarm_continental_time)
alarm_standard_time = get_standard_time(alarm_continental_time)

# display the results
print (f'The current time is {current_continental_time}:00 hours ({current_standard_time}:00 {current_am_pm})')
print (f'Your alarm is set to go off in {alarm_wait_time} hours.')
print(f'Your alarm will sound in {days_until_alarm} {days_string} and {hours_until_alarm} {hours_string} '
      f'at {alarm_continental_time}:00 hours ({alarm_standard_time}:00 {alarm_am_pm})')