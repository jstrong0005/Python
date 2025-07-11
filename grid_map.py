import textwrap
import os
import time

rows, cols = (30, 80)

grid_Maporig = [[0 for i in range(cols)]for j in range(rows)]
grid_Map = grid_Maporig
#print(*grid_Map,sep='')
#print(''.join(map(str, grid_Map)))
#for i in grid_Map:
#    print(i,end='')
critterx = 0
crittery = 0

grid_chars = {32: None, 39: None, 44: None, 91: None, 93: None}
#print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
def map_init(grid_Maporig, grid_Map):
    grid_Map = grid_Maporig
    return (grid_Map)

def character_init(critterx, crittery, grid_Map, grid_Maporig):
    grid_Map[(4 + crittery)][(15 + critterx)] = '0'
    grid_Map[(4 + crittery)][(16 + critterx)] = '0'
    grid_Map[(4 + crittery)][(17 + critterx)] = '0'
    grid_Map[(4 + crittery)][(18 + critterx)] = '0'
    grid_Map[(4 + crittery)][(19 + critterx)] = '0'
    grid_Map[(4 + crittery)][(20 + critterx)] = '0'
    grid_Map[(5 + crittery)][(14 + critterx)] = '0'
    grid_Map[(5 + crittery)][(15 + critterx)] = '0'
    grid_Map[(5 + crittery)][(16 + critterx)] = '0'
    grid_Map[(5 + crittery)][(17 + critterx)] = '0'
    grid_Map[(5 + crittery)][(18 + critterx)] = '0'
    grid_Map[(5 + crittery)][(19 + critterx)] = '0'
    grid_Map[(5 + crittery)][(20 + critterx)] = '0'
    grid_Map[(5 + crittery)][(21 + critterx)] = '0'
    grid_Map[(6 + crittery)][(15 + critterx)] = '0'
    grid_Map[(6 + crittery)][(16 + critterx)] = '0'
    grid_Map[(6 + crittery)][(17 + critterx)] = '0'
    grid_Map[(6 + crittery)][(18 + critterx)] = '0'
    grid_Map[(6 + crittery)][(19 + critterx)] = '0'
    grid_Map[(6 + crittery)][(20 + critterx)] = '0'
    grid_Map[(7 + crittery)][(14 + critterx)] = '0'
    grid_Map[(7 + crittery)][(16 + critterx)] = '0'
    grid_Map[(7 + crittery)][(18 + critterx)] = '0'
    grid_Map[(7 + crittery)][(20 + critterx)] = '0'
    grid_Map[(7 + crittery)][(21 + critterx)] = '0'

def character(critterx, crittery, grid_Map, grid_Maporig):
    grid_Map[(4 + crittery)][(15 + critterx)] = '█'
    grid_Map[(4 + crittery)][(16 + critterx)] = '█'
    grid_Map[(4 + crittery)][(17 + critterx)] = '█'
    grid_Map[(4 + crittery)][(18 + critterx)] = '█'
    grid_Map[(4 + crittery)][(19 + critterx)] = '█'
    grid_Map[(4 + crittery)][(20 + critterx)] = '█'
    grid_Map[(5 + crittery)][(14 + critterx)] = '█'
    grid_Map[(5 + crittery)][(15 + critterx)] = '█'
    grid_Map[(5 + crittery)][(16 + critterx)] = '░'
    grid_Map[(5 + crittery)][(17 + critterx)] = '░'
    grid_Map[(5 + crittery)][(18 + critterx)] = '█'
    grid_Map[(5 + crittery)][(19 + critterx)] = '░'
    grid_Map[(5 + crittery)][(20 + critterx)] = '░'
    grid_Map[(5 + crittery)][(21 + critterx)] = '█'
    grid_Map[(6 + crittery)][(15 + critterx)] = '█'
    grid_Map[(6 + crittery)][(16 + critterx)] = '█'
    grid_Map[(6 + crittery)][(17 + critterx)] = '█'
    grid_Map[(6 + crittery)][(18 + critterx)] = '█'
    grid_Map[(6 + crittery)][(19 + critterx)] = '█'
    grid_Map[(6 + crittery)][(20 + critterx)] = '█'
    grid_Map[(7 + crittery)][(14 + critterx)] = '█'
    grid_Map[(7 + crittery)][(16 + critterx)] = '█'
    grid_Map[(7 + crittery)][(18 + critterx)] = '█'
    grid_Map[(7 + crittery)][(20 + critterx)] = '█'
    grid_Map[(7 + crittery)][(21 + critterx)] = '█'




while True:
    character_init(critterx, crittery, grid_Map, grid_Maporig)
    critterx += 1
    crittery += 1
    character(critterx, crittery, grid_Map, grid_Maporig)
    print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
    time.sleep(0.5)
    os.system('cls')
    character_init(critterx, crittery, grid_Map, grid_Maporig)
    critterx += 1
    crittery += 1
    character(critterx, crittery, grid_Map, grid_Maporig)
    print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
    time.sleep(0.5)
    os.system('cls')
    character_init(critterx, crittery, grid_Map, grid_Maporig)
    critterx -= 2
    crittery -= 2
    character(critterx, crittery, grid_Map, grid_Maporig)
    print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
    time.sleep(0.5)
    os.system('cls')



"""
#grid_Map[24][19] = '░'


#print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))

#print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))

#map_init(grid_Maporig, grid_Map)
character(critterx, crittery, grid_Map, grid_Maporig)
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
#map_init(grid_Maporig, grid_Map)
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
#map_init(grid_Maporig, grid_Map)
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx -= 2
crittery -= 2
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
character_init(critterx, crittery, grid_Map, grid_Maporig)
critterx += 1
crittery += 1
character(critterx, crittery, grid_Map, grid_Maporig)
print(textwrap.fill(str(grid_Maporig).translate(grid_chars), 80))
time.sleep(0.5)
os.system('cls')
"""
"""
os.system('cls')
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
print('')
crittery = crittery + 1
character(critterx, crittery, grid_Map, grid_Maporig)
time.sleep(0.5)
os.system('cls')
os.system('cls')
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
print('')
crittery = crittery + 1
character(critterx, crittery, grid_Map, grid_Maporig)
time.sleep(0.5)
os.system('cls')
os.system('cls')
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
print('')
crittery = crittery + 1
character(critterx, crittery, grid_Map, grid_Maporig)
time.sleep(0.5)
os.system('cls')
os.system('cls')
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
print('')
crittery = crittery + 1
character(critterx, crittery, grid_Map, grid_Maporig)
time.sleep(0.5)
os.system('cls')
os.system('cls')
print(textwrap.fill(str(grid_Map).translate(grid_chars), 80))
print('')
crittery = crittery + 1
character(critterx, crittery, grid_Map, grid_Maporig)
time.sleep(0.5)
os.system('cls')
"""