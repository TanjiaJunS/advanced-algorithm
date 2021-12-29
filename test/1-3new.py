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
        if im[0] != 0 and im[1] != 0:
            print(im[0]+im[1])
except:
    pass