#%%
import re

 #%%
 
total = 0
# Using for loop
file1 = open('input.txt', 'r')
count = 0
print("Using for loop")
for line in file1:
    count += 1
    x = re.findall(r'\d', line)
    # re.match('^\D*\d\D*$', item)
    first = int(x[0]) *10
    last = int(x[-1])
    addition = first + last
    total += (first + last)
    print("Line{}: {}".format(count, line.strip()))
    print(addition)
print(total)
# Closing files
file1.close()
# %%
