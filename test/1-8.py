#获取输入的函数

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
    max = items[0][0]
    for i in range(1,max+1):
        item = items[i]
        sum = 0
        for i in item:
            sum = sum + i
        print(sum - item[0])
        print()
except:
    pass

