sandwich_orders = ['pastrami', 'Hot Brown', 'The Schimmel Reuben', 'pastrami', 'Fried Chicken', 'Turkish Grilled Cheese', 'pastrami']
finished_sandwiches = []

print('Deli has run out of pastrami!')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    print('I made your ' + current_sandwich + ' sandwich')
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches that was made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + ' sandwich')
