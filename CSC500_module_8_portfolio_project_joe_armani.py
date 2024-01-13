# CSC500 - module 8 portfolio project - Joe Armani
from decimal import Decimal, InvalidOperation

# Part 1: Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name='none', item_description='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
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

# Part 4: Build the Shopping Cart class
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        ''' Initializes the shopping cart with a customer name, current date, and an empty list of items.'''
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item_to_purchase):
        ''' Adds an item to the cart_items list.'''
        if item_to_purchase is not None:
            self.cart_items.append(item_to_purchase)
        else:
            print('Error: item to purchase is missing.')
    
    def remove_item(self, item_name):
        ''' Removes all items with item_name from the cart_items list.'''
        initial_cart_items_length = len(self.cart_items)
        self.cart_items = [item for item in self.cart_items if item.item_name != item_name]
        if len(self.cart_items) == initial_cart_items_length:
            print('Item not found in cart. Nothing removed.')
        else:
            print(f'{item_name} removed from cart.')
    
    def modify_item(self):
        ''' 
        Modifies an item's description, price, and/or quantity. Per CTA prompt: "If the item can be found (by name) in the cart,
        check if any of the item's attributes need to be modified.
        If so, modify the item and output the new description, price, and/or quantity of the modified item."
        '''
        item_name_to_modify = get_item_name()
        item_found = False
        for item in self.cart_items:
            if item.item_name.lower() == item_name_to_modify.lower():
                item_found = True
                
                print(
                    f'\nFOUND item {item.item_name} with details:\n'
                    f'   Description: {item.item_description}\n'
                    f'   Price: {item.item_price}\n'
                    f'   Quantity: {item.item_quantity}\n'
                )
                
                if item.item_description != 'none':
                    description_input = get_item_description('Type the new description or press enter to leave it unchanged: ', True)
                    if description_input:
                        item.item_description = description_input

                if item.item_price != 0:
                    price_input = get_item_price('Type the new item price or press enter to leave it unchanged: ', True)
                    if price_input:
                        item.item_price = price_input

                if item.item_quantity != 0:
                    quantity_input = get_item_quantity('Type the new item quantity or press enter to leave it unchanged:', True)
                    if quantity_input:
                        item.item_quantity = quantity_input

                print(
                    f'\nSUCCESS! Modified {item.item_name} with new details:\n'
                    f'   Description: {item.item_description}\n'
                    f'   Price: {item.item_price}\n'
                    f'   Quantity: {item.item_quantity}\n'
                )
                return
        if not item_found:
            print('Item not found in cart. Nothing modified.')
        
    def get_num_items_in_cart(self):
        ''' Returns the number of items in the cart_items list.'''
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        ''' Returns the total cost of the items in the cart_items list.'''
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        ''' Outputs the total cost of items in the cart_items list. If the cart is empty, outputs "SHOPPING CART IS EMPTY" instead.'''
        formatted_header = f'{self.customer_name}\'s Shopping Cart - {self.current_date}'
        header_length = len(formatted_header)
        total_cost = self.get_cost_of_cart()
        print()
        print('OUTPUT SHOPPING CART'.center(header_length))
        if total_cost != 0:
            divider = '-' * header_length
            print(divider)
            print(formatted_header)
            print(f'Number of Items: {self.get_num_items_in_cart()}'.center(header_length))
            for item in self.cart_items:
                print(f'{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}'.center(header_length))
            print(f'Total: ${total_cost}'.center(header_length))
            print(divider)
        else:
            empty_cart_notification = 'SHOPPING CART IS EMPTY'
            divider = '-' * len(empty_cart_notification)
            print(divider)
            print(empty_cart_notification)
            print(divider)
            
    def print_descriptions(self):
        ''' Outputs each item's description in the cart_items list.'''
        formatted_header = f'{self.customer_name}\'s Shopping Cart - {self.current_date}'
        header_length = len(formatted_header)
        divider = '-' * header_length
        print()
        print('OUTPUT ITEMS\' DESCRIPTIONS'.center(header_length))
        print(divider)
        print(formatted_header.center(header_length))
        print('Item Descriptions'.center(header_length))
        if self.get_num_items_in_cart() != 0:
            for item in self.cart_items:
                print(f'{item.item_name}: {item.item_description}'.center(header_length))
            
            print(divider)
        else:
            empty_cart_notification = 'SHOPPING CART IS EMPTY'
            divider = '-' * len(empty_cart_notification)
            print(divider)
            print(empty_cart_notification)
            print(divider)
            
