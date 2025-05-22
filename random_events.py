import random
from items import find_item

def random_event(pet):
    event = random.choice(['nothing', 'find_item', 'trap', 'enemy'])

    if event == 'nothing':
        print('The road is quiet.')
    elif event == 'find_item':
        find_item(pet)
    elif event == 'trap':
        if pet.shielded:
            print(f'{pet.name} was protected by a shield! No energy lost.')
            pet.shielded = False
        elif pet.ability == 'trap_resist' and random.random() < 0.5:
            print(f'{pet.name} sensed the trap and avoided it!')
        else:
            print('Hit a trap! Lost energy.')
            pet.energy -= 10

    elif event == 'enemy':
        if pet.shielded:
            print(f'{pet.name} blocked the wild animal with a shield! No energy lost.')
            pet.shielded = False
        elif pet.ability == 'enemy_evasion' and random.random() < 0.5:
            print(f"{pet.name} sensed the danger ahead of time.")
        else:
            print('A wild animal chases you! Lose energy while escaping.')
            pet.energy -= 15
