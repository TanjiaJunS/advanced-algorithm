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
    for im in items:
        if im[0] != 0:
            sum = 0
            for i in im:
                sum = sum + i
            print(sum-im[0])
except:
    pass