# define the item entry and validation functions
def enter_item():
    while True:
        item_name = get_item_name()
        item_description = get_item_description()
        item_price = get_item_price(item_name)
        item_quantity = get_item_quantity(item_name)
        
        if confirm_item(item_name, item_price, item_quantity):
            return ItemToPurchase(item_name, item_description, item_price, item_quantity)

def get_item_name(input_prompt='Enter the item name: '):
    while True:
        item_name = input(input_prompt) 
        if not item_name:
            print('Item name cannot be empty. Please enter an item name: ')
            continue
        return item_name

# modified to accept an optional is_update parameter -> use in modify_item()
def get_item_description(input_prompt='Enter the item description: ', is_update=False):
    while True:
        item_description = input(input_prompt)
        # if this is an update and the user didn't enter a description, return early
        if is_update and not item_description:
            return None
        if not item_description:
            print('Item description cannot be empty. Please enter an item description: ')
            continue
        return item_description

# modified to accept an optional is_update parameter -> use in modify_item()
def get_item_price(item_name, is_update=False):
    while True:
        item_price_input = input(f'Enter the cost for {item_name} in the format XX.XX: ')
        # if this is an update and the user didn't enter a price, return early
        if is_update and not item_price_input:
            return None
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

# modified to accept an optional is_update parameter -> use in modify_item()
def get_item_quantity(item_name, is_update=False):
    while True:
        try:    
            quantity_input_string = input(f'Enter the quantity for {item_name} ')
            # if this is an update and the user didn't enter a quantity, return early
            if is_update and not quantity_input_string:
                return None
            quantity = int(quantity_input_string)
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
            
            
# step 5: Implement the print_menu() function
def print_menu(shopping_cart):
    ''' Prints the menu of options for the shopping cart program.'''
    menu = (
        '\nMENU\n'
        'a - Add item to cart\n'
        'r - Remove item from cart\n'
        'c - Change item details\n'
        'i - Output items\' descriptions\n'
        'o - Output shopping cart\n'
        'q - Quit\n'
    )
    menu_selection = ''
    while menu_selection.lower() != 'q':
        print(menu)
        try:
            menu_selection = input('Choose an option or type \'q\' to quit: ')
            if menu_selection == 'a':
                shopping_cart.add_item(enter_item())
            elif menu_selection == 'r':
                item_name = input('Enter name of item to remove: ')
                shopping_cart.remove_item(item_name)
            elif menu_selection == 'c':
                shopping_cart.modify_item()
            elif menu_selection == 'i':
                shopping_cart.print_descriptions()
            elif menu_selection == 'o':
                shopping_cart.print_total()
            elif menu_selection == 'q':
                print('\nGoodbye.')
            else:
                print('\nInvalid selection. Please try again.')
        except Exception as e:
            print(f'\nError: {e}')

# step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.
def main():
    ''' Runs the main program.'''
    customer_name = input('Enter customer\'s name: ')
    current_date = input('Enter today\'s date in the format "January 1, 2020": ')
    print(f'\nCustomer name: {customer_name}')
    print(f'Today\'s date: {current_date}')
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)
    
    '''
    Parts 2 and 3: These are from Milestone 1 of the assignment. Requirements were different for Milestone 2 above. 
    '''
    
    # Part 2: prompt the user for two items and create two ItemToPurchase objects
    # This array holds the two ItemToPurchase objects. the enter_item() function returns an ItemToPurchase object wach time it is called
    print('PART 1 REQUIREMENTS - INCLUDED FOR COMPLETENESS')
    itemsToPurchase = []

    for i in range(2):
        itemsToPurchase.append(enter_item())

    # Part 3: calculate and output the total cost
    LINE_LENGTH = 45 # constant -> item_name (20) + quantity (3) + other chars (9) + price (6) + total (7) in format string

    print(f'-' * LINE_LENGTH)
    print(f'TOTAL COST - RECEIPT'.center(LINE_LENGTH))
    print(f'-' * LINE_LENGTH)
    total = Decimal('0.00') # Decimal avoids floating point errors
    for item in itemsToPurchase:
        item.print_item_cost()
        total += item.item_total
    print(f'-' * LINE_LENGTH)
    print(f'Total: ${total:.2f}'.center(LINE_LENGTH))
    print(f'-' * LINE_LENGTH)

if __name__ == '__main__':
    main()