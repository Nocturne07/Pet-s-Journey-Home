class Pet:
    def __init__(self, name: str, pet_type: str, position: tuple[int, int]):
        self.name = name
        self.pet_type = pet_type
        self.position = position
        self.inventory = ['food']
        self.alive = True
        self.shielded = False

        if pet_type == 'dog':
            self.energy = 160
            self.ability = 'trap_resist'
        elif pet_type == 'cat':
            self.energy = 140
            self.ability = 'enemy_evasion'
        elif pet_type == 'bird':
            self.energy = 100
            self.ability = 'energy_saver'

    def move(self, direction: str, grid_size: int, energy_cost: int):
        x, y = self.position
        if direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < grid_size - 1:
            x += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'right' and y < grid_size - 1:
            y += 1
        else:
            print('Invalid move.')
            return False

        self.position = (x, y)

        actual_cost = energy_cost
        if self.ability == 'energy_saver':
            actual_cost = energy_cost - 5

        self.energy -= actual_cost
    
        if self.energy <= 0:
            self.alive = False
            print(f"{self.name} has run out of energy and didn't make it home.")

        return True

    def use_item(self, item: str):
        if item in self.inventory:
            if item == 'food':
                self.energy += 30
                print(f'{self.name} eats some food and regains energy.')
            elif item == 'water':
                self.energy += 20
                print(f'{self.name} drinks water and feels refreshed.')
            elif item == 'shield':
                print(f'{self.name} is protected from the next trap!')
                self.shielded = True
            else:
                print("Item can't be used.")
            self.inventory.remove(item)
        else:
            print('Item not in inventory.')
