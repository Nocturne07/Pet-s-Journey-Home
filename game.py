from pet import Pet
from map import create_map, display_map
from random_events import random_event

def choose_difficulty():
    while True:
        difficulty = input('Choose game difficulty (easy|medium|hard): ').strip().lower()
        if difficulty == 'easy':
            return 6, 10  # grid size, base energy cost
        elif difficulty == 'medium':
            return 6, 15
        elif difficulty == 'hard':
            return 7, 15
        else:
            print('Invalid input.')

def choose_pet():
    valid_pet_types = ['dog', 'cat', 'bird']
    
    while True:
        pet_type = input('Choose your pet type (dog|cat|bird): ').strip().lower()
        if pet_type in valid_pet_types:
            break
        else:
            print('Invalid pet type.')
        
    while True:
        name = input('Give your pet a name: ').strip()
        if name:
            break
        else:
            print('Name cannot be empty.')

    return name, pet_type

def play_game():
    grid_size, base_energy_loss = choose_difficulty()

    # set home and pet positions
    start_position = (0, 0)
    home_position = (grid_size - 1, grid_size - 1)

    name, pet_type = choose_pet()
    pet = Pet(name=name, pet_type=pet_type, position=start_position)

    while True:
        if pet.energy <= 0: 
            pet.alive = False
            break

        if not pet.alive or pet.position == home_position:
            break

        grid = create_map(grid_size)
        display_map(grid, pet.position, home_position)
        print(f'{pet.name} - Energy: {pet.energy}, Inventory: {pet.inventory}')

        command = input('Action (move: up|down|left|right, or use [item]): ').strip().lower()

        if command.startswith('use '):
            item = command[4:].strip()
            pet.use_item(item)
            continue  

        elif command in ['up', 'down', 'left', 'right']:
            moved = pet.move(command, grid_size, base_energy_loss)
            if moved:
                if pet.position == home_position or not pet.alive:
                    break

                random_event(pet)
                
                if not pet.alive:
                    break

        else:
            print('Invalid action.')
            continue

    if not pet.alive:
        print('GAME OVER.')
    elif pet.position == home_position and pet.alive:
        print(f'{pet.name} is safely back home. Congratulations!')
