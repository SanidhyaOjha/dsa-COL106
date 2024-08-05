grid_representation = [[0,0,1], [0,0,1]]
resu = ''
l = len(grid_representation)
for i in range(l):
    for j in grid_representation[i]:
        resu = resu +str(j)  + ' '
    if i != l-1:
        resu += '\n'

print(resu)