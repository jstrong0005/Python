import textwrap
import os

rows, cols = (30, 80)

grid_Map = [[0 for i in range(cols)]for j in range(rows)]

#print(*grid_Map,sep='')
#print(''.join(map(str, grid_Map)))
#for i in grid_Map:
#    print(i,end='')

grid_chars = {32: None, 39: None, 44: None, 91: None, 93: None}
#print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
grid_Map[4][15] = '█'
grid_Map[4][16] = '█'
grid_Map[4][17] = '█'
grid_Map[4][18] = '█'
grid_Map[4][19] = '█'
grid_Map[4][20] = '█'

grid_Map[5][14] = '█'
grid_Map[5][15] = '█'
grid_Map[5][16] = '░'
grid_Map[5][17] = '░'
grid_Map[5][18] = '█'
grid_Map[5][19] = '░'
grid_Map[5][20] = '░'
grid_Map[5][21] = '█'

grid_Map[6][15] = '█'
grid_Map[6][16] = '█'
grid_Map[6][17] = '█'
grid_Map[6][18] = '█'
grid_Map[6][19] = '█'
grid_Map[6][20] = '█'

grid_Map[7][14] = '█'
grid_Map[7][16] = '█'
grid_Map[7][18] = '█'
grid_Map[7][20] = '█'
grid_Map[7][21] = '█'
#grid_Map[24][19] = '░'

os.system('cls')
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))