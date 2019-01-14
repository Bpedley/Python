def sandwich_order(*items):
    print('\nMaking sandwich with the following items:')
    for item in items:
        print('- ' + item)

sandwich_order('tomate', 'cheese', 'beef')
sandwich_order('tomate', 'cheese', 'beef', 'pork')
sandwich_order('beef')