import textwrap
import os
import readchar


mapcoord = [0,1]
orig_grid = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
map_grid = (orig_grid[:mapcoord[0]] + 'K' + (orig_grid[mapcoord[1]:]))
run = True

print(textwrap.fill(map_grid,20))

def request_input(mapcoord, orig_grid):
    updated_grid = orig_grid
    pressed = readchar.readkey()
    if pressed == 'a':
        print("you pressed a")
        if mapcoord[0] % 20 != 0:
            mapcoord[0] -= 1
            mapcoord[1] -= 1
        os.system('cls')
        updated_grid = (orig_grid[:mapcoord[0]] + 'K' + (orig_grid[mapcoord[1]:]))
        print(textwrap.fill(updated_grid,20))
    elif pressed == 'w':
        print("you pressed w")
        if mapcoord[0] >= 20:
            mapcoord[0] -= 20
            mapcoord[1] -= 20
        os.system('cls')
        updated_grid = (orig_grid[:mapcoord[0]] + 'K' + (orig_grid[mapcoord[1]:]))
        print(textwrap.fill(updated_grid,20))
    elif pressed == 's':
        print("you pressed s")
        if mapcoord[0] < 180:
            mapcoord[0] += 20
            mapcoord[1] += 20
        os.system('cls')
        updated_grid = (orig_grid[:mapcoord[0]] + 'K' + (orig_grid[mapcoord[1]:]))
        print(textwrap.fill(updated_grid,20))
    elif pressed == 'd':
        print("you pressed d")
        if mapcoord[1] % 20 != 0:
            mapcoord[0] += 1
            mapcoord[1] += 1
        os.system('cls')
        updated_grid = (orig_grid[:mapcoord[0]] + 'K' + (orig_grid[mapcoord[1]:]))
        print(textwrap.fill(updated_grid,20))
    return mapcoord


while run == True:
    mapcoord = request_input(mapcoord, orig_grid)


