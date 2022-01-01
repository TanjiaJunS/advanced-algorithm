
def get_i(power):
    i = 1
    strength_sum = 0
    while(power>=i**2):
        power -= i**2
        i += 1
    return i-1

import sys
try:
    items = []
    while True:
        item = sys.stdin.readline().strip()
        if item == '':
            break
        item = list(map(int,list(item.split())))
        items.append(item)
    #print(items)
    case_num = items[0][0]
    for i in range(1,case_num+1):
        print(get_i(items[i][0]))

except:
    pass
