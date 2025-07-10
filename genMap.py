import textwrap
#map = "O"

wtf = ""
wtf_append = "O"
grid_resolution = 3200


for i in range(grid_resolution):
    wtf = wtf + wtf_append

#print(wtf)
print(" ")
print(textwrap.fill(wtf, 80))