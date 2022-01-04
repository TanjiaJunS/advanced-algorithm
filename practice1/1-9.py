

def point_print(a):
    points = []

import sys
try:
    items = []
    while True:
        item = sys.stdin.readline().strip()
        if item == '':
            break
        item = list(map(int,list(item.split())))
        items.append(item)
    case_num = items[0][0]
    #print(items)
    for i in range(0,case_num*2+1):
        if i == 0:
            continue
        elif i%2 == 1:
            continue
        else:
            if len(items[i]) <= 4:
                print(-1)
            else:
                point_print(items[i])

except:
    pass



