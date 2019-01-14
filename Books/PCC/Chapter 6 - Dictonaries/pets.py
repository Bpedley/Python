pets = {
    'Bucks': {
        'animal': 'dog',
        'owner_name': 'Bob',
        },
    'Murzik': {
        'animal': 'cat',
        'owner_name': 'Alice',
        },
    'Kissy': {
        'animal': 'bunny',
        'owner_name': 'Mike',
        },
}

for pet, pet_info in pets.items():
    print('\nPet name: ' + pet)
    print('Kind of animal: ' + pet_info['animal'])
    print('Onwer name: ' + pet_info['owner_name'])