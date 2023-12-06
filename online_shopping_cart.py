from decimal import Decimal, InvalidOperation

# Part 1 define the ItemToPurchase class
# The ItemToPurchase class has three attributes defined in the CTA
# One additional attribute (item_total) is defined for convenience & readability 
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_total = item_price * item_quantity

    def print_item_cost(self):
        formatted_line = (
            f'{self.item_name.ljust(20)} '
            f'{str(self.item_quantity).rjust(3)} @ '
            f'${self.item_price:>{6}.2f} = ${self.item_total:>{7}.2f}'
        )
        print(formatted_line)
        
        
# define the item entry and validation functions
def enter_item():
    while True:
        item_name = get_item_name()
        item_price = get_item_price(item_name)
        item_quantity = get_item_quantity(item_name)
        
        if confirm_item(item_name, item_price, item_quantity):
            return ItemToPurchase(item_name, item_price, item_quantity)

def get_item_name():
    while True:
        item_name = input('Enter the item name: ')
        if not item_name:
            print('Item name cannot be empty. Please enter an item name: ')
            continue
        return item_name

def get_item_price(item_name):
    while True:
        item_price_input = input(f'Enter the cost for {item_name} in the format XX.XX: ')
        item_price_cleaned = item_price_input.replace('$', '').replace(',', '')
        try:
            price = Decimal(item_price_cleaned)
            # confirm the price has two decimal places
            if price.as_tuple().exponent != -2:
                print('Please enter a price in the format XX.XX (it must have two decimal places).')
            elif price < 0:
                print('Price cannot be negative. Please enter a positive price.')
            else:
                return price
        except InvalidOperation:
            print('Numbers only. Please enter a valid price.')

def get_item_quantity(item_name):
    while True:
        try:    
            quantity = int(input(f'Enter the quantity for {item_name} '))
            if quantity <= 0:
                print('Quantity must be positive. Please enter a positive quantity.')
                continue
            return quantity
        except ValueError:
            print('Whole numbers only. Please enter a valid quantity.')

def confirm_item(item_name, item_price, item_quantity):
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


# Part 2: prompt the user for two items and create two ItemToPurchase objects
# This array holds the two ItemToPurchase objects. the enter_item() function returns an ItemToPurchase object wach time it is called
itemsToPurchase = []

for i in range(2):
    itemsToPurchase.append(enter_item())

# Part 3: calculate and output the total cost
LINE_LENGTH = 45 # constant -> item_name (20) + quantity (3) + other chars (9) + price (6) + total (7) in format string

print(f'-' * LINE_LENGTH)
print(f'TOTAL COST - RECEIPT'.center(LINE_LENGTH))
print(f'-' * LINE_LENGTH)
total = Decimal('0.00') # Decimal aviods floating point errors
for item in itemsToPurchase:
    item.print_item_cost()
    total += item.item_total
print(f'-' * LINE_LENGTH)
print(f'Total: ${total:.2f}'.center(LINE_LENGTH))
print(f'-' * LINE_LENGTH)