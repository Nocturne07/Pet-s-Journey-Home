import random

def find_item(pet):
    item = random.choice(['food', 'water', 'shield', 'nothing'])
    if item != 'nothing':
        print(f'You found a {item}!')
        pet.inventory.append(item)
    else:
        print('You found nothing this time.')