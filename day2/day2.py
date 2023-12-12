#%%
import re
#%%
# 12 red cubes, 13 green cubes, and 14 blue
limit = {'red': 12, 'green': 13, 'blue': 14}

#%%

file1 = open('input.txt', 'r')
count = 0

for line in file1:
    gm, tmp = line.split(': ')
    idx = int(gm.split(' ')[1])

    gms = tmp.split('; ')
    
    allowed = True
    for gm in gms:
        round = gm.split(', ')
        for g in round:
            num = g.split(' ')[0]
            col = g.split(' ')[1].strip()
            if int(num) > limit[col]:
                print("Line{}: {}".format(count, line.strip()))
                print("Invalid")
                allowed = False
    if allowed:
        count += idx    

# Closing files
file1.close()
print(count)
# %%
# %%



file1 = open('input.txt', 'r')
count = 0

for line in file1:
    limit = {'red': 0, 'green': 0, 'blue': 0}
    gm, tmp = line.split(': ')
    idx = int(gm.split(' ')[1])

    gms = tmp.split('; ')

    for gm in gms:
        round = gm.split(', ')
        for g in round:
            num = int(g.split(' ')[0])
            col = g.split(' ')[1].strip()
            if num > limit[col]:
                limit[col] = num

    
    count += (limit['red'] * limit['green'] * limit['blue'])  
# %%
