# from decimal import Decimal, InvalidOperation

# # Part 1 define the ItemToPurchase class
# # The ItemToPurchase class has three attributes defined in the CTA
# # One additional attribute (item_total) is defined for convenience & readability 
# class ItemToPurchase:
#     def __init__(self, item_name='none', item_description='none', item_price=0, item_quantity=0):
#         self.item_name = item_name
#         self.item_description = item_description
#         self.item_price = item_price
#         self.item_quantity = item_quantity
#         self.item_total = item_price * item_quantity

#     def print_item_cost(self):
#         formatted_line = (
#             f'{self.item_name.ljust(20)} '
#             f'{str(self.item_quantity).rjust(3)} @ '
#             f'${self.item_price:>{6}.2f} = ${self.item_total:>{7}.2f}'
#         )
#         print(formatted_line)
        
        
# # define the item entry and validation functions
# def enter_item():
#     while True:
#         item_name = get_item_name()
#         item_description = get_item_description()
#         item_price = get_item_price(item_name)
#         item_quantity = get_item_quantity(item_name)
        
#         if confirm_item(item_name, item_price, item_quantity):
#             return ItemToPurchase(item_name, item_description, item_price, item_quantity)

# def get_item_name(input_prompt='Enter the item name: '):
#     while True:
#         item_name = input(input_prompt) 
#         if not item_name:
#             print('Item name cannot be empty. Please enter an item name: ')
#             continue
#         return item_name

# # modified to accept an optional is_update parameter -> use in modify_item()
# def get_item_description(input_prompt='Enter the item description: ', is_update=False):
#     while True:
#         item_description = input(input_prompt)
#         # if this is an update and the user didn't enter a description, return early
#         if is_update and not item_description:
#             return None
#         if not item_description:
#             print('Item description cannot be empty. Please enter an item description: ')
#             continue
#         return item_description

# # modified to accept an optional is_update parameter -> use in modify_item()
# def get_item_price(item_name, is_update=False):
#     while True:
#         item_price_input = input(f'Enter the cost for {item_name} in the format XX.XX: ')
#         # if this is an update and the user didn't enter a price, return early
#         if is_update and not item_price_input:
#             return None
#         item_price_cleaned = item_price_input.replace('$', '').replace(',', '')
#         try:
#             price = Decimal(item_price_cleaned)
#             # confirm the price has two decimal places
#             if price.as_tuple().exponent != -2:
#                 print('Please enter a price in the format XX.XX (it must have two decimal places).')
#             elif price < 0:
#                 print('Price cannot be negative. Please enter a positive price.')
#             else:
#                 return price
#         except InvalidOperation:
#             print('Numbers only. Please enter a valid price.')

# # modified to accept an optional is_update parameter -> use in modify_item()
# def get_item_quantity(item_name, is_update=False):
#     while True:
#         try:    
#             quantity_input_string = input(f'Enter the quantity for {item_name} ')
#             # if this is an update and the user didn't enter a quantity, return early
#             if is_update and not quantity_input_string:
#                 return None
#             quantity = int(quantity_input_string)
#             if quantity <= 0:
#                 print('Quantity must be positive. Please enter a positive quantity.')
#                 continue
#             return quantity
#         except ValueError:
#             print('Whole numbers only. Please enter a valid quantity.')

# def confirm_item(item_name, item_price, item_quantity):
#     while True:
#         confirmation = input(f'You entered {item_quantity} {item_name} at ${item_price} each. Is this correct? (y/n) ')
#         if confirmation.lower() == 'y':
#             print(f'{item_name} entry confirmed.')
#             return True
#         elif confirmation.lower() == 'n':
#             print(f'{item_name} entry cancelled.')
#             return False
#         else:
#             print('Please enter \'y\' or \'n\'.')

# def main():
#     # Part 2: prompt the user for two items and create two ItemToPurchase objects
#     # This array holds the two ItemToPurchase objects. the enter_item() function returns an ItemToPurchase object wach time it is called
#     itemsToPurchase = []

#     for i in range(2):
#         itemsToPurchase.append(enter_item())

#     # Part 3: calculate and output the total cost
#     LINE_LENGTH = 45 # constant -> item_name (20) + quantity (3) + other chars (9) + price (6) + total (7) in format string

#     print(f'-' * LINE_LENGTH)
#     print(f'TOTAL COST - RECEIPT'.center(LINE_LENGTH))
#     print(f'-' * LINE_LENGTH)
#     total = Decimal('0.00') # Decimal aviods floating point errors
#     for item in itemsToPurchase:
#         item.print_item_cost()
#         total += item.item_total
#     print(f'-' * LINE_LENGTH)
#     print(f'Total: ${total:.2f}'.center(LINE_LENGTH))
#     print(f'-' * LINE_LENGTH)
    
# if __name__ == '__main__':
#     main()