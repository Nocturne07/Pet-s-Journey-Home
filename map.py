def create_map(n: int):
    '''
    Initialises and returns an n x n grid representing the game map.
    '''
    grid = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(' ')
        grid.append(row)
    
    return grid

def display_map(grid: list[list[str]], pet_position: tuple[int, int], home_position: tuple[int, int]):
    '''
    Prints the current state of the grid in a readable map format.
    '''
    for i in range(len(grid)):
        print('|', end='')
        for j in range(len(grid[i])):
            if (i, j) == pet_position:
                print(' P ', end='|')
            elif (i, j) == home_position:
                print(' H ', end='|')
            else:
                print(' . ', end='|')
        print()


if __name__ == '__main__':
    grid = create_map(4)
    print(grid)
    display_map(grid, (0, 0), (3, 3))